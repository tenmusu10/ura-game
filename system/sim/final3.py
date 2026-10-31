import engine as E, json, random
T=json.load(open('res_final2.json'))
CTXMIO={'mio':'one50'}
CHAPS=[('1章',10,2,['主人公','ユズコ']),('2章',18,3,['主人公','キナコ','チヨノ']),
 ('3章',25,4,['主人公','ミナト','ヒナコ','キナコ']),('4章',32,4,['主人公','トメヨ','トモシビ','ミナト']),
 ('5章',40,5,['主人公','トメヨ','トモシビ','カゲモリ','ミナト']),('終章',45,5,['主人公','トメヨ','トモシビ','ミオ','ミナト'])]
MAXSTAR={'1章':2,'2章':3,'3章':4,'4章':5,'5章':6,'終章':6}
RR=random.Random(5)
def bon(rule,mode,ch):
    t=T[f'{rule}|{mode}|{ch}']; o=dict(t['opt']); o.update(CTXMIO)
    if o.get('taken')==1.0: o.pop('taken')
    if 'first' in o: o['first']=round(o['first'])
    return t['out'],o
def wr(names_fn,lv,n,k,b,o,N=200,mob=False,blv=None):
    w=0;loss=0;blv=blv or lv
    for _ in range(N):
        P=E.mkparty(names_fn(),lv,b); ok,_=E.battle(P,E.mkmobs(k,blv) if mob else E.mkboss(n,k,blv),o); w+=ok
        loss+=1-sum(max(0,p.hp) for p in P)/sum(p.mhp for p in P)
    return w/N,loss/N
def kfor(names_fn,lv,n,b,o,target=.5,N=200):
    lo,hi=.2,6
    for _ in range(11):
        m=(lo*hi)**.5
        if wr(names_fn,lv,n,m,b,o,N)[0]>target: lo=m
        else: hi=m
    return (lo*hi)**.5
out={}
for ch,lv,n,party in CHAPS:
    pool=[c['name'] for c in E.CH if c['star']<=MAXSTAR[ch] and (c['name']!='ミオ' or ch=='終章')]
    rnd=lambda: ['主人公']+RR.sample(pool,n-1)
    fix=lambda: list(party)
    bf,of=bon('調整案2','ふつう',ch); bo,oo=bon('調整案2','おまかせ',ch); by,oy=bon('調整案2','やりこみ',ch)
    k50=kfor(fix,lv,n,bf,of); k=k50*0.9
    r={m:wr(fn,lv,n,k,b,o)[0] for m,(fn,b,o) in {'おまかせ':(rnd,bo,oo),'ふつう':(fix,bf,of),'やりこみ':(fix,by,oy)}.items()}
    # mob: 3体。ふつうパーティの1戦あたりのHP消耗
    km=k*0.85; mw,ml=wr(fix,lv,n,km,bf,of,mob=True)
    # おまかせで勝率50%に届くレベル
    need=None
    for add in range(0,61,3):
        if wr(rnd,lv+add,n,k,bo,oo,N=200,blv=lv)[0]>=.5: need=add;break
    ko=kfor(rnd,lv,n,bo,oo); g=E.G(lv)
    out[ch]=dict(lv=lv,n=n,party=party,k=k,boss=dict(HP=round(77*n*k*g),攻撃=round(20*k*g),防御=round(15*k*g),素早さ=round(15*g)),
                 mob=dict(HP=round(30*km*g),攻撃=round(9*km*g),防御=round(10*km*g),素早さ=round(10*g)),wr=r,mobloss=ml,mobwin=mw,omakase_need=need,ratio=k50/ko)
    print(ch,out[ch],flush=True)
json.dump(out,open('res_final3.json','w'),ensure_ascii=False)
