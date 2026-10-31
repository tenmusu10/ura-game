import json
from rules import OLD,NEW,run
from strength import strength
NEW2=dict(NEW,name='調整案2',hito={2:2,3:4,4:7,5:10},pair=1,cap_all=25,floor=8)
base={n:strength(n,N=500) for n in [2,3,4,5]}
table={}
for R_ in [OLD,NEW,NEW2]:
    for mode in ['おまかせ','ふつう','やりこみ']:
        runs=[run(R_,mode,s) for s in range(2)]
        for ci in range(6):
            cs=[r[ci] for r in runs]; c=cs[0]
            out={k:sum(x['out'][k] for x in cs)/2 for k in c['out']}
            opt={}
            for x in cs:
                for k,v in x['opt'].items(): opt[k]=opt.get(k,0)+v/2
            if 'first' in opt: opt['first']=round(opt['first'])
            if opt.get('taken')==1.0: opt.pop('taken')
            st=strength(c['n'],out,opt,N=500)
            table[f"{R_['name']}|{mode}|{c['ch']}"]=dict(out=out,opt=opt,rel=st/base[c['n']])
        print(R_['name'],mode,[round(table[f"{R_['name']}|{mode}|{ch}"]['rel'],2) for ch in ['1章','2章','3章','4章','5章','終章']],flush=True)
json.dump(table,open('res_final2.json','w'),ensure_ascii=False)
