"""カゲの種類を入れたうえで、1戦のHP減りが平均15%になるように階層ごとの強さを合わせる"""
import json
import kage as K
F=K.F; E=K.E
R4=json.load(open('res_final4.json'))
def loss(stage,scale,N=300,full=False):
    old=K.CHMAP[stage]; r=R4[old]; b,o=F.bon('ふつう',old)
    L=[];wipe=0
    for _ in range(N):
        P=F.party(list(r['party']),r['lv'],b); ok,_=K.fight(P,K.spawn(stage,r['km']*scale,r['lv']),o); wipe+=not ok
        L.append(1-sum(max(0,p.hp) for p in P)/sum(p.mhp for p in P))
    L.sort()
    if full: return sum(L)/N,wipe/N,L[int(N*.9)]
    return sum(L)/N,wipe/N
out={}
for st in K.FLOORS:
    s=F.bisect(lambda m:loss(st,m)[0],.15,lo=.6,hi=2.0,it=9,dec=False)
    m,w,p90=loss(st,s,N=600,full=True)
    old=K.CHMAP[st]; r=R4[old]; g=E.G(r['lv']); k=r['km']*s
    rows=[]
    for name,grp,weak,res,(h,a,d,sp),sk in K.FLOORS[st][1]+[K.FLOORS[st][2]]:
        rows.append(dict(name=name,grp=grp,weak=weak,resist=res,HP=round(30*k*g*h),攻撃=round(9*k*g*a),防御=round(10*k*g*d),素早さ=round(10*g*sp),skill=sk))
    out[st]=dict(scale=s,mean=m,wipe=w,p90=p90,lv=r['lv'],rows=rows)
    print(st,round(s,3),round(m,3),round(p90,3),w,flush=True)
json.dump(out,open('res_kage_tune.json','w'),ensure_ascii=False)
