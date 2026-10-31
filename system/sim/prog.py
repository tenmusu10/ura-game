import json, random, math, itertools
from collections import Counter
CH=json.load(open('res_chars.json'))
GROUPS={'赤':['料理好き','食いしん坊','甘党'],'青':['頑固','心配性','力持ち'],'緑':['世話好き','お人よし','おしゃべり'],
        '黄':['夜ふかし','せっかち','きまぐれ'],'白':['物知り','集め好き','きちょうめん'],'紫':['ひねくれ','さみしがり','なまけもの']}
K2G={k:g for g,ks in GROUPS.items() for k in ks}
ALLK=list(K2G)
STAT={'赤':'atk','青':'df','緑':'hp','黄':'spd'}
STAR={1:.85,2:.92,3:1.0,4:1.08,5:1.18,6:1.30}
HERO=dict(n=0,name='主人公',kosei='?',grp='?',slots=4,origin='団地育ち',star=3)  # wildcard
# chapter model: (name, side, wall303, Lv, max star in pool, exclude)
CHAP=[('1章',2,False,10,2),('2章',3,True,18,3),('3章',4,True,25,4),('4章',4,True,32,5),('5章',5,True,40,6),('終章',5,False,45,6)]
def nslots(r,lv): 
    open_=1+(lv>=10)+(lv>=25)+(lv>=40); return min(r['slots'],open_)
def lines(n,wall):
    L=[[(i,j) for j in range(n)] for i in range(n)]+[[(i,j) for i in range(n)] for j in range(n)]
    L+=[[(i,i) for i in range(n)],[(i,n-1-i) for i in range(n)]]
    w=(2,2) if wall and n>=3 else None
    return [l for l in L if w not in l], w
def roll(r,lv,R):
    ks={r['kosei']}
    for _ in range(nslots(r,lv)-1):
        while True:
            if R.random()<.7:
                k=R.choice([x for x in GROUPS[r['grp']] if x!=r['kosei']])
            else:
                k=R.choice([x for x in ALLK if K2G[x]!=r['grp']])
            if k not in ks: ks.add(k);break
            if len(ks)>=3 and R.random()<.5: break
    return ks
def board_bonus(assign,ks,n,wall,origin):
    L,w=lines(n,wall)
    b=Counter(); rl=None
    for l in L:
        sets=[ks[assign[c]] for c in l]
        best=None
        for g,st in STAT.items():
            for k in GROUPS[g]:
                if all(s=='*' or k in s for s in sets): best=max(best or (0,''),(10,st))
            if all(s=='*' or any(K2G[x]==g for x in s) for s in sets): best=max(best or (0,''),(5,st))
        if best: b[best[1]]+=best[0]
    # renkei: all rooms share group
    cells=[c for c in assign]
    for g in STAT:
        if all(ks[assign[c]]=='*' or any(K2G[x]==g for x in ks[assign[c]]) for c in cells):
            sup=any(all(ks[assign[c]]=='*' or k in ks[assign[c]] for c in cells) for k in GROUPS[g])
            rl=(g,sup)
    # jimoto: pairs +2, lines +6 (all stats)
    j=0
    for (i,jj) in cells:
        for d in [(1,0),(0,1)]:
            c2=(i+d[0],jj+d[1])
            if c2 in assign and origin[assign[(i,jj)]]==origin[assign[c2]]: j+=2
    for l in L:
        if len({origin[assign[c]] for c in l})==1: j+=6
    b['all']+=j
    return b,rl
W={'atk':1.0,'spd':.8,'hp':.5,'df':.15,'all':2.2}
RLV={'赤':40,'青':60,'緑':45,'黄':50}
def score(b,rl):
    s=sum(min(v,100)*W[k] for k,v in b.items())
    if rl: s+=RLV[rl[0]]*(2 if rl[1] else 1)
    return s
def optimize(pool,ks,origin,n,wall,R,free=False,lv=40,iters=6000):
    cells=[(i,j) for i in range(n) for j in range(n) if not(wall and n>=3 and (i,j)==(2,2))]
    ids=[r['n'] for r in pool]
    R.shuffle(ids)
    assign={c:ids[k] for k,c in enumerate(cells)}
    bench=ids[len(cells):]
    ks=dict(ks)
    def cur(): return score(*board_bonus(assign,ks,n,wall,origin))
    s=cur(); T=20.0
    byid={r['n']:r for r in pool}
    for it in range(iters):
        T=20*(1-it/iters)+0.1
        mv=R.random()
        if mv<.45:
            a,b2=R.sample(cells,2); assign[a],assign[b2]=assign[b2],assign[a]; undo=lambda:(assign.__setitem__(a,assign[b2]),assign.__setitem__(b2,assign[a])) 
            ns=cur()
            if ns<s and R.random()>math.exp((ns-s)/T): assign[a],assign[b2]=assign[b2],assign[a]
            else: s=ns
        elif mv<.75 and bench:
            a=R.choice(cells); bi=R.randrange(len(bench))
            assign[a],bench[bi]=bench[bi],assign[a]
            ns=cur()
            if ns<s and R.random()>math.exp((ns-s)/T): assign[a],bench[bi]=bench[bi],assign[a]
            else: s=ns
        elif free:
            a=R.choice(cells); rid=assign[a]
            if ks[rid]=='*': continue
            r=byid[rid]; k=nslots(r,lv)
            if k<2: continue
            old=ks[rid]; new=set(old); new.discard(R.choice([x for x in old if x!=r['kosei']]))
            new.add(R.choice([x for x in ALLK if x not in new])); ks[rid]=new
            ns=cur()
            if ns<s and R.random()>math.exp((ns-s)/T): ks[rid]=old
            else: s=ns
    b,rl=board_bonus(assign,ks,n,wall,origin)
    return b,rl,assign,ks
def sortie(n,wall,mode):
    # ひとすじ + おとなり for best/typical sortie of n members
    if n<2: return 0
    hito={2:5,3:12,4:22,5:35}[n]
    if mode=='random': return 0
    return hito+3*(n-1)  # straight row incl. hero (hero movable)
def run(mode,seed=0):
    R=random.Random(seed); out=[]
    for name,n,wall,lv,maxstar in CHAP:
        pool=[r for r in CH if r['star']<=maxstar and not(name!='終章' and r['name']=='ミオ')]+[HERO]
        origin={r['n']:r['origin'] for r in pool}
        ks={}
        for r in pool:
            if r['n']==0: ks[0]='*'
            elif mode=='やりこみ': ks[r['n']]=set([r['kosei']]+R.sample([x for x in GROUPS[r['grp']] if x!=r['kosei']],min(2,nslots(r,lv)-1))+([R.choice(ALLK)] if nslots(r,lv)==4 else []))
            else: ks[r['n']]=roll(r,lv,R)
        if mode=='おまかせ':
            cells=[(i,j) for i in range(n) for j in range(n) if not(wall and n>=3 and (i,j)==(2,2))]
            ids=[r['n'] for r in pool]; R.shuffle(ids); assign={c:ids[k] for k,c in enumerate(cells)}
            b,rl=board_bonus(assign,ks,n,wall,origin); so=sortie(n,wall,'random')
        else:
            b,rl,assign,_=optimize(pool,ks,origin,n,wall,R,free=(mode=='やりこみ'),lv=lv)
            so=sortie(n,wall,'line')
        b['all']+=so
        # origin-floor match: assume half the party matches for planned players
        if mode!='おまかせ': b['all']+=15*0.6
        stars=sorted([STAR[r['star']] for r in pool if r['n']],reverse=True)[:n-1]+[1.0]
        out.append(dict(ch=name,n=n,lv=lv,b=dict(b),rl=rl,star=sum(stars)/n if mode!='おまかせ' else sum(STAR[r['star']] for r in pool if r['n'])/(len(pool)-1)))
    return out
if __name__=='__main__':
    res={}
    for mode in ['おまかせ','ふつう','やりこみ']:
        res[mode]=[run(mode,s) for s in range(3)]
        for c in res[mode][0]: print(mode,c)
    json.dump(res,open('res_prog.json','w'),ensure_ascii=False,default=list)
