"""成長と経済のバランス（計算だけ）"""
import math, json
need=lambda lv: round(8*lv**1.7)            # 次のレベルまで
cum=lambda lv: sum(need(l) for l in range(1,lv))  # Lv1→lv までの合計
CH=[('1章',10,15),('2章',18,20),('3章',25,25),('4章',32,25),('5章',40,30),('終章',45,15)]  # 章, 章末の推奨Lv, 夜の数
FIGHTS=8   # 1夜の雑魚戦（第3版のシミュレーションで5〜15戦）
GRIND_SHARE=.8  # 雑魚戦の経験値でレベルの8割、残りはボス・イベント
rows=[];prev=1;exp_tab=[]
for ch,lv,nights in CH:
    gain=cum(lv)-cum(prev); per_fight=gain*GRIND_SHARE/(nights*FIGHTS)
    # 3レベル上げるのに何夜かかるか（ドラクエのレベル上げの手間）
    up3=(cum(lv+3)-cum(lv))/(per_fight*FIGHTS)
    rows.append(dict(ch=ch,lv=lv,nights=nights,gain=gain,per_fight=round(per_fight),boss=round(gain*(1-GRIND_SHARE)),up3=round(up3,1)))
    prev=lv
for r in rows: print(r)
# 雑魚1組（4体）の経験値を、敵のレベルの式で表す：EXP = A × Lv^B
import itertools
xs=[(r['lv'],r['per_fight']) for r in rows]
# 最小二乗（log）
n=len(xs); lx=[math.log(a) for a,_ in xs]; ly=[math.log(b) for _,b in xs]
mx=sum(lx)/n; my=sum(ly)/n
B=sum((a-mx)*(b-my) for a,b in zip(lx,ly))/sum((a-mx)**2 for a in lx); A=math.exp(my-B*mx)
print('mob group EXP = %.2f * Lv^%.2f'%(A,B))
for lv,pf in xs: print(lv,pf,round(A*lv**B))
json.dump(dict(rows=rows,A=A,B=B),open('econ_exp.json','w'),ensure_ascii=False)
