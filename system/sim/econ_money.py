"""ヒノカケラの出入り：章ごとの使い道から、雑魚1組あたりの稼ぎを逆算"""
import json, math
FIGHTS=8
REPAIR={'3×3':300,'4×4':800,'5×5':2000}
GRADE={2:200,3:500,4:1200,5:3000}    # 部屋の格を1つ上げる値段
ITEM={'おにぎり':30,'お弁当':200,'栄養ドリンク':500,'気つけ薬':300,'目覚まし時計':50}
# 章ごと：(夜の数, 直す部屋, 格上げの目安 {格:部屋数}, 1夜のアイテム代, 振り直しの回数)
PLAN={
 '1章':(15,[],{2:4,3:2},4*30,0),
 '2章':(20,[('3×3',4)],{2:4,3:4,4:1},3*30+1*200,3),
 '3章':(25,[('4×4',7)],{3:6,4:4,5:1},2*30+1*200+0.3*300,8),
 '4章':(25,[],{4:6,5:3},2*30+1*200+0.5*500,10),
 '5章':(30,[('5×5',9)],{4:6,5:4},2*200+0.5*500+0.5*300,12),
 '終章':(15,[],{5:4},2*200+1*500+0.5*300,6),
}
LV={'1章':10,'2章':18,'3章':25,'4章':32,'5章':40,'終章':45}
rows=[]
for ch,(nights,rep,gr,itm,rr) in PLAN.items():
    r=sum(REPAIR[s]*c for s,c in rep); g=sum(GRADE[k]*c for k,c in gr.items()); i=itm*nights
    slot=2 if LV[ch]<25 else (3 if LV[ch]<40 else 4); rc=rr*100*slot
    total=r+g+i+rc
    boss=0.15*total    # ボス・宝箱・イベントで15%
    per_fight=(total-boss)/(nights*FIGHTS)
    rows.append(dict(ch=ch,nights=nights,repair=r,grade=g,item=i,reroll=rc,total=round(total),per_night=round(total/nights),per_fight=round(per_fight)))
for x in rows: print(x)
lx=[math.log(LV[x['ch']]) for x in rows]; ly=[math.log(x['per_fight']) for x in rows]
n=len(rows); mx=sum(lx)/n; my=sum(ly)/n
B=sum((a-mx)*(b-my) for a,b in zip(lx,ly))/sum((a-mx)**2 for a in lx); A=math.exp(my-B*mx)
print('mob group カケラ = %.2f * Lv^%.2f'%(A,B)); print([(x['ch'],x['per_fight'],round(A*LV[x['ch']]**B)) for x in rows])
json.dump(dict(rows=rows,A=A,B=B,GRADE=GRADE,REPAIR=REPAIR,ITEM=ITEM),open('econ_money.json','w'),ensure_ascii=False)
