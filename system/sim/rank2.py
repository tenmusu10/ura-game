from rank import strength
import engine as E
base=strength(['主人公','_a','_b','_c','_d'],N=300)
for n in ['ゲンゾウ','ミナト','ゴウダ','カサジロウ','レイジ','ボンボン']:
    print(n,round(strength(['主人公','_a','_b','_c',n],N=300)/base,3),flush=True)
for v in ['all50','all20','one50']:
    print('ミオ',v,round(strength(['主人公','_a','_b','_c','ミオ'],ctx={'mio':v},N=300)/base,3),flush=True)
