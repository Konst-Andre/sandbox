#!/usr/bin/env python3
"""Обробка сирих GLB з inbox/ -> models/, posters/, catalog.json.

Вхід: inbox/<Brand>__<Name>.glb  (або просто <Name>.glb)
      inbox/<те саме ім'я>.json  (необов'язково: {"brand","name","yaw"})
Вихід: models/<id>.glb, posters/<id>.webp, запис у catalog.json; сирий файл з inbox видаляється.
"""
import json, os, re, shutil, struct, subprocess, sys, tempfile, unicodedata
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
INBOX, MODELS, POSTERS = BASE / 'inbox', BASE / 'models', BASE / 'posters'
CATALOG = BASE / 'catalog.json'
GT = os.environ.get('GT_BIN') or str(BASE / 'node_modules/.bin/gltf-transform')
TARGET_TRIS = 100_000   # цільова кількість трикутників після спрощення
DEFAULT_YAW = 140       # кут огляду для постера (градуси)


def run(*args):
    subprocess.run([str(a) for a in args], check=True)


def slug(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode()
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')


def count_tris(glb):
    data = Path(glb).read_bytes()
    clen, _ = struct.unpack('<II', data[12:20])
    j = json.loads(data[20:20 + clen])
    n = 0
    for m in j.get('meshes', []):
        for p in m['primitives']:
            if p.get('mode', 4) == 4 and 'indices' in p:
                n += j['accessors'][p['indices']]['count'] // 3
    return n


def process(glb):
    stem = glb.stem
    brand, name = (stem.split('__', 1) + [None])[:2] if '__' in stem else ('Інше', stem)
    if name is None:
        name = brand
    meta = {}
    side = glb.with_suffix('.json')
    if side.exists():
        meta = json.loads(side.read_text(encoding='utf-8'))
    brand = meta.get('brand', brand.replace('_', ' '))
    name = meta.get('name', name.replace('_', ' '))
    yaw = float(meta.get('yaw', DEFAULT_YAW))
    mid = slug(stem) or 'model-' + str(abs(hash(stem)) % 10000)
    print(f'== {glb.name}: id={mid} brand={brand!r} name={name!r} yaw={yaw}')

    with tempfile.TemporaryDirectory() as t:
        t = Path(t)
        run(GT, 'resize', glb, t / 'a.glb', '--width', 2048, '--height', 2048)
        tris = count_tris(t / 'a.glb')
        ratio = min(1.0, TARGET_TRIS / tris) if tris else 1.0
        print(f'   трикутників: {tris}, ratio: {ratio:.3f}')

        # 1) файл для сайту: WebP, weld, simplify, meshopt
        run(GT, 'webp', t / 'a.glb', t / 'b.glb', '--quality', 80)
        run(GT, 'weld', t / 'b.glb', t / 'c.glb')
        src = t / 'c.glb'
        if ratio < 0.95:
            run(GT, 'simplify', t / 'c.glb', t / 'd.glb', '--ratio', f'{ratio:.4f}', '--error', 0.001)
            src = t / 'd.glb'
        MODELS.mkdir(exist_ok=True)
        out = MODELS / f'{mid}.glb'
        run(GT, 'meshopt', src, out, '--level', 'high')

        # 2) постер: рендер з проміжного GLB без meshopt і WebP (JPEG/PNG-текстури)
        psrc = t / 'a.glb'
        if ratio < 0.95:
            run(GT, 'simplify', t / 'a.glb', t / 'p.glb', '--ratio', f'{ratio:.4f}', '--error', 0.001)
            psrc = t / 'p.glb'
        POSTERS.mkdir(exist_ok=True)
        run(sys.executable, BASE / 'scripts/poster.py', psrc, yaw, POSTERS / f'{mid}.webp')

    size = round(out.stat().st_size / 1e6, 1)
    items = json.loads(CATALOG.read_text(encoding='utf-8')) if CATALOG.exists() else []
    entry = {'id': mid, 'brand': brand, 'name': name,
             'glb': f'models/{mid}.glb', 'poster': f'posters/{mid}.webp', 'sizeMB': size}
    for i, it in enumerate(items):
        if it['id'] == mid:
            items[i] = entry
            break
    else:
        items.append(entry)
    CATALOG.write_text(json.dumps(items, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    glb.unlink()
    if side.exists():
        side.unlink()
    print(f'   готово: {size} МБ')
    return mid


def main():
    files = sorted(INBOX.glob('*.glb')) if INBOX.exists() else []
    if not files:
        print('inbox порожній')
        return 0
    done, failed = [], []
    for f in files:
        try:
            done.append(process(f))
        except Exception as e:  # одна погана модель не має зупиняти решту
            print(f'!! {f.name}: {e}', file=sys.stderr)
            failed.append(f.name)
    Path(os.environ.get('GITHUB_OUTPUT', os.devnull)).open('a').write('done=' + ', '.join(done) + '\n')
    print('оброблено:', done, 'помилки:', failed)
    return 1 if failed else 0


if __name__ == '__main__':
    sys.exit(main())
