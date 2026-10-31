import engine as E, json, time, sys
LV=40
def strength(names,bonus={},ctx={},N=200,it=10,lo=.3,hi=4.0,boss=True,noskill=False):
    for _ in range(it):
        m=(lo*hi)**.5; w=0
        for _ in range(N):
            P=E.mkparty(names,LV,bonus)
            if noskill:
                for p in P: p.skill=None
            w+=E.battle(P,E.mkboss(len(names),m,LV) if boss else E.mkmobs(m,LV),ctx)[0]
        if w/N>.5: lo=m
        else: hi=m
    return (lo*hi)**.5
if __name__=='__main__':
    t=time.time()
    base=strength(['主人公','_a','_b','_c','_d'])
    print('base',base,time.time()-t,flush=True)
    res={}
    for c in E.CH:
        n=c['name']
        s=strength(['主人公','_a','_b','_c',n]); s0=strength(['主人公','_a','_b','_c',n],noskill=True)
        res[n]=dict(star=c['star'],grp=c['grp'],total=s/base,stat_only=s0/base,skill=s/s0)
        print(n,c['star'],c['grp'],round(s/base,3),round(s0/base,3),flush=True)
    json.dump(dict(base=base,res=res),open('res_rank.json','w'),ensure_ascii=False)
