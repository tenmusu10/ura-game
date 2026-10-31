import json
from strength import winrate
d=json.load(open('res_final.json')); T=d['table']
G=lambda lv:1+0.08*(lv-1)
chs=['1章','2章','3章','4章','5章','終章']
rep={}
for rule in ['いまのルール','調整案']:
    for ch in chs:
        f=T[f'{rule}|ふつう|{ch}']; k=f['k']*0.92; n=f['n']; lv=f['lv']
        wr={m:winrate(n,k,T[f'{rule}|{m}|{ch}']['out'],{kk:(round(v) if kk=='first' else v) for kk,v in T[f'{rule}|{m}|{ch}']['opt'].items() if not(kk=='taken' and v==1)},N=600,star=T[f'{rule}|{m}|{ch}']['star']) for m in ['おまかせ','ふつう','やりこみ']}
        g=G(lv)
        boss=dict(HP=round(77*n*k*g),攻撃=round(20*k*g),防御=round(15*k*g),素早さ=round(15*g))
        mob=dict(HP=round(30*k*0.85*g),攻撃=round(9*k*0.85*g),防御=round(10*k*0.85*g),素早さ=round(10*g))
        rep[f'{rule}|{ch}']=dict(k=k,boss=boss,mob=mob,wr=wr,lv=lv,n=n)
        print(rule,ch,lv,n,boss,mob,{m:f'{v:.0%}' for m,v in wr.items()},flush=True)
json.dump(rep,open('res_enemy.json','w'),ensure_ascii=False)
