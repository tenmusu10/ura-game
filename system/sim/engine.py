"""戦闘シミュレータ v2：わざ・回復・状態異常つき"""
import random, json
R=random.Random(11)
CH=json.load(open('res_chars.json'))
STAR={1:.85,2:.92,3:1.0,4:1.08,5:1.18,6:1.30}
PROF={'赤':dict(hp=.95,atk=1.3,df=.8,spd=.95),'青':dict(hp=1.3,atk=.8,df=1.4,spd=.7),
      '緑':dict(hp=1.15,atk=.85,df=1.0,spd=1.0),'黄':dict(hp=.9,atk=1.05,df=.85,spd=1.3),
      '白':dict(hp=1.0,atk=1.0,df=1.0,spd=1.0),'紫':dict(hp=.95,atk=1.0,df=.95,spd=1.1),'?':dict(hp=1,atk=1,df=1,spd=1)}
G=lambda lv:1+0.08*(lv-1)
# 固有わざ：key -> (種類, 回数)。数値は下の act() に書く
SKILL={'ユズコ':'renda','ゲンゾウ':'guard','ミツキ':'p_spd','トメヨ':'healall','ポチタ':'atkdown','マネキチ':'mirror',
 'フミオ':None,'ニボシ':None,'サキミキ':'p_twin','ミオ':'p_revive','カサジロウ':'umbrella','カタッポ':'handheal',
 'ペンタ':None,'カナエ':'blind','ゴウダ':'revenge','シズカ':None,'リョウ':'encore','ジハンキ':'p_lucky',
 'チヨノ':'p_regen','キナコ':'kuji','ボンボン':'sleep','レイジ':'p_watch','マワリ':'haste','ミチノスケ':'teikoku',
 'ミナト':'taunt','ヒナコ':'hina','ユメミ':'steal','サカキ':None,'トモシビ':'p_first','カゲモリ':'p_ura','主人公':'aikagi'}
USES=3   # 固有わざ：1夜に3回（第3版）
MISS=0.04; SPREAD=(.8,1.2); ECRIT=0.03
LEARNED_HOOK=None
CRIT=[0.0]
class U:
    def __init__(s,name,grp,star,lv,side,bonus=None,skill=None,mult=1.0):
        b=bonus or {}; p=PROF.get(grp,PROF['白']); g=G(lv)*STAR.get(star,1)*mult
        f=lambda k:1+b.get(k,0)/100
        s.name=name; s.side=side; s.grp=grp
        s.mhp=60*p['hp']*g*f('hp'); s.hp=s.mhp; s.atk=12*p['atk']*g*f('atk'); s.df=10*p['df']*g*f('df'); s.spd=10*p['spd']*g*f('spd')
        s.skill=skill; s.uses=USES; s.t=0; s.st={}  # status: name->turns
        s.taunt=0; s.mirror=False; s.next_mult=1.0; s.dead_once=False
    def alive(s): return s.hp>0
def mkparty(names,lv,bonus,first_bonus=0):
    out=[]
    for n in names:
        if n=='主人公': out.append(U('主人公','?',3,lv,0,bonus,'aikagi'))
        elif n.startswith('_'): out.append(U(n,'白',3,lv,0,bonus,None))   # 比較用の素の住人
        else:
            c=next(c for c in CH if c['name']==n); out.append(U(n,c['grp'],c['star'],lv,0,bonus,SKILL[n]))
    return out
def mkboss(n,k,lv):
    g=G(lv); b=U('ボス','紫',3,lv,1); b.mhp=b.hp=77*n*k*g; b.atk=20*k*g; b.df=15*k*g; b.spd=15*g; b.uses=99; b.skill='boss'; b.rage=False
    return [b]
def mkmobs(k,lv,cnt=3):
    g=G(lv); out=[]
    for i in range(cnt):
        e=U(f'カゲ{i}','紫',3,lv,1); e.mhp=e.hp=30*k*g; e.atk=9*k*g; e.df=10*k*g; e.spd=10*g; out.append(e)
    return out
def hit(a,t,mult=1.0,ctx=None):
    if a.side==1 and a.st.get('blind'): 
        if R.random()<.3: return 0
    if t.st.get('sleep'): t.st.pop('sleep')
    atk=a.atk*(0.8 if a.st.get('down') else 1)*(1.3 if getattr(a,'rage',False) else 1)
    df=t.df*(2.0 if t.taunt else 1)*(1.3 if (t.side==0 and ctx and ctx.get('watch')) else 1)
    if R.random()<MISS: return 0
    d=atk*atk/(atk+df)*2*mult*R.uniform(*SPREAD)
    if a.side==1 and R.random()<ECRIT: d*=1.8
    if a.side==0 and R.random()<.05+CRIT[0]: d*=1.5
    if t.side==0 and ctx:
        d*=ctx.get('taken',1.0)
        if ctx.get('niou'): d*=.75
        kb=ctx.get('kabau')
        if kb and kb[2]>0 and t is kb[1] and kb[0].alive(): t=kb[0]
        if t.st.get('teppeki'): d*=.5
        if ctx.get('umbrella'): ctx['umbrella']=0; return 0
        g=ctx.get('guard')
        if g and g.alive() and t is not g: d*=.5; g.hp-=d*.5; return d
        if g is t: d*=.5
    if t.taunt: d*=.7
    t.hp-=d
    if t.hp<=0 and getattr(t,'sutemi',False): t.sutemi=False; t.hp=1
    if t.mirror and t.alive():
        t.mirror=False; a.hp-=d
    return d
def battle(P,E,ctx=None,maxt=400):
    ctx=dict(ctx or {}); regen=ctx.get('regen',0); CRIT[0]=0.0
    names={u.name for u in P}
    if 'カサジロウ' in names: ctx['umbrella']=1
    if 'レイジ' in names: ctx['watch']=1
    for u in P:
        if u.skill=='p_spd': u.spd*=1.15
        if u.skill=='p_ura': u.atk*=1.08;u.df*=1.08;u.mhp*=1.08;u.hp=u.mhp
    for u in P+E: u.t=100/u.spd*R.uniform(.9,1.1)
    first=ctx.get('first',0)+(1 if any(u.skill=='p_first' for u in P) else 0)
    if first:
        for u in P: u.t=0.001*R.random()
    revive=any(u.skill=='p_revive' for u in P); acts=0
    while acts<maxt:
        ap=[u for u in P if u.alive()]; ae=[e for e in E if e.alive()]
        if not ae: return True,acts
        if revive and ctx.get('mio')=='one50':
            dead=[p for p in P if not p.alive()]
            if dead and ap: revive=False; dead[0].hp=dead[0].mhp*.5; continue
        if not ap:
            if revive:
                revive=False
                MIO=ctx.get('mio','all50')
                if MIO=='all50':
                    for u in P: u.hp=u.mhp*.5
                elif MIO=='all20':
                    for u in P: u.hp=u.mhp*.2
                continue
            return False,acts
        u=min(ap+ae,key=lambda x:x.t); now=u.t; acts+=1
        for k in list(u.st):
            if k!='sleep':
                u.st[k]-=1
                if u.st[k]<=0: u.st.pop(k)
        if u.st.get('sleep'):
            u.st['sleep']-=1
            if u.st['sleep']<=0: u.st.pop('sleep')
            u.t=now+100/u.spd; continue
        if u.side==0:
            act(u,ap,ae,ctx)
            if regen:
                for p in ap: p.hp=min(p.mhp,p.hp+p.mhp*regen/len(ap))
            if any(x.skill=='p_regen' and x.alive() for x in P):
                for p in ap: p.hp=min(p.mhp,p.hp+p.mhp*.03/len(ap))
            u.t=now+100/u.spd
            if u.taunt: u.taunt-=1
        else:
            enemy_act(u,ap,ctx); u.t=now+100/u.spd
        if ctx.get('niou'): ctx['niou']-=1
        if ctx.get('kabau'): kb=ctx['kabau']; ctx['kabau']=(kb[0],kb[1],kb[2]-1) if kb[2]>1 else None
        ctx['dead']=[p for p in P if p.hp<=0]
        if ctx.get('guard_t'):
            ctx['guard_t']-=1
            if ctx['guard_t']<=0: ctx['guard']=None
    return False,acts
def lowest(ap): return min(ap,key=lambda p:p.hp/p.mhp)
def act(u,ap,ae,ctx):
    tgt=min(ae,key=lambda e:e.hp); s=u.skill; low=lowest(ap)
    if s=='aikagi' and u.uses>0:   # 主人公：となりのわざを1回借りる → 仲間で一番役に立つわざをまねる
        cands=[p.skill for p in ap if p is not u and p.skill and not p.skill.startswith('p_')]
        if cands:
            u.uses-=1; s2=('healall' if 'healall' in cands and low.hp/low.mhp<.5 else R.choice(cands))
            return use(u,s2,ap,ae,tgt,low,ctx,borrowed=True)
    if s and not s.startswith('p_') and u.uses>0:
        if use(u,s,ap,ae,tgt,low,ctx): return
    if LEARNED_HOOK and LEARNED_HOOK(u,ap,ae,tgt,low,ctx): return
    m=u.next_mult; u.next_mult=1.0
    hit(u,tgt,m)
    if s=='p_lucky' and R.random()<1/8: hit(u,tgt,2.0)
    if s=='p_twin':
        low.hp=min(low.mhp,low.hp+low.mhp*.06)
def use(u,s,ap,ae,tgt,low,ctx,borrowed=False):
    """使ったら True"""
    dec=lambda:None if borrowed else setattr(u,'uses',u.uses-1)
    boss=len(ae)==1
    if s=='renda': dec(); [hit(u,tgt,.55) for _ in range(3)]; return True
    if s=='guard' and min(p.hp/p.mhp for p in ap)<.7 and not ctx.get('guard'):
        dec(); ctx['guard']=u; ctx['guard_t']=len(ap)+2; return True
    if s=='healall' and sum(p.hp/p.mhp<.6 for p in ap)>=2:
        dec(); [setattr(p,'hp',min(p.mhp,p.hp+p.mhp*.35)) or p.st.clear() for p in ap]; return True
    if s=='atkdown' and not ae[0].st.get('down'):
        dec(); [e.st.__setitem__('down',4) for e in ae]; return True
    if s=='mirror' and not u.mirror: dec(); u.mirror=True; return True
    if s=='umbrella': return False
    if s=='handheal' and sum(p.hp/p.mhp<.7 for p in ap)>=2:
        dec(); pairs=len(ap)-1; [setattr(p,'hp',min(p.mhp,p.hp+p.mhp*.05*pairs)) for p in ap]; return True
    if s=='blind' and not ae[0].st.get('blind'): dec(); [e.st.__setitem__('blind',4) for e in ae]; return True
    if s=='revenge' and u.hp/u.mhp<.6: dec(); hit(u,tgt,1+2.5*(1-u.hp/u.mhp)); return True
    if s=='encore':
        best=max([p for p in ap if p is not u],key=lambda p:p.atk,default=None)
        if best: dec(); hit(best,tgt,1.0); return True
    if s=='kuji': dec(); R.choice(ap).next_mult=2.0; hit(u,tgt,1.0); return True
    if s=='sleep':
        if boss: return False
        dec()
        for e in ae:
            if R.random()<(.25 if boss else .6): e.st['sleep']=2
        return True
    if s=='haste' and u.uses>0: dec(); [setattr(p,'spd',p.spd*1.1) for p in ap]; return True
    if s=='teikoku': dec(); hit(u,tgt,1.5); u.t-=50/u.spd; return True
    if s=='taunt' and not u.taunt: dec(); u.taunt=4; return True
    if s=='hina' and (any(p.st for p in ap) or low.hp/low.mhp<.6):
        dec(); [setattr(p,'hp',min(p.mhp,p.hp+p.mhp*.1)) or p.st.clear() or p.st.__setitem__('immune',4) for p in ap]; return True
    if s=='steal' and getattr(ae[0],'rage',False): dec(); ae[0].rage=False; u.atk*=1.3; return True
    return False
def enemy_act(e,ap,ctx):
    tgt=next((p for p in ap if p.taunt),None) or R.choice(ap)
    if e.skill=='boss':
        if not e.rage and e.hp<e.mhp*.5: e.rage=True; return
        e.uses=getattr(e,'cnt',0)+1; e.cnt=e.uses
        if e.cnt%3==0:
            for p in ap: hit(e,p,.55,ctx)
            return
        if e.cnt%4==0 and not tgt.st.get('immune'): tgt.st['down']=3
    hit(e,tgt,1.0,ctx)
