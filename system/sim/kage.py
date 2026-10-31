"""カゲ（雑魚）の種類：階層ごとの4種＋まれな1種。第3版の雑魚の強さ（res_final4.json の km）を1とした倍率"""
import json, random
import f4lib as F
E=F.E
R=E.R
# 名前, 系統, 苦手な系統, 得意な系統, (HP, 攻撃, 防御, 素早さ) の倍率, わざ
FLOORS={
 '序章':('団地のエレベーター',[
   ('ほこりだま','白',('赤',),(),(0.9,0.9,1.0,1.0),None),
   ('切れた電球','黄',('青',),(),(0.8,1.0,0.8,1.3),None),
   ('ちぎれたチラシ','紫',('緑',),(),(0.9,0.9,0.9,1.1),'down'),
   ('なくした鍵','青',('黄',),(),(1.2,0.8,1.3,0.7),None)],
   ('迷子の風船','黄',(),(),(0.6,0.5,0.6,1.5),'flee')),
 '1章':('シャッター街',[
   ('売れ残りの招き猫','青',('黄',),('赤',),(1.3,0.8,1.4,0.6),'guard'),
   ('剥がれた値札','赤',('青',),(),(0.8,1.3,0.8,1.1),None),
   ('シャッターガラガラ','紫',('緑',),(),(1.0,0.8,1.1,0.9),'aoe'),
   ('回らない福引き','紫',('白',),(),(1.0,0.9,0.9,1.0),'sleep')],
   ('閉店セールの看板','白',(),(),(0.7,0.5,0.7,1.4),'flee')),
 '2章':('水びたしの倉庫街',[
   ('迷子のブイ','緑',('赤',),('青',),(1.1,0.7,1.0,0.9),'heal'),
   ('錆びた錨','青',('黄',),('赤',),(1.4,1.3,1.3,0.5),None),
   ('濡れた段ボール','紫',('白',),(),(0.9,0.9,0.9,1.0),'down'),
   ('破れた漁網','紫',('緑',),(),(1.0,0.8,0.9,1.1),'slow')],
   ('瓶詰めの手紙','白',(),(),(0.7,0.5,0.7,1.4),'flee')),
 '3章':('坂と階段の迷路',[
   ('片方の靴','黄',('青',),(),(0.8,1.1,0.8,1.5),None),
   ('鳴りやまない目覚まし','黄',('紫',),('黄',),(0.8,0.9,0.9,1.2),'double'),
   ('返されない本','白',('白',),('紫',),(1.2,0.8,1.4,0.8),'guard'),
   ('落ち葉の山','緑',('赤',),(),(1.1,0.8,1.0,1.0),'heal')],
   ('置き去りの三輪車','白',(),(),(0.7,0.5,0.7,1.4),'flee')),
 '4章':('団地を裏返した階層',[
   ('消えた表札','紫',('白',),(),(1.0,1.0,1.0,1.0),'sleep'),
   ('割れた植木鉢','緑',('赤',),(),(1.1,0.8,1.0,1.0),'heal'),
   ('鳴らない呼び鈴','黄',('青',),(),(0.8,1.1,0.8,1.4),'first'),
   ('開かない郵便受け','青',('黄',),('赤',),(1.3,0.9,1.4,0.6),'guard')],
   ('古い鍵束','白',(),(),(0.7,0.5,0.7,1.4),'flee')),
 '終章':('303の中（最深部）',[
   ('言えなかった約束','紫',('緑',),(),(1.0,1.0,1.0,1.0),'down'),
   ('だれかの落書き','赤',('青',),(),(0.8,1.3,0.8,1.1),'aoe'),
   ('欠けた集合写真','白',('紫',),(),(1.1,0.9,1.2,0.9),'guard'),
   ('冷めたお弁当','赤',('白',),('緑',),(1.0,1.2,0.9,1.0),None)],
   ('子どもの長靴','白',(),(),(0.7,0.5,0.7,1.4),'flee')),
}
CHMAP={'序章':'1章','1章':'2章','2章':'3章','3章':'4章','4章':'5章','終章':'終章'}  # 第3版の表の行（旧い章の呼び方）との対応
RARE=0.05
def spawn(stage,k,lv,cnt=4):
    _,pool,rare=FLOORS[stage]; g=E.G(lv); out=[]
    for i in range(cnt):
        sp=rare if R.random()<RARE else R.choice(pool)
        name,grp,weak,res,(h,a,d,s),sk=sp
        e=E.U(name,grp,3,lv,1); e.mhp=e.hp=30*k*g*h; e.atk=9*k*g*a; e.df=10*k*g*d; e.spd=10*g*s
        e.weak=weak; e.resist=res; e.skill=sk; e.grp=grp; out.append(e)
    return out
def kage_act(e,ap,ctx):
    sk=e.skill
    if sk and R.random()<.3:
        if sk=='aoe':
            for p in ap: E.hit(e,p,.5,ctx)
            return True
        if sk=='down': R.choice(ap).st['down']=3; return True
        if sk=='slow':
            for p in ap: p.t+=30/p.spd
            return True
        if sk=='sleep':
            t=R.choice(ap)
            if not t.st.get('immune') and R.random()<.5: t.st['sleep']=2
            return True
        if sk=='guard': e.df*=1.3; e.skill=None; return True
        if sk=='heal':
            al=[x for x in ctx.get('_enemies',[]) if x.hp>0]
            if al:
                t=min(al,key=lambda x:x.hp/x.mhp); t.hp=min(t.mhp,t.hp+t.mhp*.25); return True
        if sk=='flee': e.hp=0; return True
    if sk=='double': E.hit(e,R.choice(ap),.6,ctx); E.hit(e,R.choice(ap),.6,ctx); return True
    return False
_orig=E.enemy_act
def enemy_act(e,ap,ctx):
    if getattr(e,'weak',None) is not None and kage_act(e,ap,ctx): return
    _orig(e,ap,ctx)
E.enemy_act=enemy_act
def fight(P,mobs,o):
    o=dict(o); o['_enemies']=mobs
    # first: 鳴らない呼び鈴がいると、こちらの先制を打ち消す
    if any(m.skill=='first' for m in mobs): o['first']=0
    return E.battle(P,mobs,o)
def measure(stage,N=400):
    old=CHMAP[stage]; R4=json.load(open('res_final4.json'))[old]
    lv=R4['lv']; names=R4['party']; km=R4['km']
    b,o=F.bon('ふつう',old)
    L=[];wipe=0
    for _ in range(N):
        P=F.party(list(names),lv,b); mobs=spawn(stage,km,lv)
        ok,_=fight(P,mobs,o); wipe+=not ok
        L.append(1-sum(max(0,p.hp) for p in P)/sum(p.mhp for p in P))
    L.sort()
    return dict(mean=sum(L)/N,p90=L[int(N*.9)],wipe=wipe/N)
if __name__=='__main__':
    out={}
    for st in FLOORS:
        out[st]=measure(st); print(st,{k:round(v,3) for k,v in out[st].items()},flush=True)
    json.dump(out,open('res_kage.json','w'),ensure_ascii=False)
