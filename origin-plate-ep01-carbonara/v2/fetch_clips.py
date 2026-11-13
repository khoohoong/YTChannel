"""Locate + download finished v2 clips. CDN name = hf_<date>_<HHMMSS of submit>_<job>.mp4, so probe the submit window."""
import subprocess,datetime,concurrent.futures as cf,os,time,sys
rows=[l.split() for l in open('clip_jobs.tsv')]
ids={l.split('\t')[0]:l.split('\t')[1] for l in open('still_jobs.tsv')}
base="https://d8j0ntlcm91z4.cloudfront.net/user_30b7CTGiTTJpfv3eHgP4QQtBJ1y/hf_20261113_%s_%s.mp4"
import os as _o
_h,_m,_s,_n=[int(x) for x in _o.environ.get('WIN','6,48,50,260').split(',')]
W=[(datetime.datetime(2026,11,13,_h,_m,_s)+datetime.timedelta(seconds=k)).strftime('%H%M%S') for k in range(_n)]
found={}
if os.path.exists('clip_urls.tsv'):
    for l in open('clip_urls.tsv'):
        a=l.rstrip('\n').split('\t'); found[a[3]]=a[2]
def probe(a):
    t,j=a
    r=subprocess.run(['curl','-s','-o','/dev/null','-I','-m','10','-w','%{http_code}',base%(t,j)],capture_output=True,text=True).stdout
    return (j,base%(t,j)) if r=='200' else None
for rnd in range(int(sys.argv[1]) if len(sys.argv)>1 else 1):
    todo=[j for i,j in rows if j not in found]
    if not todo: break
    with cf.ThreadPoolExecutor(64) as ex:
        for r in ex.map(probe,[(t,j) for j in todo for t in W]):
            if r: found[r[0]]=r[1]
    with open('clip_urls.tsv','w') as f:
        for i,j in rows:
            if j in found: f.write(f"{i}\t{ids[i]}\t{found[j]}\t{j}\n")
    print('round',rnd,'found',len(found),'of',len(rows),flush=True)
    if len(found)<len(rows): time.sleep(40)
for i,j in rows:
    if j in found:
        dst=f"clips/{int(i):03d}_{ids[i]}.mp4"
        if not os.path.exists(dst): subprocess.run(['curl','-sSfL','--retry','3','-o',dst,found[j]])
print('downloaded',len(os.listdir('clips')),'missing',[i for i,j in rows if j not in found])
