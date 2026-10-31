import json, random, math
from collections import Counter
from prog import CH,GROUPS,K2G,ALLK,STAR,HERO,CHAP,nslots,lines,roll
STAT={'赤':'atk','青':'df','緑':'hp','黄':'spd'}
OLD=dict(name='いまのルール',big=10,small=5,blue='df',green_mult=1,hero_kosei=True,jimoto='global',
         hito={2:5,3:12,4:22,5:35},pair=3,floor=15,renkei_scale=False,super_mult=2,cap_all=100,cap_stat=100)
NEW=dict(name='調整案',big=12,small=6,blue='taken',green_mult=1.5,hero_kosei=False,jimoto='member',
         hito={2:3,3:6,4:10,5:15},pair=2,floor=10,renkei_scale=True,super_mult=1.5,cap_all=40,cap_stat=80,len_scale=True)
RENKEI={'赤':('atk',40),'青':('taken',35),'緑':('regen',8),'黄':('first',1)}
def evaluate(assign,ks,n,wall,origin,R_):
    L,w=lines(n,wall); b=Counter(); taken=0.0
    def has_k(s,k,hero_ok): return (s=='*' and hero_ok) or (s!='*' and k in s)
    def has_g(s,g): return s=='*' or any(K2G[x]==g for x in s)
    for l in L:
        sets=[ks[assign[c]] for c in l]; best=None
        for g,st in STAT.items():
            v=None
            ls=len(l)/5 if R_.get('len_scale') else 1
            if any(all(has_k(s,k,R_['hero_kosei']) for s in sets) for k in GROUPS[g]): v=R_['big']*ls
            elif all(has_g(s,g) for s in sets): v=R_['small']*ls
            if v:
                if g=='青' and R_['blue']=='taken': key,val='taken',v*0.4
                elif g=='緑': key,val='hp',v*R_['green_mult']
                else: key,val=st,v
                if not best or val>best[1]: best=(key,val)
        if best:
            if best[0]=='taken': taken+=best[1]
            else: b[best[0]]+=best[1]
    cells=list(assign); opt={}
    rooms=len(cells); scale=rooms/24 if R_['renkei_scale'] else 1
    for g,(key,v) in RENKEI.items():
        if all(has_g(ks[assign[c]],g) for c in cells):
            sup=any(all(has_k(ks[assign[c]],k,R_['hero_kosei']) for c in cells) for k in GROUPS[g])
            m=(R_['super_mult'] if sup else 1)*scale
            if key=='atk': b['atk']+=v*m
            elif key=='taken': taken+=v*m
            elif key=='regen': opt['regen']=v*m/100
            elif key=='first': opt['first']=1+round((2 if sup else 1)*scale) if scale>=0.5 else 0
    # sortie: best line containing hero position is free (hero movable) -> choose line maximizing jimoto
    sl=max(L,key=lambda l:len(l)) if L else []
    def nb(c):
        i,j=c; return [x for x in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)] if x in assign]
    if R_['jimoto']=='global':
        j=sum(2 for c in cells for d in [(1,0),(0,1)] if (c[0]+d[0],c[1]+d[1]) in assign and origin[assign[c]]==origin[assign[(c[0]+d[0],c[1]+d[1])]])
        j+=sum(6 for l in L if len({origin[assign[c]] for c in l})==1)
        best_line=max(L,key=lambda l:0)
    else:
        def mem(l): return sum(min(12,3*sum(origin[assign[x]]==origin[assign[c]] for x in nb(c))) for c in l)/len(l)
        best_line=max(L,key=mem); j=mem(best_line)
    b['all']+=j
    b['all']+=R_['hito'][n]+R_['pair']*(n-1)
    b['all']+=R_['floor']*0.6
    # caps
    out={}
    allv=min(b['all'],R_['cap_all'])
    for k in ['atk','df','hp','spd']:
        out[k]=min(b[k]+allv,R_['cap_stat'] if R_['cap_all']<100 else 100)
    if R_['blue']=='taken': opt['taken']=max(0.3,1-min(taken,60)/100)
    return out,opt,b
def score(out,opt):
    s=out['atk']*1.0+out['spd']*.6+out['hp']*.6+out['df']*.2
    s+= (1-opt.get('taken',1))*120 + opt.get('regen',0)*300 + opt.get('first',0)*10
    return s
def place(pool,ks,origin,n,wall,R,R_,free,lv,iters=5000,random_only=False):
    cells=[(i,j) for i in range(n) for j in range(n) if not(wall and n>=3 and (i,j)==(2,2))]
    ids=[r['n'] for r in pool]; R.shuffle(ids)
    assign={c:ids[k] for k,c in enumerate(cells)}; bench=ids[len(cells):]; ks=dict(ks)
    byid={r['n']:r for r in pool}
    f=lambda:score(*evaluate(assign,ks,n,wall,origin,R_)[:2])
    if random_only: return evaluate(assign,ks,n,wall,origin,R_)
    s=f()
    for it in range(iters):
        T=15*(1-it/iters)+.05; mv=R.random()
        if mv<.45:
            a,c=R.sample(cells,2); assign[a],assign[c]=assign[c],assign[a]; ns=f()
            if ns<s and R.random()>math.exp((ns-s)/T): assign[a],assign[c]=assign[c],assign[a]
            else: s=ns
        elif mv<.75 and bench:
            a=R.choice(cells); i=R.randrange(len(bench)); assign[a],bench[i]=bench[i],assign[a]; ns=f()
            if ns<s and R.random()>math.exp((ns-s)/T): assign[a],bench[i]=bench[i],assign[a]
            else: s=ns
        elif free:
            a=R.choice(cells); rid=assign[a]
            if ks[rid]=='*': continue
            r=byid[rid]
            if nslots(r,lv)<2: continue
            old=ks[rid]; new=set(old); new.discard(R.choice([x for x in old if x!=r['kosei']]))
            new.add(R.choice([x for x in ALLK if x not in new])); ks[rid]=new; ns=f()
            if ns<s and R.random()>math.exp((ns-s)/T): ks[rid]=old
            else: s=ns
    return evaluate(assign,ks,n,wall,origin,R_)
def run(R_,mode,seed):
    R=random.Random(seed); res=[]
    for name,n,wall,lv,maxstar in CHAP:
        pool=[r for r in CH if r['star']<=maxstar and not(name!='終章' and r['name']=='ミオ')]+[HERO]
        origin={r['n']:r['origin'] for r in pool}
        ks={r['n']:('*' if r['n']==0 else roll(r,lv,R)) for r in pool}
        out,opt,raw=place(pool,ks,origin,n,wall,R,R_,free=(mode=='やりこみ'),lv=lv,random_only=(mode=='おまかせ'))
        if mode=='おまかせ':  # random sortie: no line, no floor plan
            sub=R_['hito'][n]+R_['pair']*(n-1)+R_['floor']*0.6
            for k in out: out[k]=max(0,out[k]-sub)
        star=(sum(sorted([STAR[r['star']] for r in pool if r['n']],reverse=True)[:n-1])+1)/n
        if mode=='おまかせ': star=(sum(STAR[r['star']] for r in pool if r['n'])/(len(pool)-1)*(n-1)+1)/n
        res.append(dict(ch=name,n=n,lv=lv,out=out,opt=opt,star=star))
    return res
if __name__=='__main__':
    allres={}
    for R_ in [OLD,NEW]:
        for mode in ['おまかせ','ふつう','やりこみ']:
            allres[(R_['name'],mode)]=[run(R_,mode,s) for s in range(2)]
            print(R_['name'],mode,[ (c['ch'],c['out'],c['opt']) for c in allres[(R_['name'],mode)][0]],flush=True)
    json.dump({f'{a}|{b}':v for (a,b),v in allres.items()},open('res_rules.json','w'),ensure_ascii=False)
