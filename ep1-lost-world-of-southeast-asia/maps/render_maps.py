#!/usr/bin/env python3
"""Render this episode's 3 accurate animated map infographics from real Natural Earth data.
1920x1080 MP4, NO text (labels added in the editor). Reuses the series map machinery + palette.
  MAP1_sundaland  — the drowned Sunda Shelf highlighted over today's islands
  MAP2_routes     — Taiwan out + the great Austronesian ocean spread (Madagascar ... Rapa Nui)
  MAP3_angkor     — Khmer heartland + Angkor locator
"""
import json, math, os, sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch, Polygon
from matplotlib.collections import LineCollection
import imageio.v2 as imageio

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "map_clips"); os.makedirs(OUT, exist_ok=True)
W, H, DPI, FPS = 1920, 1080, 100, 24

OCEAN="#0E272E"; LAND="#5C4A33"; COAST="#243A40"; GRAT="#16323A"; AMBER="#E0A44E"; GOLD="#F4CE86"

with open(os.path.join(HERE, "ne_50m.geojson")) as f:
    GJ = json.load(f)

def rings_of(g):
    t,c = g["type"], g["coordinates"]
    if t=="Polygon": return [np.asarray(r,float) for r in c]
    if t=="MultiPolygon": return [np.asarray(r,float) for poly in c for r in poly]
    return []

def decim(r):
    if len(r) > 60: return np.vstack([r[::2], r[-1]])
    return r

COUNTRIES={}
for feat in GJ["features"]:
    nm = feat["properties"].get("NAME") or feat["properties"].get("ADMIN") or "?"
    COUNTRIES.setdefault(nm, [])
    COUNTRIES[nm] += [decim(r) for r in rings_of(feat["geometry"])]
ALL_RINGS=[r for rs in COUNTRIES.values() for r in rs]

def shift(lon, west): return (np.asarray(lon,float) - west) % 360.0

def split_seam(x,y):
    x=np.asarray(x); y=np.asarray(y)
    if len(x)<2: return [(x,y)]
    brk=np.where(np.abs(np.diff(x))>180)[0]
    if len(brk)==0: return [(x,y)]
    segs=[]; s=0
    for b in brk: segs.append((x[s:b+1],y[s:b+1])); s=b+1
    segs.append((x[s:],y[s:]))
    return [(a,b) for a,b in segs if len(a)>=2]

def compound(names_rings, west):
    verts,codes=[],[]
    for ring in names_rings:
        x=shift(ring[:,0],west); y=ring[:,1]
        for sx,sy in split_seam(x,y):
            if len(sx)>=3:
                verts.append((sx[0],sy[0])); codes.append(Path.MOVETO)
                for k in range(1,len(sx)): verts.append((sx[k],sy[k])); codes.append(Path.LINETO)
                verts.append((sx[0],sy[0])); codes.append(Path.CLOSEPOLY)
    return Path(verts,codes) if verts else None

def build_basemap(ax, west=-180):
    ax.set_facecolor(OCEAN)
    p=compound(ALL_RINGS, west)
    if p is not None: ax.add_patch(PathPatch(p, fc=LAND, ec="none", zorder=1))
    lines=[]
    for ring in ALL_RINGS:
        x=shift(ring[:,0],west); y=ring[:,1]
        for sx,sy in split_seam(x,y): lines.append(np.column_stack([sx,sy]))
    ax.add_collection(LineCollection(lines, colors=COAST, linewidths=0.5, zorder=2))
    g=[]
    for lon in range(-180,181,15):
        for sx,sy in split_seam(shift(np.full(91,lon),west), np.linspace(-90,90,91)):
            g.append(np.column_stack([sx,sy]))
    for lat in range(-75,76,15):
        for sx,sy in split_seam(shift(np.linspace(-180,180,181),west), np.full(181,lat)):
            g.append(np.column_stack([sx,sy]))
    ax.add_collection(LineCollection(g, colors=GRAT, linewidths=0.4, zorder=0))

def country_fill(ax, names, west, color, alpha, z, dyn):
    rings=[r for nm in names for r in COUNTRIES.get(nm,[])]
    p=compound(rings, west)
    if p is not None:
        pp=PathPatch(p, fc=color, ec="none", alpha=alpha, zorder=z); ax.add_patch(pp); dyn.append(pp)

def great_circle(p1,p2,n=150):
    lon1,lat1=map(math.radians,p1); lon2,lat2=map(math.radians,p2)
    v1=np.array([math.cos(lat1)*math.cos(lon1),math.cos(lat1)*math.sin(lon1),math.sin(lat1)])
    v2=np.array([math.cos(lat2)*math.cos(lon2),math.cos(lat2)*math.sin(lon2),math.sin(lat2)])
    om=math.acos(np.clip(np.dot(v1,v2),-1,1)); t=np.linspace(0,1,n)
    pts=(np.outer(np.ones(n),v1) if om<1e-6 else
         (np.sin((1-t)*om)[:,None]*v1+np.sin(t*om)[:,None]*v2)/math.sin(om))
    return (np.degrees(np.arctan2(pts[:,1],pts[:,0])), np.degrees(np.arcsin(np.clip(pts[:,2],-1,1))))

def ease(t): return t*t*(3-2*t)
def new_fig():
    fig=plt.figure(figsize=(W/DPI,H/DPI),dpi=DPI); fig.patch.set_facecolor(OCEAN)
    ax=fig.add_axes([0,0,1,1]); ax.set_axis_off(); return fig,ax
def grab(fig):
    fig.canvas.draw(); return np.asarray(fig.canvas.buffer_rgba())[:,:,:3].copy()

def marker(ax,lon,lat,west,phase,base,dyn):
    x=float(shift(lon,west))
    dyn.append(ax.scatter([x],[lat],s=70*base,c=GOLD,zorder=6,edgecolors="none"))
    for k in range(3):
        p=(phase+k/3.0)%1.0
        dyn.append(ax.scatter([x],[lat],s=(70+p*2600)*base,facecolors="none",
                   edgecolors=AMBER,linewidths=2.2*(1-p),alpha=(1-p)*0.9,zorder=5))

def glow_line(ax,x,y,dyn,wmul=1.0):
    dyn += ax.plot(x,y,color=AMBER,lw=7*wmul,alpha=0.18,zorder=4,solid_capstyle="round")
    dyn += ax.plot(x,y,color=GOLD,lw=2.4*wmul,alpha=0.95,zorder=5,solid_capstyle="round")

def clear(dyn):
    for a in dyn: a.remove()
    dyn.clear()

def writer(name):
    return imageio.get_writer(os.path.join(OUT,name), fps=FPS, codec="libx264",
        quality=8, macro_block_size=8, ffmpeg_params=["-pix_fmt","yuv420p"])

# Approx Sunda Shelf outline (the low-lying land exposed at the last glacial maximum that joined
# the Malay Peninsula, Sumatra, Borneo and Java). Hand-traced approximation for illustration; the
# real -120 m contour is more intricate. Labels + "Ice Age / Today" captions added in the editor.
SUNDA = np.array([
    (100.2,13.0),(102.5,9.5),(104.5,7.0),(104.8,4.5),(105.2,2.0),(106.5,-1.0),
    (106.0,-3.0),(108.5,-5.5),(112.0,-6.8),(115.5,-6.2),(117.5,-4.0),(118.8,-3.2),
    (118.5,-0.5),(117.0,2.5),(114.5,4.2),(113.0,5.0),(110.0,5.6),(106.5,6.2),
    (103.5,6.5),(101.2,7.5),(100.0,10.5),(100.2,13.0),
])

def shot_sundaland():
    print("MAP1 sundaland"); N=int(6*FPS); west=-180; fig,ax=new_fig(); build_basemap(ax,west); dyn=[]
    ax.set_xlim(shift(94,west),shift(122,west)); ax.set_ylim(-12,16)
    sx=shift(SUNDA[:,0],west); sy=SUNDA[:,1]
    for i in range(N):
        t=ease(i/(N-1)); clear(dyn)
        a=np.clip(t/0.7,0,1)
        # exposed shelf as amber "extra land"; islands still read through the low alpha + coastlines
        poly=Polygon(np.column_stack([sx,sy]), closed=True, fc=AMBER, ec=GOLD,
                     lw=1.6*a, alpha=0.42*a, zorder=1.5); ax.add_patch(poly); dyn.append(poly)
        w_gc = None
        w=None
        # subtle pulse outline
        poly2=Polygon(np.column_stack([sx,sy]), closed=True, fc="none", ec=GOLD,
                      lw=2.2*(0.5+0.5*math.sin(i/4.0)), alpha=0.5*a, zorder=6); ax.add_patch(poly2); dyn.append(poly2)
        _writer_frame(ax)
        FRAMES.append(grab(fig))
    _flush("MAP1_sundaland.mp4"); plt.close(fig); print("  done MAP1")

def shot_routes():
    print("MAP2 routes"); N=int(7*FPS); west=-30; fig,ax=new_fig(); build_basemap(ax,west); dyn=[]
    TAI=(121.15,22.8); ISEA=(120.0,-2.0)
    # Austronesian reach: Taiwan start, then the great spread to the far corners
    dests=[(46.9,-18.9),   # Madagascar (far west)
           (178.0,-17.7),  # Fiji
           (-172.0,-13.8), # Samoa
           (-109.37,-27.12),# Rapa Nui / Easter Island (far east)
           (-155.5,19.6),  # Hawaii
           (175.0,-39.0)]  # Aotearoa / NZ
    arc_tai=great_circle(TAI,ISEA,120)
    arcs=[great_circle(ISEA,d,160) for d in dests]; w=writer("MAP2_routes.mp4")
    ax.set_xlim(5,300); ax.set_ylim(-55,45)
    for i in range(N):
        t=i/(N-1); clear(dyn)
        # first the Taiwan -> Island SE Asia leg
        progT=np.clip(t/0.25,0,1); kT=max(2,int(progT*len(arc_tai[0])))
        if kT>=2:
            xt=shift(arc_tai[0][:kT],west)
            for a,b in split_seam(xt,arc_tai[1][:kT]): glow_line(ax,a,b,dyn,0.9)
        # then the ocean spread
        for j,(lon,lat) in enumerate(arcs):
            prog=np.clip((t-0.25-0.07*j)/0.6,0,1); k=max(2,int(prog*len(lon)))
            if k>=2:
                x=shift(lon[:k],west)
                for a,b in split_seam(x,lat[:k]): glow_line(ax,a,b,dyn,0.9)
                xe=float(shift(lon[k-1],west)); dyn.append(ax.scatter([xe],[lat[k-1]],s=40,c=GOLD,zorder=6,edgecolors="none"))
        marker(ax,TAI[0],TAI[1],west,(i/FPS)%1.0,0.9,dyn)
        w.append_data(grab(fig))
    w.close(); plt.close(fig); print("  done MAP2")

def shot_angkor():
    print("MAP3 angkor"); N=int(6*FPS); west=-180; fig,ax=new_fig(); build_basemap(ax,west); dyn=[]
    ANG=(103.867,13.412); terr=["Cambodia","Thailand","Laos"]; w=writer("MAP3_angkor.mp4")
    ax.set_xlim(shift(94,west),shift(114,west)); ax.set_ylim(4,24)
    for i in range(N):
        t=i/(N-1); clear(dyn); a=ease(np.clip(t/0.7,0,1))
        country_fill(ax,terr,west,AMBER,0.5*a,3,dyn)
        country_fill(ax,["Cambodia"],west,GOLD,0.35*a,4,dyn)
        if t>0.25: marker(ax,ANG[0],ANG[1],west,(i/FPS)%1.0,1.0,dyn)
        w.append_data(grab(fig))
    w.close(); plt.close(fig); print("  done MAP3")

# tiny frame buffer helpers for shot_sundaland (kept isolated so the others use direct writers)
FRAMES=[]
def _writer_frame(ax): pass
def _flush(name):
    global FRAMES
    w=writer(name)
    for fr in FRAMES: w.append_data(fr)
    w.close(); FRAMES=[]

if __name__=="__main__":
    fns={"1":shot_sundaland,"2":shot_routes,"3":shot_angkor}
    which=sys.argv[1] if len(sys.argv)>1 else "all"
    for k in ("123" if which=="all" else which): fns[k]()
    print("ALL DONE")
