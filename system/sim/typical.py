"""ふつうに家具をそろえ、留守番もいるときに、第3版のボスの勝率がどう変わるか"""
import json
import f4lib as F
from rusuban import rusu_effects, merge
R4=json.load(open('res_final4.json'))
TYP_RUSU={'赤':2,'青':2,'緑':2}
TYP_FURN={'hp':4,'atk':4,'df':3,'spd':2}   # 1部屋に家具3つ、★2〜3中心。1人の合計+13%を上限+10%に丸めた想定
out={}
for ch in ['1章','2章','3章','4章','5章','終章']:
    v=R4[ch]; lv=v['lv']; n=v['n']; names=v['party']
    bf,of=F.bon('ふつう',ch); rb,ph=rusu_effects(TYP_RUSU)
    b=merge(merge(bf,rb),TYP_FURN)
    w0=F.boss_wr(lambda:list(names),lv,n,v['kb'],bf,of,N=400)[0]
    w1=F.boss_wr(lambda:list(names),lv,n,v['kb'],b,of,N=400)[0]
    k60=F.bisect(lambda m:F.boss_wr(lambda:list(names),lv,n,m,b,of,N=200)[0],.6)
    out[ch]=dict(wr_before=w0,wr_after=w1,k60=k60,scale=k60/v['kb'])
    print(ch,round(w0,2),round(w1,2),round(k60/v['kb'],3),flush=True)
json.dump(out,open('res_typical.json','w'),ensure_ascii=False)
