#!/usr/bin/env python3
"""Episode 2 (Srivijaya) map shots — same engine/palette as Episode 1's renderer.
Reads the shared Natural Earth geojson from the Ep1 maps folder. 1920x1080 MP4, no text
(labels go on in the edit). Shots:
  1 MAP1_strait_routes    (20s) trade routes converge on the Malacca Strait choke point
  2 MAP2_srivijaya_network(20s) the empire's port network lights up around Palembang
  3 MAP3_chola_strike     (15s) 1025: the Chola fleet vector crosses the Bay of Bengal
  4 MAP4_fall_majapahit   (15s) the network dims; Majapahit rises in Java; 1377 blow
"""
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
GEOJSON = os.path.join(HERE, "..", "..", "the-true-origin-of-southeast-asia", "maps", "ne_50m.geojson")
OUT = os.path.join(HERE, "map_clips"); os.makedirs(OUT, exist_ok=True)
W, H, DPI, FPS = 1920, 1080, 100, 24

OCEAN="#0E272E"; LAND="#5C4A33"; COAST="#243A40"; GRAT="#16323A"; AMBER="#E0A44E"; GOLD="#F4CE86"

with open(GEOJSON) as f:
    GJ = json.load(f)

def rings_of(g):
    t,c = g["type"], g["coordinates"]
    if t=="Polygon": return [np.asarray(r,float) for r in c]
    if t=="MultiPolygon": return [np.asarray(r,float) for poly in c for r in poly]
    return []

def decim(r):
    if len(r) > 60: return np.vstack([r[::2], r[-1]])
    return r

ALL_RINGS=[]
for feat in GJ["features"]:
    ALL_RINGS += [decim(r) for r in rings_of(feat["geometry"])]

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

def compound(rings, west):
    verts,codes=[],[]
    for ring in rings:
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

def great_circle(p1,p2,n=150):
    lon1,lat1=map(math.radians,p1); lon2,lat2=map(math.radians,p2)
    v1=np.array([math.cos(lat1)*math.cos(lon1),math.cos(lat1)*math.sin(lon1),math.sin(lat1)])
    v2=np.array([math.cos(lat2)*math.cos(lon2),math.cos(lat2)*math.sin(lon2),math.sin(lat2)])
    om=math.acos(np.clip(np.dot(v1,v2),-1,1)); t=np.linspace(0,1,n)
    pts=(np.outer(np.ones(n),v1) if om<1e-6 else
         (np.sin((1-t)*om)[:,None]*v1+np.sin(t*om)[:,None]*v2)/math.sin(om))
    return (np.degrees(np.arctan2(pts[:,1],pts[:,0])), np.degrees(np.arcsin(np.clip(pts[:,2],-1,1))))

def chain(points, n=110):
    """concatenate great-circle legs through waypoints"""
    lons,lats=[],[]
    for a,b in zip(points[:-1],points[1:]):
        lo,la=great_circle(a,b,n)
        lons.append(lo); lats.append(la)
    return np.concatenate(lons), np.concatenate(lats)

def ease(t): return t*t*(3-2*t)
def new_fig():
    fig=plt.figure(figsize=(W/DPI,H/DPI),dpi=DPI); fig.patch.set_facecolor(OCEAN)
    ax=fig.add_axes([0,0,1,1]); ax.set_axis_off(); return fig,ax
def grab(fig):
    fig.canvas.draw(); return np.asarray(fig.canvas.buffer_rgba())[:,:,:3].copy()

def marker(ax,lon,lat,west,phase,base,dyn,color_dot=GOLD,color_ring=AMBER,alpha=1.0):
    x=float(shift(lon,west))
    dyn.append(ax.scatter([x],[lat],s=70*base,c=color_dot,zorder=6,edgecolors="none",alpha=alpha))
    for k in range(3):
        p=(phase+k/3.0)%1.0
        dyn.append(ax.scatter([x],[lat],s=(70+p*2600)*base,facecolors="none",
                   edgecolors=color_ring,linewidths=2.2*(1-p),alpha=(1-p)*0.9*alpha,zorder=5))

def dot(ax,lon,lat,west,base,dyn,alpha=1.0):
    dyn.append(ax.scatter([float(shift(lon,west))],[lat],s=70*base,c=GOLD,zorder=6,
               edgecolors="none",alpha=alpha))

def glow_line(ax,x,y,dyn,wmul=1.0,alpha=1.0):
    dyn += ax.plot(x,y,color=AMBER,lw=7*wmul,alpha=0.18*alpha,zorder=4,solid_capstyle="round")
    dyn += ax.plot(x,y,color=GOLD,lw=2.4*wmul,alpha=0.95*alpha,zorder=5,solid_capstyle="round")

def clear(dyn):
    for a in dyn: a.remove()
    dyn.clear()

def writer(name):
    return imageio.get_writer(os.path.join(OUT,name), fps=FPS, codec="libx264",
        quality=8, macro_block_size=8, ffmpeg_params=["-pix_fmt","yuv420p"])

def lerp_view(v0,v1,t):
    return tuple(a+(b-a)*t for a,b in zip(v0,v1))

# key places
PALEMBANG=(104.75,-2.99); JAMBI=(103.61,-1.61); KEDAH=(100.37,6.12); CHAIYA=(99.18,9.38)
STRAIT=(102.2,1.9); SUNDA=(106.0,-5.9); NAGAPATTINAM=(79.84,10.77); TROWULAN=(112.35,-7.55)
GUANGZHOU=(113.3,22.1); COROMANDEL=(80.3,13.1); ARABIA=(58.5,14.5); CEYLON=(81.0,5.5)
VIET_OFFSHORE=(109.8,9.5)
NETWORK=[PALEMBANG,JAMBI,STRAIT,KEDAH,CHAIYA,SUNDA]

def shot1():  # MAP1 — trade routes converge on the strait (20s)
    print("MAP1 strait routes"); N=int(20*FPS); west=-180; fig,ax=new_fig(); build_basemap(ax,west); dyn=[]
    v0=(60,150,-22,36); v1=(86,124,-11,15)
    routes=[chain([GUANGZHOU,VIET_OFFSHORE,STRAIT]),
            chain([COROMANDEL,CEYLON,STRAIT]),
            chain([ARABIA,CEYLON,STRAIT])]
    w=writer("MAP1_strait_routes.mp4")
    for i in range(N):
        t=i/(N-1); clear(dyn)
        lo0,lo1,la0,la1=lerp_view(v0,v1,ease(min(1.0,t/0.85)))
        for j,(lon,lat) in enumerate(routes):
            prog=np.clip((t-0.10-0.12*j)/0.45,0,1); k=max(2,int(prog*len(lon)))
            if prog>0 and k>=2:
                x=shift(lon[:k],west)
                for sx,sy in split_seam(x,lat[:k]): glow_line(ax,sx,sy,dyn)
                dyn.append(ax.scatter([float(shift(lon[k-1],west))],[lat[k-1]],s=45,c=GOLD,zorder=6,edgecolors="none"))
        if t>0.55: marker(ax,STRAIT[0],STRAIT[1],west,(i/FPS)%1.0,0.9+0.4*ease((t-0.55)/0.45),dyn)
        ax.set_xlim(shift(lo0,west),shift(lo1,west)); ax.set_ylim(la0,la1)
        w.append_data(grab(fig))
    w.close(); plt.close(fig); print("  done MAP1")

def shot2():  # MAP2 — the Srivijaya network lights up (20s)
    print("MAP2 srivijaya network"); N=int(20*FPS); west=-180; fig,ax=new_fig(); build_basemap(ax,west); dyn=[]
    v0=(90,124,-10,13); v1=(94,118,-8,11)
    links=[chain([PALEMBANG,JAMBI]),chain([JAMBI,STRAIT]),chain([STRAIT,KEDAH]),
           chain([KEDAH,CHAIYA]),chain([PALEMBANG,SUNDA])]
    w=writer("MAP2_srivijaya_network.mp4")
    for i in range(N):
        t=i/(N-1); clear(dyn)
        lo0,lo1,la0,la1=lerp_view(v0,v1,ease(t))
        marker(ax,PALEMBANG[0],PALEMBANG[1],west,(i/FPS)%1.0,1.15,dyn)
        for j,(lon,lat) in enumerate(links):
            prog=np.clip((t-0.15-0.11*j)/0.30,0,1); k=max(2,int(prog*len(lon)))
            if prog>0 and k>=2:
                glow_line(ax,shift(lon[:k],west),lat[:k],dyn,0.9)
        for j,(plon,plat) in enumerate([JAMBI,STRAIT,KEDAH,CHAIYA,SUNDA]):
            a=np.clip((t-0.28-0.11*j)/0.18,0,1)
            if a>0: dot(ax,plon,plat,west,0.8*ease(a)+0.2,dyn,alpha=ease(a))
        ax.set_xlim(shift(lo0,west),shift(lo1,west)); ax.set_ylim(la0,la1)
        w.append_data(grab(fig))
    w.close(); plt.close(fig); print("  done MAP2")

def shot3():  # MAP3 — the Chola strike, 1025 (15s)
    print("MAP3 chola strike"); N=int(15*FPS); west=-180; fig,ax=new_fig(); build_basemap(ax,west); dyn=[]
    v0=(66,120,-12,24); v1=(72,116,-10,20)
    strike1=chain([NAGAPATTINAM,KEDAH]); strike2=chain([KEDAH,PALEMBANG])
    targets=[KEDAH,STRAIT,JAMBI,PALEMBANG]
    w=writer("MAP3_chola_strike.mp4")
    for i in range(N):
        t=i/(N-1); clear(dyn)
        lo0,lo1,la0,la1=lerp_view(v0,v1,ease(t))
        marker(ax,NAGAPATTINAM[0],NAGAPATTINAM[1],west,(i/FPS)%1.0,1.0,dyn)
        p1=np.clip((t-0.12)/0.34,0,1); k1=max(2,int(p1*len(strike1[0])))
        if p1>0: glow_line(ax,shift(strike1[0][:k1],west),strike1[1][:k1],dyn,1.5)
        p2=np.clip((t-0.50)/0.22,0,1); k2=max(2,int(p2*len(strike2[0])))
        if p2>0: glow_line(ax,shift(strike2[0][:k2],west),strike2[1][:k2],dyn,1.5)
        for j,(plon,plat) in enumerate(targets):
            hit=0.46+0.13*j
            if t>hit:
                ph=((t-hit)*3.0)%1.0
                marker(ax,plon,plat,west,ph,1.0,dyn)
        ax.set_xlim(shift(lo0,west),shift(lo1,west)); ax.set_ylim(la0,la1)
        w.append_data(grab(fig))
    w.close(); plt.close(fig); print("  done MAP3")

def shot4():  # MAP4 — the network dims; Majapahit rises; 1377 (15s)
    print("MAP4 fall + majapahit"); N=int(15*FPS); west=-180; fig,ax=new_fig(); build_basemap(ax,west); dyn=[]
    v0=(92,124,-11,12); v1=(94,122,-10,10)
    fading=[CHAIYA,KEDAH,STRAIT,SUNDA,JAMBI]
    blow=chain([TROWULAN,PALEMBANG])
    w=writer("MAP4_fall_majapahit.mp4")
    for i in range(N):
        t=i/(N-1); clear(dyn)
        lo0,lo1,la0,la1=lerp_view(v0,v1,ease(t))
        for j,(plon,plat) in enumerate(fading):
            a=1.0-np.clip((t-0.06-0.08*j)/0.16,0,1)
            if a>0: dot(ax,plon,plat,west,0.9,dyn,alpha=a)
        pal_a=1.0-0.85*np.clip((t-0.80)/0.20,0,1)   # Palembang dims at the end
        marker(ax,PALEMBANG[0],PALEMBANG[1],west,(i/FPS)%1.0,1.0,dyn,alpha=pal_a)
        mj=np.clip((t-0.38)/0.25,0,1)
        if mj>0: marker(ax,TROWULAN[0],TROWULAN[1],west,(i/FPS)%1.0,0.5+1.0*ease(mj),dyn)
        pb=np.clip((t-0.60)/0.22,0,1); kb=max(2,int(pb*len(blow[0])))
        if pb>0: glow_line(ax,shift(blow[0][:kb],west),blow[1][:kb],dyn,1.5)
        ax.set_xlim(shift(lo0,west),shift(lo1,west)); ax.set_ylim(la0,la1)
        w.append_data(grab(fig))
    w.close(); plt.close(fig); print("  done MAP4")

if __name__=="__main__":
    fns={"1":shot1,"2":shot2,"3":shot3,"4":shot4}
    which=sys.argv[1] if len(sys.argv)>1 else "all"
    for k in ("1234" if which=="all" else which): fns[k]()
    print("ALL DONE")
