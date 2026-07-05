#!/usr/bin/env python3
"""Build a pixel-perfect YouTube thumbnail (1280x720) in code.
Map background (accurate geodata) + crisp PIL text. Two headline variants."""
import json, math, os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch
from matplotlib.collections import LineCollection
from PIL import Image, ImageDraw, ImageFont, ImageFilter

HERE=os.path.dirname(os.path.abspath(__file__))
W,H=1280,720
OCEAN="#0B2026"; LAND="#4E3F2C"; COAST="#213338"; GRAT="#123037"; AMBER="#E8AC52"; GOLD="#F6D48C"
FONT_BOLD="/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"

with open(os.path.join(HERE,"ne_50m.geojson")) as f: GJ=json.load(f)
def rings_of(g):
    t,c=g["type"],g["coordinates"]
    if t=="Polygon": return [np.asarray(r,float) for r in c]
    if t=="MultiPolygon": return [np.asarray(r,float) for poly in c for r in poly]
    return []
def decim(r): return np.vstack([r[::2],r[-1]]) if len(r)>60 else r
ALL=[decim(r) for feat in GJ["features"] for r in rings_of(feat["geometry"])]
def shift(lon,west): return (np.asarray(lon,float)-west)%360.0
def seam(x,y):
    x=np.asarray(x);y=np.asarray(y)
    if len(x)<2: return [(x,y)]
    b=np.where(np.abs(np.diff(x))>180)[0]
    if len(b)==0: return [(x,y)]
    segs=[];s=0
    for k in b: segs.append((x[s:k+1],y[s:k+1]));s=k+1
    segs.append((x[s:],y[s:]))
    return [(a,c) for a,c in segs if len(a)>=2]
def gc(p1,p2,n=160):
    lo1,la1=map(math.radians,p1);lo2,la2=map(math.radians,p2)
    v1=np.array([math.cos(la1)*math.cos(lo1),math.cos(la1)*math.sin(lo1),math.sin(la1)])
    v2=np.array([math.cos(la2)*math.cos(lo2),math.cos(la2)*math.sin(lo2),math.sin(la2)])
    om=math.acos(np.clip(np.dot(v1,v2),-1,1));t=np.linspace(0,1,n)
    pts=(np.outer(np.ones(n),v1) if om<1e-6 else (np.sin((1-t)*om)[:,None]*v1+np.sin(t*om)[:,None]*v2)/math.sin(om))
    return np.degrees(np.arctan2(pts[:,1],pts[:,0])),np.degrees(np.arcsin(np.clip(pts[:,2],-1,1)))

def render_map():
    west=-30
    fig=plt.figure(figsize=(W/100,H/100),dpi=100); fig.patch.set_facecolor(OCEAN)
    ax=fig.add_axes([0,0,1,1]); ax.set_axis_off(); ax.set_facecolor(OCEAN)
    verts,codes,lines=[],[],[]
    for ring in ALL:
        x=shift(ring[:,0],west);y=ring[:,1]
        for sx,sy in seam(x,y):
            if len(sx)>=3:
                verts.append((sx[0],sy[0]));codes.append(Path.MOVETO)
                for k in range(1,len(sx)): verts.append((sx[k],sy[k]));codes.append(Path.LINETO)
                verts.append((sx[0],sy[0]));codes.append(Path.CLOSEPOLY)
            lines.append(np.column_stack([sx,sy]))
    ax.add_patch(PathPatch(Path(verts,codes),fc=LAND,ec="none",zorder=1))
    ax.add_collection(LineCollection(lines,colors=COAST,linewidths=0.5,zorder=2))
    g=[]
    for lon in range(-180,181,15):
        for sx,sy in seam(shift(np.full(91,lon),west),np.linspace(-90,90,91)): g.append(np.column_stack([sx,sy]))
    for lat in range(-75,76,15):
        for sx,sy in seam(shift(np.linspace(-180,180,181),west),np.full(181,lat)): g.append(np.column_stack([sx,sy]))
    ax.add_collection(LineCollection(g,colors=GRAT,linewidths=0.4,zorder=0))
    ISEA=(120.0,-2.0)
    for d in [(46.9,-18.9),(178.0,-17.7),(-172.0,-13.8),(-109.37,-27.12),(-155.5,19.6),(175.0,-39.0)]:
        lon,lat=gc(ISEA,d); x=shift(lon,west)
        for sx,sy in seam(x,lat):
            ax.plot(sx,sy,color=AMBER,lw=6,alpha=0.16,zorder=4,solid_capstyle="round")
            ax.plot(sx,sy,color=GOLD,lw=2.2,alpha=0.95,zorder=5,solid_capstyle="round")
        xe=float(shift(d[0],west)); ax.scatter([xe],[d[1]],s=32,c=GOLD,zorder=6,edgecolors="none")
    xo=float(shift(ISEA[0],west))
    ax.scatter([xo],[ISEA[1]],s=90,c=GOLD,zorder=7,edgecolors="none")
    ax.scatter([xo],[ISEA[1]],s=900,facecolors="none",edgecolors=AMBER,linewidths=2,alpha=0.7,zorder=6)
    ax.set_xlim(60,300); ax.set_ylim(-52,40)
    fig.canvas.draw()
    img=np.asarray(fig.canvas.buffer_rgba())[:,:,:3].copy(); plt.close(fig)
    return Image.fromarray(img)

def left_scrim(img):
    """Darken the left ~55% with a horizontal gradient for text legibility."""
    grad=Image.new("L",(W,H),0); d=ImageDraw.Draw(grad)
    for x in range(W):
        a=int(235*max(0.0,(1-(x/(W*0.58)))))**1
        a=min(235,max(0,int(235*(1-(x/(W*0.60)))))) if x< W*0.60 else 0
        d.line([(x,0),(x,H)],fill=a)
    black=Image.new("RGB",(W,H),(6,14,17))
    return Image.composite(black,img,grad)

def fit_font(draw,text,maxw,start=120,minsz=40):
    s=start
    while s>minsz:
        f=ImageFont.truetype(FONT_BOLD,s)
        if draw.textlength(text,font=f)<=maxw: return f
        s-=2
    return ImageFont.truetype(FONT_BOLD,minsz)

def draw_text(img, eyebrow, lines, tag):
    d=ImageDraw.Draw(img)
    x=64; maxw=int(W*0.52)
    # eyebrow
    fe=ImageFont.truetype(FONT_BOLD,30)
    d.text((x,78),eyebrow,font=fe,fill=(232,172,82))
    d.line([(x,120),(x+d.textlength(eyebrow,font=fe),120)],fill=(232,172,82),width=3)
    # headline lines
    y=150
    fonts=[fit_font(d,ln,maxw) for ln in lines]
    for ln,f in zip(lines,fonts):
        # soft shadow for pop
        d.text((x+3,y+3),ln,font=f,fill=(0,0,0))
        d.text((x,y),ln,font=f,fill=(245,245,240))
        y+=f.size+6
    # channel tag bottom-left
    ft=ImageFont.truetype(FONT_BOLD,26)
    d.text((x,H-58),tag,font=ft,fill=(150,160,160))

def build(variant, eyebrow, lines, tag, outname):
    base=render_map()
    base=left_scrim(base)
    # subtle vignette
    v=Image.new("L",(W,H),0); dv=ImageDraw.Draw(v)
    dv.ellipse([-W*0.3,-H*0.3,W*1.3,H*1.3],fill=255)
    v=v.filter(ImageFilter.GaussianBlur(180))
    dark=Image.new("RGB",(W,H),(4,10,12))
    base=Image.composite(base,dark,v)
    draw_text(base,eyebrow,lines,tag)
    out=os.path.join(HERE,outname); base.save(out,quality=95)
    print("wrote",out)

if __name__=="__main__":
    build("B","THE AUSTRONESIAN EXPANSION",["WHO REALLY","SETTLED THE","PACIFIC?"],
          "THE TRUE ORIGIN OF SOUTHEAST ASIA","thumb_map_A.png")
    build("B2","SOUTHEAST ASIA",["STRANGER","THAN YOU","THINK"],
          "A DOCUMENTARY","thumb_map_B.png")
    print("done")
