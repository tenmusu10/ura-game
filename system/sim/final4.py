"""ドラクエくらいの難易度で敵を逆算する（第3版）"""
import engine as E, learned as L, json, random
E.LEARNED_HOOK=L.try_learned
T=json.load(open('res_final2.json'))
CHAPS=[('1章',10,2,['主人公','ユズコ']),('2章',18,3,['主人公','キナコ','チヨノ']),
 ('3章',25,4,['主人公','ミナト','ヒナコ','キナコ']),('4章',32,4,['主人公','トメヨ','トモシビ','ミナト']),
 ('5章',40,5,['主人公','トメヨ','トモシビ','カゲモリ','ミナト']),('終章',45,5,['主人公','トメヨ','トモシビ','ミオ','ミナト'])]
MAXSTAR={'1章':2,'2章':3,'3章':4,'4章':5,'5章':6,'終章':6}
RR=random.Random(9)
TARGET_BOSS=.60; TARGET_MOBLOSS=.15; MOBS=4
def bon(mode,ch):
    t=T[f'調整案2|{mode}|{ch}']; o=dict(t['opt']); o['mio']='one50'
    if o.get('taken')==1.0: o.pop('taken')
    if 'first' in o: o['first']=round(o['first'])
    return t['out'],o
def party(names,lv,b):
    P=E.mkparty(names,lv,b)
    for p in P: L.learn(p,lv)
    return P
def boss_wr(fn,lv,n,k,b,o,N=200,blv=None):
    w=0;acts=0
    for _ in range(N):
        P=party(fn(),lv,b); ok,a=E.battle(P,E.mkboss(n,k,blv or lv),o); w+=ok; acts+=a
    return w/N, acts/N/(n+1)
def mob_loss(fn,lv,k,b,o,N=200):
    loss=0;w=0
    for _ in range(N):
        P=party(fn(),lv,b); ok,_=E.battle(P,E.mkmobs(k,lv,MOBS),o); w+=ok
        loss+=1-sum(max(0,p.hp) for p in P)/sum(p.mhp for p in P)
    return loss/N,w/N
def night(fn,lv,k,b,o,items,N=150):
    """回復なしで雑魚戦を続け、全員の平均HPが35%を切るか、だれか倒れたら帰る。items＝回復アイテム（1個で1人30%）"""
    tot=0
    for _ in range(N):
        P=party(fn(),lv,b); it=items; c=0
        while c<30:
            for p in P:   # 戦闘のあいだに回復アイテム
                if p.hp>0 and p.hp/p.mhp<.4 and it>0: p.hp+=p.mhp*.3; it-=1
            # わざの回数は1夜で共有（戻らない）
            hp0=[p.hp for p in P]
            ok,_=E.battle(P,E.mkmobs(k,lv,MOBS),o)
            if not ok: break
            c+=1
            if any(p.hp<=0 for p in P) or sum(max(0,p.hp) for p in P)/sum(p.mhp for p in P)<.35: break
        tot+=c
    return tot/N
def bisect(f,target,lo=.2,hi=8,it=11,dec=True):
    for _ in range(it):
        m=(lo*hi)**.5
        if (f(m)>target)==dec: lo=m
        else: hi=m
    return (lo*hi)**.5
out={}
for ch,lv,n,names in CHAPS:
    pool=[c['name'] for c in E.CH if c['star']<=MAXSTAR[ch] and (c['name']!='ミオ' or ch=='終章')]
    rnd=lambda: ['主人公']+RR.sample(pool,n-1); fix=lambda: list(names)
    bf,of=bon('ふつう',ch); bo,oo=bon('おまかせ',ch)
    kb=bisect(lambda m:boss_wr(fix,lv,n,m,bf,of)[0],TARGET_BOSS)
    w0,turns=boss_wr(fix,lv,n,kb,bf,of,N=300)
    wm3=boss_wr(fix,max(1,lv-3),n,kb,bf,of,blv=lv)[0]; wp3=boss_wr(fix,lv+3,n,kb,bf,of,blv=lv)[0]
    need=None
    for add in range(0,41,2):
        if boss_wr(rnd,lv+add,n,kb,bo,oo,N=150,blv=lv)[0]>=.5: need=add;break
    km=bisect(lambda m:mob_loss(fix,lv,m,bf,of)[0],TARGET_MOBLOSS,dec=False)
    ml,mw=mob_loss(fix,lv,km,bf,of,N=300)
    n0=night(fix,lv,km,bf,of,0); n5=night(fix,lv,km,bf,of,5)
    g=E.G(lv)
    out[ch]=dict(lv=lv,n=n,party=names,kb=kb,km=km,
        boss=dict(HP=round(77*n*kb*g),攻撃=round(20*kb*g),防御=round(15*kb*g),素早さ=round(15*g)),
        mob=dict(HP=round(30*km*g),攻撃=round(9*km*g),防御=round(10*km*g),素早さ=round(10*g)),
        boss_wr=w0,turns=turns,wr_m3=wm3,wr_p3=wp3,omakase_need=need,mobloss=ml,mobwin=mw,night0=n0,night5=n5)
    print(ch,out[ch],flush=True)
json.dump(out,open('res_final4.json','w'),ensure_ascii=False)
