# 戦闘シミュレータ

Python 3 だけで動きます（追加のライブラリはいりません）。このフォルダの中で実行してください。

| ファイル | 中身 |
|---|---|
| res_chars.json | characters_30.md から読み込んだ住人のデータ |
| prog.py / rules.py | 団地の並び（こせい枠の解放つき）を最適化して、章ごとのボーナスを出す。`OLD` が元のルール、`NEW` に上書きした `NEW2`（final2.py の中）が調整案2 |
| strength.py | 第1版：通常攻撃だけの戦闘 |
| final2.py | 第1版：ルールごと・章ごとの戦力（res_final2.json を作る） |
| engine.py | 第2版：わざ・回復・状態異常つきの戦闘 |
| rank.py / rank2.py | 第2版：住人1人ずつの戦力（res_rank.txt） |
| final3.py | 第2版：章ごとの敵の強さの逆算（res_final2.json を使う） |
| learned.py | 第3版：レベルアップで覚えるわざ24種 |
| final4.py / f4lib.py | 第3版：ドラクエくらいの難易度で敵を逆算（夜回りの連戦つき）→ res_final4.json |
| rescue.py | 第3版：救済策の効果 → res_rescue.json |

```
python3 final2.py   # 数分
python3 rank.py     # 10分ほど
python3 final3.py   # 10分ほど
python3 final4.py   # 15分ほど
python3 rescue.py   # 10分ほど
```

※ engine.py は第3版の設定（固有わざ1夜3回、ダメージのぶれ±20%など）になっています。第2版の数字を出し直すときは、engine.py の先頭の USES・MISS・SPREAD・ECRIT を第2版の値（2・0・(.9,1.1)・0）に戻してください。
