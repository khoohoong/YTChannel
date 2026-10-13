#!/usr/bin/env python3
"""Origin Plate Ep 1 — 4 accurate animated maps (Natural Earth data), clay-matched palette.
Based on the Ep 1 SEA renderer; reads its geojson, writes only to this folder. 1920x1080, no text
(labels go on in the editor). Usage: python3 render_maps_ep01.py [1234]"""
import json, math, os, sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch
from matplotlib.collections import LineCollection
import imageio.v2 as imageio

HERE = os.path.dirname(os.path.abspath(__file__))
GEO = os.path.join(HERE, "..", "..", "the-true-origin-of-southeast-asia", "maps", "ne_50m.geojson")
OUT = os.path.join(HERE, "map_clips"); os.makedirs(OUT, exist_ok=True)
W, H, DPI, FPS = 1920, 1080, 100, 24

# Clay palette — warm, matte, matches the clay stills
OCEAN="#A8C9D2"; LAND="#E9D5B3"; COAST="#C7A57A"; GRAT="#B8D4DB"
ACCENT="#C8553D"; GOLD="#F2B544"; HILITE="#F3C98B"

GJ = json.load(open(GEO))
def rings_of(g):
    t,c=g["type"],g["coordinates"]
    if t=="Polygon": return [np.asarray(r,float) for r in c]
    if t=="MultiPolygon": return [np.asarray(r,float) for p in c for r in p]
    return []
COUNTRIES={}
for f in GJ["features"]:
    nm=f["properties"].get("NAME") or f["properties"].get("ADMIN") or "?"
    COUNTRIES.setdefault(nm,[]).extend(rings_of(f["geometry"]))
ALL=[r for rs in COUNTRIES.values() for r in rs]

def path_of(rings):
    v,c=[],[]
    for r in rings:
        if len(r)<3: continue
        v.append(tuple(r[0])); c.append(Path.MOVETO)
        for p in r[1:]: v.append(tuple(p)); c.append(Path.LINETO)
        v.append(tuple(r[0])); c.append(Path.CLOSEPOLY)
    return Path(v,c)

def new_fig():
    fig=plt.figure(figsize=(W/DPI,H/DPI),dpi=DPI); fig.patch.set_facecolor(OCEAN)
    ax=fig.add_axes([0,0,1,1]); ax.set_axis_off(); ax.set_facecolor(OCEAN); return fig,ax

def basemap(ax, highlight=()):
    # soft drop shadow under land = "clay relief" feel
    sh=path_of([r+np.array([0.25,-0.25]) for r in ALL])
    ax.add_patch(PathPatch(sh,fc="#7FA3AD",ec="none",alpha=0.5,zorder=1))
    ax.add_patch(PathPatch(path_of(ALL),fc=LAND,ec="none",zorder=2))
    for nm in highlight:
        ax.add_patch(PathPatch(path_of(COUNTRIES.get(nm,[])),fc=HILITE,ec="none",zorder=3))
    ax.add_collection(LineCollection(ALL,colors=COAST,linewidths=0.8,zorder=4))
    g=[np.column_stack([np.full(91,lo),np.linspace(-90,90,91)]) for lo in range(-180,181,10)]
    g+=[np.column_stack([np.linspace(-180,180,181),np.full(181,la)]) for la in range(-80,81,10)]
    ax.add_collection(LineCollection(g,colors=GRAT,linewidths=0.5,zorder=0))

def gc(p1,p2,n=160):
    lo1,la1=map(math.radians,p1); lo2,la2=map(math.radians,p2)
    a=np.array([math.cos(la1)*math.cos(lo1),math.cos(la1)*math.sin(lo1),math.sin(la1)])
    b=np.array([math.cos(la2)*math.cos(lo2),math.cos(la2)*math.sin(lo2),math.sin(la2)])
    om=math.acos(np.clip(a@b,-1,1)); t=np.linspace(0,1,n)
    p=(np.sin((1-t)*om)[:,None]*a+np.sin(t*om)[:,None]*b)/math.sin(om)
    return np.degrees(np.arctan2(p[:,1],p[:,0])), np.degrees(np.arcsin(np.clip(p[:,2],-1,1)))

def ease(t): return t*t*(3-2*t)
def grab(fig): fig.canvas.draw(); return np.asarray(fig.canvas.buffer_rgba())[:,:,:3].copy()
def writer(n): return imageio.get_writer(os.path.join(OUT,n),fps=FPS,codec="libx264",quality=8,
                                         macro_block_size=8,ffmpeg_params=["-pix_fmt","yuv420p"])
def clear(d):
    for a in d: a.remove()
    d.clear()

def pin(ax,lon,lat,phase,scale,d,color=ACCENT):
    d.append(ax.scatter([lon],[lat],s=120*scale,c=color,zorder=8,edgecolors="white",linewidths=2))
    for k in range(2):
        p=(phase+k/2)%1
        d.append(ax.scatter([lon],[lat],s=(120+p*2200)*scale,facecolors="none",edgecolors=color,
                            linewidths=2.5*(1-p),alpha=(1-p)*0.8,zorder=7))

def route(ax,lon,lat,prog,d,dashed=False):
    k=max(2,int(prog*len(lon)))
    d+=ax.plot(lon[:k],lat[:k],color="white",lw=7,alpha=0.6,zorder=5,solid_capstyle="round")
    d+=ax.plot(lon[:k],lat[:k],color=ACCENT,lw=3.2,zorder=6,solid_capstyle="round",
               linestyle=(0,(4,2)) if dashed else "-")
    d.append(ax.scatter([lon[k-1]],[lat[k-1]],s=60,c=GOLD,zorder=8,edgecolors="none"))

def zoom(ax,v0,v1,t):
    lo0,lo1,la0,la1=[a+(b-a)*t for a,b in zip(v0,v1)]
    ax.set_xlim(lo0,lo1); ax.set_ylim(la0,la1)

ROME=(12.4964,41.9028); NAPLES=(14.2681,40.8518); BOLOGNA=(11.3426,44.4949); RICCIONE=(12.6551,43.9998)
CHICAGO=(-87.6298,41.8781); LONDON=(-0.1276,51.5072); NYC=(-74.006,40.7128)
TOKYO=(139.6917,35.6895); SYDNEY=(151.2093,-33.8688); BA=(-58.3816,-34.6037)

def map1():  # VO-1: Italy — Naples (Cavalcanti) + Rome (gricia), 8s
    N=8*FPS; fig,ax=new_fig(); basemap(ax,["Italy"]); d=[]; w=writer("MAP1_italy_naples_rome.mp4")
    for i in range(N):
        t=ease(i/(N-1)); clear(d); zoom(ax,(-2,30,33,50),(6.5,19.5,37.5,45.5),t)
        if t>0.35: pin(ax,*NAPLES,(i/FPS)%1,1,d)
        if t>0.6: pin(ax,*ROME,(i/FPS+.5)%1,1,d,GOLD)
        w.append_data(grab(fig))
    w.close(); plt.close(fig); print("MAP1 done")

def map2():  # VO-2: Rome 1944 + Bologna -> Riccione, 10s
    N=10*FPS; fig,ax=new_fig(); basemap(ax,["Italy"]); d=[]; w=writer("MAP2_rome_riccione.mp4")
    lo,la=gc(BOLOGNA,RICCIONE,100)
    for i in range(N):
        t=i/(N-1); clear(d); zoom(ax,(7,19,38,47),(9,16,40.8,45.3),ease(t))
        pin(ax,*ROME,(i/FPS)%1,1,d,GOLD)
        if t>0.4: route(ax,lo,la,ease(np.clip((t-0.4)/0.4,0,1)),d,dashed=True)
        if t>0.8: pin(ax,*RICCIONE,(i/FPS)%1,1,d)
        w.append_data(grab(fig))
    w.close(); plt.close(fig); print("MAP2 done")

def map3():  # VO-3: Rome <-> Chicago, 8s
    N=8*FPS; fig,ax=new_fig(); basemap(ax,["Italy","United States of America"]); d=[]
    w=writer("MAP3_rome_chicago.mp4"); lo,la=gc(ROME,CHICAGO)
    ax.set_xlim(-105,30); ax.set_ylim(15,68)
    for i in range(N):
        t=i/(N-1); clear(d); pin(ax,*ROME,(i/FPS)%1,1,d,GOLD)
        route(ax,lo,la,ease(np.clip(t/0.7,0,1)),d)
        if t>0.7: pin(ax,*CHICAGO,(i/FPS)%1,1.2,d)
        w.append_data(grab(fig))
    w.close(); plt.close(fig); print("MAP3 done")

def map4():  # VO-3B: carbonara goes global, 8s
    N=8*FPS; fig,ax=new_fig(); basemap(ax); d=[]; w=writer("MAP4_goes_global.mp4")
    dests=[LONDON,NYC,CHICAGO,TOKYO,SYDNEY,BA]; arcs=[gc(ROME,x) for x in dests]
    ax.set_xlim(-130,175); ax.set_ylim(-50,72)
    for i in range(N):
        t=i/(N-1); clear(d); pin(ax,*ROME,(i/FPS)%1,1.2,d,GOLD)
        for j,(lo,la) in enumerate(arcs):
            pr=np.clip((t-0.08*j)/0.5,0,1)
            if pr>0: route(ax,lo,la,ease(pr),d)
            if pr>=1: pin(ax,*dests[j],(i/FPS+j/6)%1,0.8,d)
        w.append_data(grab(fig))
    w.close(); plt.close(fig); print("MAP4 done")

if __name__=="__main__":
    fns={"1":map1,"2":map2,"3":map3,"4":map4}
    for k in (sys.argv[1] if len(sys.argv)>1 else "1234"): fns[k]()
