#!/usr/bin/env python3
"""Rank collected videos by multiples of their own channel's median views."""
import json, os, re, statistics, sys
HERE=os.path.dirname(os.path.abspath(__file__))
FORMULAS=json.load(open(os.path.join(HERE,"..","yt-script","hooks.json")))["hooks"]
def classify(title):
    scored=[]
    for f in FORMULAS:
        n=sum(1 for p in f["match"] if re.search(p,title,re.I))
        if n:scored.append((n,f["name"]))
    scored.sort(reverse=True);return scored[0][1] if scored else "Unclassified"
def main():
    a=sys.argv[1:];as_json="--json" in a;a=[x for x in a if x!="--json"]
    lo=float(a[a.index("--min")+1]) if "--min" in a else 1.5
    files=[x for x in a if not x.startswith("--") and not re.match(r"^[\d.]+$",x)]
    if not files or not os.path.exists(files[0]):print(__doc__);sys.exit(1)
    rows=json.load(open(files[0]));rows=rows.get("videos",[]) if isinstance(rows,dict) else rows
    by={}
    for r in rows:by.setdefault(r.get("channel","?"),[]).append(r)
    out=[];thin=[]
    for ch,vids in by.items():
        views=[float(v.get("views",0) or 0) for v in vids];med=statistics.median(views) if views else 0
        if len(vids)<4:thin.append((ch,len(vids)));continue
        for v in vids:
            m=float(v.get("views",0) or 0)/med if med else 0
            out.append({"channel":ch,"title":v.get("title",""),"views":int(v.get("views",0) or 0),"median":int(med),"multiple":round(m,2),"formula":classify(v.get("title","")),"url":v.get("url","")})
    out=[r for r in out if r["multiple"]>=lo];out.sort(key=lambda r:-r["multiple"])
    if as_json:print(json.dumps({"outliers":out,"skipped_thin_channels":thin},indent=1));return
    print(f"\n  {len(rows)} videos across {len(by)} channels, outliers at {lo}x or better\n")
    for r in out[:25]:print(f"    {r['multiple']:5.2f}x  {r['views']:>9,}  vs {r['median']:>9,} median   {r['channel'][:22]:<22} {r['title'][:52]}\n            {r['formula']}")
    if not out:print("    nothing cleared the threshold - collect more per channel or lower --min")
    if thin:print(f"\n  skipped {len(thin)} channel(s) with under 4 videos collected - "+", ".join(f"{c} ({n})" for c,n in thin[:6]))
    counts={}
    for r in out:counts[r["formula"]]=counts.get(r["formula"],0)+1
    if counts:
        print("\n  formulas among the outliers")
        for f,n in sorted(counts.items(),key=lambda x:-x[1]):print(f"    {n:2d}x  {f}")
    print()
if __name__=="__main__":main()
