"""留守番と家具の効果を、第3版の敵（res_final4.json）で確かめる"""
import json, random, sys
import f4lib as F
E=F.E; L=F.L
R4=json.load(open('res_final4.json'))
RR=random.Random(21)
# 留守番：系統ごと1人あたりの効果（ideas_system.md A章の表）。同じ系統は3人まで重なる
def rusu_effects(counts,per=1.0):
    c={g:min(3,counts.get(g,0)) for g in '赤青緑黄白紫'}
    b={'atk':2*c['赤']*per,'df':2*c['青']*per}
    post_heal=.03*c['緑']*per          # 戦闘のあと全員のHPを回復
    first_down=.05*c['黄']*per         # 不意打ちされる確率が下がる（シミュレータでは使わない）
    return b,post_heal
def merge(b1,b2):
    out=dict(b1)
    for k,v in b2.items(): out[k]=out.get(k,0)+v
    return out
def boss_k50(names,lv,n,b,o,blv):
    return F.bisect(lambda m:F.boss_wr(lambda:list(names),lv,n,m,b,o,N=200,blv=blv)[0],.5)
def night(names,lv,km,b,o,post_heal,items=0,N=200):
    tot=0
    for _ in range(N):
        P=F.party(list(names),lv,b); it=items; c=0
        while c<40:
            for p in P:
                if p.hp>0 and p.hp/p.mhp<.4 and it>0: p.hp+=p.mhp*.3; it-=1
            ok,_=E.battle(P,E.mkmobs(km,lv,F.MOBS),o)
            if not ok: break
            c+=1
            for p in P:
                if p.hp>0: p.hp=min(p.mhp,p.hp+p.mhp*post_heal)
            if any(p.hp<=0 for p in P) or sum(max(0,p.hp) for p in P)/sum(p.mhp for p in P)<.35: break
        tot+=c
    return tot/N
def run(cases):
    out={}
    for ch in ['3章','5章']:
        v=R4[ch]; lv=v['lv']; n=v['n']; names=v['party']
        bf,of=F.bon('ふつう',ch); base_k=v['kb']
        for name,(counts,per,furn) in cases.items():
            rb,ph=rusu_effects(counts,per)
            b=merge(merge(bf,rb),furn)
            k=boss_k50(names,lv,n,b,of,lv)
            nt=night(names,lv,v['km'],b,of,ph)
            out[f'{ch}|{name}']=dict(k=k,night=nt)
            print(ch,name,round(k,3),round(nt,1),flush=True)
    return out
if __name__=='__main__':
    cases={
     'なし':({},1,{}),
     '赤3':({'赤':3},1,{}),
     '青3':({'青':3},1,{}),
     '緑3':({'緑':3},1,{}),
     '赤3青3緑3（最大）':({'赤':3,'青':3,'緑':3},1,{}),
     '緑3・2倍（★1の2倍ルール）':({'緑':3},2,{}),
     '家具 本人+5%×全員':({},1,{'hp':5,'atk':5,'df':5,'spd':5}),
     '家具 本人+10%×全員':({},1,{'hp':10,'atk':10,'df':10,'spd':10}),
     '家具 本人+15%×全員':({},1,{'hp':15,'atk':15,'df':15,'spd':15}),
    }
    res=run(cases)
    json.dump(res,open('res_rusuban.json','w'),ensure_ascii=False)
