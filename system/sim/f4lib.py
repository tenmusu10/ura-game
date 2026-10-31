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
