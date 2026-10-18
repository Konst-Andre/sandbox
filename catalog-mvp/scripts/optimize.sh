#!/usr/bin/env bash
# Оптимізація GLB з Meshy для вебу. Потрібен Node 18+.
# Використання: ./optimize.sh input.glb output.glb
# Результат на Nurofen stand: 34,2 МБ -> 1,5 МБ (текстури 2K WebP, ~107 тис. трикутників, meshopt)
set -e
IN="$1"; OUT="$2"; T=$(mktemp -d)
npm i --no-save @gltf-transform/cli meshoptimizer sharp >/dev/null
G=./node_modules/.bin/gltf-transform
$G resize   "$IN"        $T/a.glb --width 2048 --height 2048
$G webp     $T/a.glb     $T/b.glb --quality 80
$G weld     $T/b.glb     $T/c.glb
$G simplify $T/c.glb     $T/d.glb --ratio 0.25 --error 0.001
$G meshopt  $T/d.glb     "$OUT"   --level high
