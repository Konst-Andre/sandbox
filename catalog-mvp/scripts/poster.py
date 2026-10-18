import numpy as np, trimesh, math, sys, time
from PIL import Image
t0=time.time()
sc=trimesh.load(sys.argv[1])
m=trimesh.util.concatenate(list(sc.geometry.values())) if hasattr(sc,'geometry') else sc
tex=m.visual.material.baseColorTexture
tex=np.asarray(tex.convert('RGB'))
TH,TW=tex.shape[:2]
uv=m.visual.uv
V=m.vertices.copy(); F=m.faces
print('tris',len(F),'tex',tex.shape)
# camera: yaw, pitch
yaw=math.radians(float(sys.argv[2])); pitch=math.radians(8)
Ry=np.array([[math.cos(yaw),0,math.sin(yaw)],[0,1,0],[-math.sin(yaw),0,math.cos(yaw)]])
Rx=np.array([[1,0,0],[0,math.cos(pitch),-math.sin(pitch)],[0,math.sin(pitch),math.cos(pitch)]])
R=Rx@Ry
P=V@R.T
W,H=1600,2000
mn,mx=P.min(0),P.max(0)
s=min(W*0.82/(mx[0]-mn[0]),H*0.9/(mx[1]-mn[1]))
cx=(mx[0]+mn[0])/2; cy=(mx[1]+mn[1])/2
X=(P[:,0]-cx)*s+W/2; Y=H/2-(P[:,1]-cy)*s; Z=P[:,2]
N=m.face_normals@R.T
L=np.array([-0.4,0.6,0.7]); L/=np.linalg.norm(L)
img=np.zeros((H,W,4),np.uint8); zb=np.full((H,W),-1e9)
for f in range(len(F)):
    a,b,c=F[f]
    x0,y0,x1,y1,x2,y2=X[a],Y[a],X[b],Y[b],X[c],Y[c]
    xmin=max(int(min(x0,x1,x2)),0); xmax=min(int(max(x0,x1,x2))+1,W-1)
    ymin=max(int(min(y0,y1,y2)),0); ymax=min(int(max(y0,y1,y2))+1,H-1)
    if xmax<xmin or ymax<ymin: continue
    den=(y1-y2)*(x0-x2)+(x2-x1)*(y0-y2)
    if abs(den)<1e-9: continue
    gx,gy=np.meshgrid(np.arange(xmin,xmax+1)+0.5,np.arange(ymin,ymax+1)+0.5)
    w0=((y1-y2)*(gx-x2)+(x2-x1)*(gy-y2))/den
    w1=((y2-y0)*(gx-x2)+(x0-x2)*(gy-y2))/den
    w2=1-w0-w1
    ins=(w0>=-1e-6)&(w1>=-1e-6)&(w2>=-1e-6)
    if not ins.any(): continue
    z=w0*Z[a]+w1*Z[b]+w2*Z[c]
    sub=zb[ymin:ymax+1,xmin:xmax+1]
    ok=ins&(z>sub)
    if not ok.any(): continue
    u=w0*uv[a,0]+w1*uv[b,0]+w2*uv[c,0]
    v=w0*uv[a,1]+w1*uv[b,1]+w2*uv[c,1]
    tx=np.clip((u%1.0*(TW-1)).astype(int),0,TW-1)
    ty=np.clip(((1-v%1.0)*(TH-1)).astype(int),0,TH-1)
    col=tex[ty,tx].astype(float)
    n=N[f]; 
    if n[2]<0: n=-n
    sh=0.55+0.45*max(0,float(n@L))
    col=np.clip(col*sh,0,255).astype(np.uint8)
    sub[ok]=z[ok]
    reg=img[ymin:ymax+1,xmin:xmax+1]
    reg[ok,:3]=col[ok]; reg[ok,3]=255
Image.fromarray(img).resize((800,1000),Image.LANCZOS).save(sys.argv[3])
print('done',round(time.time()-t0,1),'s')
