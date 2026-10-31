"""レベルアップで覚えるわざ（3択）の数値と、戦闘での動き"""
import engine as E
R=E.R
# key: (名前, ★, 系統, 説明)
POOL={
 # 赤：攻撃
 'oogiri':('大ぶり',1,'赤','敵1体に倍率1.6'),
 'nagi':('なぎはらい',2,'赤','敵全体に倍率0.6'),
 'tame':('力ため',3,'赤','次の自分の攻撃が2.2倍'),
 'kaen':('ごちそう攻め',5,'赤','敵1体に倍率2.5'),
 # 青：守り
 'kabau':('かばう',1,'青','一番弱っている味方への攻撃を3行動かわりに受ける'),
 'teppeki':('てっぺき',2,'青','3行動のあいだ自分の被ダメージ−50%'),
 'niou':('みんなの盾',4,'青','4行動のあいだ味方全員の被ダメージ−25%'),
 'sutemi':('すてみの守り',5,'青','HPが30%を切ると1回だけ1で踏みとどまる（常時）'),
 # 緑：回復
 'teate':('てあて',1,'緑','味方1人のHP30%回復'),
 'oyatsu':('みんなでおやつ',2,'緑','味方全員のHP15%回復'),
 'genki':('げんきの素',4,'緑','倒れた味方1人をHP30%でよみがえらせる'),
 'daikaifuku':('おおなべ',5,'緑','味方全員のHP35%回復'),
 # 黄：素早さ
 'hayaoki':('はやおき',1,'黄','味方全員の素早さ+15%'),
 'renda2':('すばやい連打',2,'黄','敵1体に倍率0.7×2回'),
 'sakidori':('さきどり',3,'黄','すぐにもう1回行動する'),
 'kousoku':('こうそく便',5,'黄','味方全員がすぐに行動する（1回）'),
 # 白：探索・弱点
 'shiraberu':('しらべる',1,'白','敵1体の防御−25%（戦闘中ずっと）'),
 'kansatsu':('よく見る',2,'白','味方全員の会心率+15%'),
 'nukeana':('ぬけ道',3,'白','雑魚戦から必ずにげる（シミュレータでは使わない）'),
 'zukan':('カゲ図鑑',5,'白','敵全体の防御−25%'),
 # 紫：じゃま
 'nemuri':('ねむり歌',1,'紫','雑魚全体を50%で2行動眠らせる'),
 'odokashi':('おどかし',2,'紫','敵全体の攻撃−15%（5行動）'),
 'noroi':('のろい',3,'紫','敵1体の攻撃と防御−20%（戦闘中ずっと）'),
 'uragiri':('うらがえし',5,'紫','敵1体の強化を全部消す'),
}
BYGRP={}
for k,(n,s,g,d) in POOL.items(): BYGRP.setdefault(g,[]).append((k,s))
LIGHT=6   # 覚えたわざは「光」を1つ使う。1夜に6回まで（ドラクエのMPのかわり）
STARP={1:45,2:30,3:15,4:7,5:2.5,6:.5}
def learn(u,lv):
    """Lv10・20・30・40で1つ覚える。3枚から1枚：同じ系統2枚＋ほか1枚。一番★が高いものを選ぶ"""
    g=u.grp if u.grp in BYGRP else R.choice(list(BYGRP))
    u.learned=[]; 
    for step in range(1,lv//10+1):
        cards=[]
        for i in range(3):
            gg=g if i<2 else R.choice(list(BYGRP))
            opts=[(k,s) for k,s in BYGRP[gg] if k not in u.learned]
            if not opts: continue
            ws=[STARP[s] for k,s in opts]
            cards.append(R.choices(opts,ws)[0])
        if cards: u.learned.append(max(cards,key=lambda x:x[1])[0])
    u.luses={k:99 for k in u.learned}; u.light=LIGHT
    if 'sutemi' in u.learned: u.sutemi=True
def try_learned(u,ap,ae,tgt,low,ctx):
    L=getattr(u,'learned',None)
    if not L: return False
    boss=len(ae)==1
    def can(k): return k in L and u.light>0
    def use(k): u.light-=1
    hurt=sum(p.hp/p.mhp<.5 for p in ap)
    if can('daikaifuku') and hurt>=2: use('daikaifuku'); [setattr(p,'hp',min(p.mhp,p.hp+p.mhp*.35)) for p in ap]; return True
    if can('oyatsu') and hurt>=2: use('oyatsu'); [setattr(p,'hp',min(p.mhp,p.hp+p.mhp*.15)) for p in ap]; return True
    if can('teate') and low.hp/low.mhp<.4: use('teate'); low.hp=min(low.mhp,low.hp+low.mhp*.3); return True
    if can('genki') and ctx.get('dead'):
        d=ctx['dead'][0]
        if d.hp<=0: use('genki'); d.hp=d.mhp*.3; return True
    if can('niou') and hurt>=1 and not ctx.get('niou'): use('niou'); ctx['niou']=len(ap)*1+4; return True
    if can('kabau') and low is not u and low.hp/low.mhp<.5: use('kabau'); ctx['kabau']=(u,low,4); return True
    if can('teppeki') and u.hp/u.mhp<.5: use('teppeki'); u.st['teppeki']=3; return True
    if can('odokashi') and not ae[0].st.get('down'): use('odokashi'); [e.st.__setitem__('down',5) for e in ae]; return True
    if can('noroi') and boss and not getattr(tgt,'cursed',False): use('noroi'); tgt.cursed=True; tgt.atk*=.8; tgt.df*=.8; return True
    if can('shiraberu') and not getattr(tgt,'scanned',False): use('shiraberu'); tgt.scanned=True; tgt.df*=.75; return True
    if can('zukan') and not getattr(ae[0],'zk',False): use('zukan'); [setattr(e,'df',e.df*.75) or setattr(e,'zk',True) for e in ae]; return True
    if can('uragiri') and getattr(tgt,'rage',False): use('uragiri'); tgt.rage=False; return True
    if can('hayaoki'): use('hayaoki'); [setattr(p,'spd',p.spd*1.15) for p in ap]; return True
    if can('kousoku'): use('kousoku'); [setattr(p,'t',p.t-100/p.spd) for p in ap]; return True
    if can('kansatsu'): use('kansatsu'); E.CRIT[0]+=.15; return True
    if can('nemuri') and not boss and len(ae)>=2: use('nemuri'); [e.st.__setitem__('sleep',2) for e in ae if R.random()<.5]; return True
    if can('nagi') and len(ae)>=2: use('nagi'); [E.hit(u,e,.6) for e in ae]; return True
    if can('kaen'): use('kaen'); E.hit(u,tgt,2.5); return True
    if can('tame') and boss: use('tame'); u.next_mult=2.2; return True
    if can('oogiri'): use('oogiri'); E.hit(u,tgt,1.6); return True
    if can('renda2'): use('renda2'); E.hit(u,tgt,.7); E.hit(u,tgt,.7); return True
    if can('sakidori'): use('sakidori'); E.hit(u,tgt,1.0); u.t-=100/u.spd; return True
    return False
