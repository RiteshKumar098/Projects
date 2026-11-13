#!/usr/bin/env python3
"""Score YouTube hooks with a heuristic panel; not a performance predictor."""
import json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
FORMULAS = json.load(open(os.path.join(HERE, "hooks.json")))["hooks"]
FILLER = {"basically","actually","literally","just","really","very","so","kind","sort","like","guys","hey","welcome","today","video","subscribe","channel"}
VAGUE = {"amazing","incredible","insane","crazy","huge","massive","game","changer","secret","powerful","ultimate","best","revolutionary","mind","blowing","unbelievable"}
CONCRETE = re.compile(r"\b(\d[\d,.]*\s?(%|k|m|x|s|m|h)?|\$\d|\d+\s?(second|minute|hour|day|week|month|year)s?)\b", re.I)
YOU = re.compile(r"\b(you|your|you're|youre|yourself)\b", re.I)
STAKE = re.compile(r"\b(lose|lost|wasting|waste|quit|fail|broke|cost|risk|before|stop|never|die|dying|dead)\b", re.I)
CURIOSITY = re.compile(r"\b(why|how|what|which|until|before|but|nobody|almost|except|reason|actually)\b", re.I)
def words(t): return re.findall(r"[a-z0-9'%$.]+", t.lower())
def specificity(t):
    w=words(t)
    if not w:return 0
    nums=len(CONCRETE.findall(t)); vague=sum(x in VAGUE for x in w); filler=sum(x in FILLER for x in w)
    s=34+nums*22-vague*16-filler*5; s+=min(18,6*sum(x[:1].isupper() for x in t.split()[1:]))
    return max(0,min(100,s))
def address(t):
    n=len(YOU.findall(t)); first=30 if YOU.search(" ".join(t.split()[:6])) else 0
    return max(0,min(100,26+n*20+first))
def stakes(t):
    n=len(STAKE.findall(t)); return max(0,min(100,22+n*26+(14 if CONCRETE.search(t) else 0)))
def curiosity(t):
    n=len(CURIOSITY.findall(t)); q=18 if t.strip().endswith("?") else 0
    closed=-18 if re.search(r"\b(because|so that|which means)\b",t,re.I) else 0
    return max(0,min(100,24+n*17+q+closed))
def brevity(t):
    n=len(words(t))
    if n==0:return 0
    if 9<=n<=24:return 100
    if n<9:return max(30,100-(9-n)*11)
    return max(10,100-(n-24)*7)
PROPS=[("SPECIFICITY",specificity),("ADDRESS",address),("STAKES",stakes),("CURIOSITY",curiosity),("BREVITY",brevity)]
def classify(t):
    best,hits=None,0
    for f in FORMULAS:
        n=sum(1 for p in f["match"] if re.search(p,t,re.I))
        if n>hits:best,hits=f,n
    return (best["name"] if best else "Unclassified"),hits
def score(t):
    parts={n:fn(t) for n,fn in PROPS}; vals=list(parts.values()); verdict=round(.6*(sum(vals)/len(vals))+.4*min(vals)); name,hits=classify(t)
    return parts,verdict,name,hits
def band(v): return "STRONG" if v>=72 else "WORKABLE" if v>=55 else "WEAK"
FIX={"SPECIFICITY":"swap one adjective for a number, a name or a date","ADDRESS":"say 'you' in the first six words","STAKES":"name what it costs them to keep doing it the current way","CURIOSITY":"cut the half of the sentence that answers itself","BREVITY":"9 to 24 words. Read it out loud and stop where you run out of breath"}
def report(t,parts,verdict,name,hits):
    print(f"\n  {t.strip()}\n  {'-'*min(72,max(20,len(t.strip())))}")
    for k,v in parts.items():print(f"    {k:<12} {v:3d}  {'#'*(v//5)}")
    print(f"    {'VERDICT':<12} {verdict:3d}  {band(verdict)}")
    print(f"    formula      {name}"+(f"  ({hits} patterns matched)" if hits else "  (no formula matched - usually a summary, not a hook)"))
    low=min(parts,key=parts.get); print(f"    weakest      {low} - {FIX[low]}")
def main():
    a=sys.argv[1:]; as_json="--json" in a; a=[x for x in a if x!="--json"]
    if "--hook" in a:lines=[a[a.index("--hook")+1]]
    elif a and os.path.exists(a[0]):lines=[l for l in open(a[0]).read().splitlines() if l.strip()]
    else:print(__doc__); sys.exit(1 if not a else 0)
    out=[]
    for t in lines:
        parts,verdict,name,hits=score(t); out.append({"hook":t.strip(),"properties":parts,"verdict":verdict,"band":band(verdict),"formula":name,"matched":hits})
    out.sort(key=lambda r:-r["verdict"])
    if as_json:print(json.dumps([{k:v for k,v in r.items() if k!="matched"} for r in out],indent=1));return
    for r in out:report(r["hook"],r["properties"],r["verdict"],r["formula"],r["matched"])
    if len(out)>1:print(f"\n  winner: {out[0]['hook'].strip()}  ({out[0]['verdict']}, {out[0]['band']})\n")
if __name__=="__main__":main()
