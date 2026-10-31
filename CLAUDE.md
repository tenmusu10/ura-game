# CLAUDE.md

おぼろ団地（仮タイトル：ウラガワ・ダンジョン）。昼は団地、夜はダンジョン「ハザマ」にもぐる、団地経営＋ダンジョン探索のドット絵ゲームの企画リポジトリ。エンジンは Godot 4（2D、320×180）。いまは実装前で、世界観と素材生成用のプロンプトを置いている。詳しい説明は [README.md](README.md)、自動化の設定は `kit.config.json`（部品の元は `tenmusu10/teck-matome`）。

## どこに何があるか

大きいファイルは丸ごと読まず、grep で場所を絞ってから要る行だけ読む。

| 場所 | 担当 |
|---|---|
| `prompts/00_world_bible.md` | 世界観バイブル。設定・用語・色・解像度の正本 |
| `prompts/` | 物語・住人・画像・音・映像のプロンプト、検討メモ（`ideas_*.md`＝経過であって決定ではない） |
| `story/` / `system/` / `images/` / `preview/` | 物語の説明図 / 戦闘・数値バランスのシミュレーション / 説明図 / ドット絵の試作 |
| `tools/` | 秘密ファイル・公開前チェック・`kit-config.mjs` |
| `.claude/` | settings.json（読まない場所・フック）・`hooks/guard.mjs` |

## 確かめ方

PR を出す前・完了を報告する前に必ず通す（CI の「チェック」と同じ）。落ちたまま報告しない。

```
npm test                 # 道具のテスト
npm run release:check    # 公開前チェック（仮置き・テスト用 ID）
npm run secret:check     # 秘密ファイル
```

- ドット絵や図の変更は画像を見て確かめる（PR やスレッドに載せる）
- CI は `*.md` だけの変更では走らない（`kit.config.json` の `ci.ignore`）

## PR・ブランチ・コミット

- 1つの話題につき1本の PR。プロジェクトの各スレッドは自分の担当ファイルだけを PR にする
- PR のタイトルは日本語で「何がどう変わるか」を書く。本文は `.github/pull_request_template.md` の5つの見出しで書く
- マージは tenmusu が「マージ」と言ってから（squash だけ使う）
- `.claude/hooks/guard.mjs` が、main への直接 push・force push・CI が緑でない PR のマージを止める。止められたら回避せず、理由に従う

## 壊さない約束

- 設定を変えるときは、まず `prompts/00_world_bible.md` を直してから各ファイルに反映する
- 署名鍵・サービスアカウントの鍵・.env・デプロイ鍵はコミットしない（Secrets に入れる）。`tools/secret-check.mjs` が CI で毎回見る。引っかかったら外して、push 済みなら鍵を作り直す
- Godot のキャッシュ `.godot/` はコミットしない（`*.import` は残す）
