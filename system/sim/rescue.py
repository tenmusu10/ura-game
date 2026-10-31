"""救済策の効果：適当なパーティが、推奨レベルのボスに勝率5割で勝つのに必要な追加レベル"""
import json, random
import f4lib as F
E=F.E
R4=json.load(open('res_final4.json'))
RR=random.Random(3)
def need(ch,variant):
    v=R4[ch]; lv=v['lv']; n=v['n']; kb=v['kb']
    pool=[c['name'] for c in E.CH if c['star']<=F.MAXSTAR[ch] and (c['name']!='ミオ' or ch=='終章')]
    rnd=lambda: ['主人公']+RR.sample(pool,n-1)
    bo,oo=F.bon('おまかせ',ch)
    if variant in ('line','all'): bo,oo=F.bon('ふつう',ch)   # 出撃を一列にするだけ（団地の並びは考えない）は「ふつう」の値に近いので上限として使う
    orig=dict(E.STAR)
    if variant in ('grow','all'):
        # ★1〜2の伸びしろ：Lvが上がるほど★の差が縮み、Lv40で半分になる
        g=min(1,lv/40)*.5
        for s_ in E.STAR: E.STAR[s_]=orig[s_]+(1.0-orig[s_])*g if orig[s_]<1 else orig[s_]
    for add in range(0,41,2):
        if F.boss_wr(rnd,lv+add,n,kb,bo,oo,N=150,blv=lv)[0]>=.5:
            E.STAR.update(orig); return add
    E.STAR.update(orig); return None
out={}
for ch in ['3章','4章','5章','終章']:
    out[ch]={v:need(ch,v) for v in ['none','grow','line','all']}
    print(ch,out[ch],flush=True)
json.dump(out,open('res_rescue.json','w'),ensure_ascii=False)
