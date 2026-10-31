import random, statistics as st
R=random.Random(7)
class U:
    __slots__=('hp','mhp','atk','df','spd','side','t')
    def __init__(s,hp,atk,df,spd,side): s.hp=s.mhp=hp;s.atk=atk;s.df=df;s.spd=spd;s.side=side;s.t=0
def dmg(a,d): return a*a/(a+d)*2*R.uniform(.9,1.1)
def party(n,b,cap=100,star=1.0):
    g=lambda k:1+min(b.get(k,0)+b.get('all',0),cap)/100
    return [U(60*star*g('hp'),12*star*g('atk'),10*star*g('df'),10*star*g('spd'),0) for _ in range(n)]
def fight(P,E,taken=1.0,regen=0,first=0):
    for u in P+E: u.t=100/u.spd*R.uniform(.9,1.1)
    ex={}
    if first:
        for u in P: u.t=0; ex[id(u)]=first-1
    while True:
        ap=[u for u in P if u.hp>0]; ae=[e for e in E if e.hp>0]
        if not ae: return True
        if not ap: return False
        u=min(ap+ae,key=lambda x:x.t)
        if u.side==0:
            t=min(ae,key=lambda e:e.hp); t.hp-=dmg(u.atk,t.df)*(1.5 if R.random()<.05 else 1)
            if regen:
                for p in ap: p.hp=min(p.mhp,p.hp+p.mhp*regen/len(ap))
            if ex.get(id(u),0)>0: ex[id(u)]-=1
            else: u.t+=100/u.spd
        else:
            t=R.choice(ap); t.hp-=dmg(u.atk,t.df)*taken; u.t+=100/u.spd
# boss template scaled by party size n and factor k (hp, atk, df scale together)
def boss(n,k): return [U(77*n*k,20*k,15*k,15,1)]
def winrate(n,k,b,opt,N=300,star=1.0):
    return sum(fight(party(n,b,star=star),boss(n,k),**opt) for _ in range(N))/N
def strength(n,b={},opt={},star=1.0,N=300):
    lo,hi=0.3,6.0
    for _ in range(11):
        m=(lo*hi)**.5
        if winrate(n,m,b,opt,N,star)>.5: lo=m
        else: hi=m
    return (lo*hi)**.5
if __name__=='__main__':
    for n in [2,3,4,5]: print(n,round(strength(n),3))
