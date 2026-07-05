#!/usr/bin/env python3
"""Render 6 accurate animated map infographics from real Natural Earth data.
Build basemap ONCE per shot; only animate dynamic overlays. 1920x1080 MP4, no text."""
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

# ---------------- shots ----------------
def shot1():
    print("shot1 reveal"); N=int(6*FPS); fig,ax=new_fig(); build_basemap(ax,-180); dyn=[]
    v0=(55,180,-52,58); v1=(92,150,-13,27); w=writer("MAP1_sea_reveal.mp4")
    sea=["Indonesia","Malaysia","Philippines","Vietnam","Thailand","Cambodia","Laos","Myanmar","Brunei","Timor-Leste"]
    for i in range(N):
        t=ease(i/(N-1)); clear(dyn)
        lo0=v0[0]+(v1[0]-v0[0])*t; lo1=v0[1]+(v1[1]-v0[1])*t; la0=v0[2]+(v1[2]-v0[2])*t; la1=v0[3]+(v1[3]-v0[3])*t
        if t>0.45: country_fill(ax,sea,-180,AMBER,0.16*ease((t-0.45)/0.55),3,dyn)
        ax.set_xlim(shift(lo0,-180),shift(lo1,-180)); ax.set_ylim(la0,la1)
        w.append_data(grab(fig))
    w.close(); plt.close(fig); print("  done MAP1")

def shot2():
    print("shot2 flores"); N=int(6*FPS); fig,ax=new_fig(); build_basemap(ax,-180); dyn=[]
    v0=(95,145,-14,22); v1=(117,124,-10.5,-6); FLO=(120.4439,-8.5314); w=writer("MAP2_flores_zoom.mp4")
    for i in range(N):
        t=ease(i/(N-1)); clear(dyn)
        lo0=v0[0]+(v1[0]-v0[0])*t; lo1=v0[1]+(v1[1]-v0[1])*t; la0=v0[2]+(v1[2]-v0[2])*t; la1=v0[3]+(v1[3]-v0[3])*t
        if t>0.4: marker(ax,FLO[0],FLO[1],-180,(i/FPS)%1.0,0.7+0.6*t,dyn)
        ax.set_xlim(shift(lo0,-180),shift(lo1,-180)); ax.set_ylim(la0,la1)
        w.append_data(grab(fig))
    w.close(); plt.close(fig); print("  done MAP2")

def shot3():
    print("shot3 taiwan"); N=int(6*FPS); west=-180; fig,ax=new_fig(); build_basemap(ax,west); dyn=[]
    TAI=(121.15,22.8); dests=[(121.7,17.6),(114.0,0.5),(110.0,-7.5),(125.0,1.5)]
    arcs=[great_circle(TAI,d,120) for d in dests]; w=writer("MAP3_taiwan_routes.mp4")
    ax.set_xlim(shift(103,west),shift(133,west)); ax.set_ylim(-12,30)
    for i in range(N):
        t=i/(N-1); clear(dyn)
        for j,(lon,lat) in enumerate(arcs):
            prog=np.clip((t-0.12*j)/0.55,0,1); k=max(2,int(prog*len(lon)))
            if k>=2:
                x=shift(lon[:k],west); glow_line(ax,x,lat[:k],dyn)
                dyn.append(ax.scatter([x[-1]],[lat[k-1]],s=45,c=GOLD,zorder=6,edgecolors="none"))
        marker(ax,TAI[0],TAI[1],west,(i/FPS)%1.0,1.0,dyn)
        w.append_data(grab(fig))
    w.close(); plt.close(fig); print("  done MAP3")

def shot4():
    print("shot4 spread"); N=int(7*FPS); west=-30; fig,ax=new_fig(); build_basemap(ax,west); dyn=[]
    ISEA=(120.0,-2.0); dests=[(46.9,-18.9),(178.0,-17.7),(-172.0,-13.8),(-109.37,-27.12),(-155.5,19.6),(175.0,-39.0)]
    arcs=[great_circle(ISEA,d,160) for d in dests]; w=writer("MAP4_ocean_spread.mp4")
    ax.set_xlim(5,300); ax.set_ylim(-55,45)
    for i in range(N):
        t=i/(N-1); clear(dyn)
        for j,(lon,lat) in enumerate(arcs):
            prog=np.clip((t-0.08*j)/0.6,0,1); k=max(2,int(prog*len(lon)))
            if k>=2:
                x=shift(lon[:k],west)
                for sx,sy in split_seam(x,lat[:k]): glow_line(ax,sx,sy,dyn,0.9)
                xe=float(shift(lon[k-1],west)); dyn.append(ax.scatter([xe],[lat[k-1]],s=40,c=GOLD,zorder=6,edgecolors="none"))
        marker(ax,ISEA[0],ISEA[1],west,(i/FPS)%1.0,0.8,dyn)
        w.append_data(grab(fig))
    w.close(); plt.close(fig); print("  done MAP4")

def shot5():
    print("shot5 peoples"); N=int(6*FPS); west=-180; fig,ax=new_fig(); build_basemap(ax,west); dyn=[]
    seq=[["Malaysia","Brunei"],["Indonesia"],["Philippines"]]; w=writer("MAP5_maritime_peoples.mp4")
    ax.set_xlim(shift(94,west),shift(132,west)); ax.set_ylim(-11,20)
    for i in range(N):
        t=i/(N-1); clear(dyn)
        for j,names in enumerate(seq):
            a=np.clip((t-(0.18+0.22*j))/0.3,0,1)
            if a>0:
                country_fill(ax,names,west,AMBER,0.55*ease(a),3,dyn)
                country_fill(ax,names,west,GOLD,0.22*ease(a),4,dyn)
        w.append_data(grab(fig))
    w.close(); plt.close(fig); print("  done MAP5")

def shot6():
    print("shot6 khmer"); N=int(6*FPS); west=-180; fig,ax=new_fig(); build_basemap(ax,west); dyn=[]
    ANG=(103.867,13.412); terr=["Cambodia","Thailand","Laos"]; w=writer("MAP6_khmer_empire.mp4")
    ax.set_xlim(shift(94,west),shift(114,west)); ax.set_ylim(4,24)
    for i in range(N):
        t=i/(N-1); clear(dyn); a=ease(np.clip(t/0.7,0,1))
        country_fill(ax,terr,west,AMBER,0.5*a,3,dyn)
        country_fill(ax,["Cambodia"],west,GOLD,0.35*a,4,dyn)
        if t>0.25: marker(ax,ANG[0],ANG[1],west,(i/FPS)%1.0,1.0,dyn)
        w.append_data(grab(fig))
    w.close(); plt.close(fig); print("  done MAP6")

if __name__=="__main__":
    fns={"1":shot1,"2":shot2,"3":shot3,"4":shot4,"5":shot5,"6":shot6}
    which=sys.argv[1] if len(sys.argv)>1 else "all"
    for k in ("123456" if which=="all" else which): fns[k]()
    print("ALL DONE")
