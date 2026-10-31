# 音楽・効果音・映像 プロンプト集（v0.2）

> 世界観バイブル v1.2（00_world_bible.md）の 2章「物語の軸：ドアだけの303号室」・4章の章立てとエンディング・7章・8章 に従って作っています。303号室は、302と304のあいだの壁に表札とドアだけがあり、開けてもすぐ壁です。24部屋の修繕がすべて終わるとドアの向こうに部屋が現れ、終章が始まります。団地にいま管理人はおらず（管理人室は空席、先代管理人サカキは行方不明）、主人公はサカキの孫で31人目の住人です。団地の正式名は「灯野第三団地」、通称は「おぼろ団地」です。用語・色・解像度はバイブルが「正」です。
> **0章の方向性は、すべて★おすすめ案で決定しました（2026-10-31）。** 1〜3章はその案で書いています。ほかの案は、あとで変えたくなったとき用に残しています。

---

## 0. 方向性（★が決定。ほかは控えの案）

### 0-1. BGMの音の時代感

| 案 | 中身 | 合う人 |
|---|---|---|
| A | ファミコン寄り（矩形波2＋三角波＋ノイズの4音だけ）。素朴で懐かしさ最大 | 「レトロさ」を一番に出したい |
| **B ★おすすめ** | スーファミ寄り16bit。チップ音色に、やわらかいエレピ・ストリングス・オルゴールを少し足す。バイブル7-1どおり | 笑いと切なさの両方を出したい |
| C | チップチューン＋ローファイ・ヒップホップ（ビートとテープのゆらぎ）。昼の団地がチルな雰囲気 | 作業用BGMのような心地よさ |
| D | チップチューン＋昭和歌謡・ムード歌謡（団地・商店街の空気） | 「団地」の時代感を強く出したい |
| E | 表はB、裏はシンセウェーブ寄り（ネオン色に合わせて80年代シンセを強め） | 昼夜の差をはっきりさせたい |

### 0-2. メインテーマ（くり返し出てくるメロディ）

| 案 | 中身 |
|---|---|
| **A ★おすすめ** | 「**303号室のテーマ**」を1本作り、OP・団地・切ない場面・エンディングでアレンジ違いを使う。303号室が現れる場面で初めてフルで鳴る |
| B | 表のテーマ・裏のテーマの2本立て。エンディングで2本が重なる |
| C | 曲ごとに独立（作りやすい・統一感は弱め） |

Sunoは同じメロディを狙って出すのが苦手なので、Aの場合は「Cover（カバー）」機能で、1曲目を元に別アレンジを作る方法を使います（1-0参照）。

### 0-3. 団地のBGMの成長

| 案 | 中身 |
|---|---|
| **A ★おすすめ** | 団地の曲は同じ曲で3段階。住人が少ない＝さびしいソロ → 中盤＝楽器が増える → 終盤＝にぎやか。「明かりが増える」を音でも表す |
| B | 段階なし。昼の曲は1つ |
| C | 段階に加えて、れんけいの系統（赤青緑黄白紫）で音色が少し変わる（作る曲数が多い） |

### 0-4. エンディング曲

| 案 | 中身 |
|---|---|
| **A ★おすすめ** | 歌なし。メインテーマのフルアレンジ（オルゴール→全楽器） |
| B | エンディングだけ歌あり（日本語・やさしい女性ボーカル）。バイブルは「歌なし」なので、選ぶならバイブルの例外として追記が必要 |
| C | 歌なし版と歌あり版の両方を作り、分岐エンディングで使い分ける |

### 0-5. 効果音の作り方

| 案 | 中身 |
|---|---|
| **A ★おすすめ** | 文章プロンプトで生成AI（ElevenLabs Sound Effects など）に作らせ、足りない分を下の数値メモで補う |
| B | jsfxr／ChipTone などの「レトロ効果音メーカー」で作る（無料・確実にチップ音になる）。各音に作り方のメモを付ける |
| C | AとBの併用（UIはB、ボス・環境音はA） |

### 0-6. OPの見せ方

| 案 | 中身 |
|---|---|
| **A ★おすすめ** | 「**0時の303号室**」：夕方の団地 → 3階の303のドアを住人が開けると、すぐ壁 → 0時、シャッターが境目になる → ハザマへ → 住人たちが一人ずつ登場 → タイトル |
| B | 「**明かりの数**」：真っ暗な団地の窓に、住人が来るたび1つずつ明かりが灯る。最後に3階だけ窓が1つ少ないことに気づかせる（303号室の伏線） |
| C | 「**主人公の一日**」：朝の掃除、内見、回覧板、夜回り…をテンポよく。コメディ寄り |
| D | AとBの合わせ技（前半A、後半Bの窓の明かり） |

### 0-7. 映像の作り方

| 案 | 中身 |
|---|---|
| **A ★おすすめ** | Geminiでカットごとの1枚絵（キーフレーム）を作り、Godotの中でスクロール・点滅・スプライトを動かしてOPにする。ドット絵がくずれない |
| B | 1枚絵を動画生成AI（画像から動画）で動かし、4章の後処理でドット絵に戻す |
| C | Aを基本に、雨・霧・ネオンのゆらぎなど「難しい動き」だけBで作る |

---

## 1. BGM（Suno）

### 1-0. Sunoの使い方メモ

- **Custom モード** を使う。
  - **Style of Music**：下の各曲の Style をそのまま貼る（先頭にバイブル10章の共通前置きを入れてあります）。
  - **Lyrics**：歌なしなので、構成タグだけを入れる（各曲の「構成」欄）。
  - **Instrumental** をオンにする。
  - **Exclude Styles**（ある場合）：`vocals, singing, choir, rap, orchestral, cinematic, EDM drop, dubstep, heavy distortion`
- **ループ**：Sunoは曲の終わりをフェードや締めで終えることが多い。いい曲ができたら、波形編集ソフト（Audacityなど）でループ区間を切り出し、Godotでは `AudioStreamOggVorbis` の `loop = true` と `loop_offset`（イントロの長さ）を設定する。
- **メインテーマのアレンジ**（0-2 A）：まず 1-1「303号室のテーマ」を作る → その曲の「Cover」で Style だけ差し替えて、団地・切ない場面・エンディング版を作る。
- 1曲につき何回か生成して、**左上の光源のように「明るさの基準」をそろえる**つもりで、音量・音の明るさが近いものを選ぶ。

### 1-1. メイン・タイトル

#### M01 303号室のテーマ（タイトル画面）
- 使う場面：タイトル画面（ゲームのタイトルは「**おぼろ団地と303号室**」）。全体のメロディの元になる曲。
- Style：
```
chiptune, 16-bit, retro game soundtrack, instrumental, loopable, title theme for a game about a hazy forgotten apartment complex and its mysterious door-only room 303, nostalgic and gentle, warm square wave lead melody, soft triangle bass, light music box counter-melody, mid-tempo 96 BPM, major key with a bittersweet minor turn, memorable simple melody, small Japanese seaside town at dusk
```
- 構成：
```
[Intro: music box alone]
[Main Theme]
[Bridge: bittersweet minor]
[Main Theme: fuller]
[Loop]
```

#### M02 オープニング（OP映像用・約75秒）
- 使う場面：OP映像（3-1）。ループしない1曲。
- Style：
```
chiptune, 16-bit, retro game soundtrack, instrumental, opening theme, starts calm then builds, dusk town to midnight mystery, square wave lead, arpeggiated synth, punchy chip drums enter at the middle, uplifting heroic finale, 120 BPM, 75 seconds
```
- 構成：
```
[Intro: quiet dusk, music box]
[Verse: town, warm]
[Break: clock strikes midnight, sudden silence]
[Build: dark arpeggio, mystery]
[Chorus: heroic main theme, full drums]
[Outro: title hit]
[End]
```

### 1-2. 表（昼）＝灯野第三団地（通称おぼろ団地）・灯野市

#### M10 団地のテーマ（3段階）（0-3 A）
共通の Style 先頭：
```
chiptune, 16-bit, retro game soundtrack, instrumental, loopable, home base theme, old Japanese apartment complex, warm and nostalgic,
```

| 曲 | 段階 | Style 後半 |
|---|---|---|
| M10a | 序盤（住人4人まで） | `lonely but hopeful, solo square wave melody with soft triangle bass only, sparse, slow 90 BPM, quiet afternoon, cicadas feeling` |
| M10b | 中盤（3×3〜4×4） | `cozy and lively, square wave lead with electric piano chords, light shaker and soft kick, 100 BPM, lo-fi warmth` |
| M10c | 終盤（5×5） | `bustling and joyful, full chiptune band, two square leads in harmony, bouncy bass, claps, glockenspiel, 108 BPM, festival feeling` |

- 構成（3曲共通）：`[Intro] [A] [B] [A] [Loop]`
- できればM10aをCoverしてM10b・M10cを作る（同じメロディのまま楽器が増える）。

#### M11 団地のメニュー（修繕・部屋の並べ替え）
```
chiptune, 16-bit, retro game soundtrack, instrumental, loopable, menu and puzzle music, calm thinking mood, plucky square wave, soft marimba-like triangle, gentle 92 BPM, light and clean, not distracting
```
構成：`[Intro] [Loop A] [Loop B] [Loop]`

#### M12 内見（入居希望者が来る）
```
chiptune, 16-bit, retro game soundtrack, instrumental, loopable, light comedic tension, a visitor inspecting the room, tiptoe staccato square wave, pizzicato-like bass, playful pauses, 104 BPM, curious and slightly nervous
```

#### M13 回覧板・日常のおしゃべり（コメディ）
```
chiptune, 16-bit, retro game soundtrack, instrumental, loopable, comedy slice of life, silly bouncy melody, kazoo-like square wave, oom-pah bass, woodblock percussion, 112 BPM, boke and tsukkomi timing, cheerful
```

#### M14 灯野市の街（商店街・港・坂の上）
```
chiptune, 16-bit, retro game soundtrack, instrumental, loopable, small seaside Japanese town, showa era nostalgia, shopping street, warm square wave melody, accordion-like synth, soft drums, 100 BPM, slightly faded but kind
```
- 0-1でDを選んだ場合は末尾に `showa kayo, mood kayo influence` を足す。

#### M15 夕暮れ（夜回りの前）
```
chiptune, 16-bit, retro game soundtrack, instrumental, loopable, sunset before night, calm and a little uneasy, slow triangle bass, distant square wave melody with echo, crickets feeling, 90 BPM, orange sky turning purple
```

### 1-3. 裏（夜）＝ハザマ

#### M20 境目（0時、ハザマへ入るジングル・約6秒）
```
chiptune, 16-bit, retro game sound, instrumental, short jingle, clock striking midnight, descending arpeggio, reverse cymbal, warm tones turning cold and dark synth, mysterious, 6 seconds
```
構成：`[Jingle] [End]`

#### M21 ハザマ（共通の探索曲）
共通の Style 先頭：
```
chiptune, 16-bit, retro game soundtrack, instrumental, loopable, dungeon exploration, dark synth and chiptune, mysterious arpeggios, a little lonely,
```

| 曲 | 階層（出身地と対応） | Style 後半 |
|---|---|---|
| M21a | シャッター街（商店街） | `abandoned shopping arcade at night, rattling metal percussion, detuned square lead, 110 BPM` |
| M21b | 水びたしの倉庫街（港町） | `flooded warehouse, dripping water sounds, slow wobbling bass, foghorn-like low synth, 100 BPM` |
| M21c | 坂と階段の迷路（坂の上） | `endless stairs maze, rising and falling arpeggios, staccato steps rhythm, 116 BPM, dizzy` |
| M21d | 裏返しの団地（団地育ち） | `inverted apartment complex, the home theme melody played backwards and in minor key, music box out of tune, 104 BPM, eerie but nostalgic` |
| M21e | 最深部・303の中（ハザマ生まれ／終章） | `deepest layer, the hidden room 303 of the shadow apartment complex, vast empty darkness, sparse neon-like high square pings, faint music box of the main theme, deep drone, 100 BPM, sad and sacred` |

構成：`[Intro] [Loop A] [Loop B] [Loop]`
- M21dは「団地のテーマの逆さま」なので、M10aをCoverして作るのがおすすめ。

#### M22 ひろいもの部屋・セーフルーム（休憩）
```
chiptune, 16-bit, retro game soundtrack, instrumental, loopable, safe room in a dark dungeon, small warm light, soft music box and triangle pad, slow 80 BPM, relief and comfort
```

### 1-4. 戦闘

#### M30 通常戦闘（カゲ）
```
chiptune, 16-bit, retro game soundtrack, instrumental, loopable, battle theme, fast and energetic, dark synth arpeggios with chiptune lead, driving noise drums, strong kick and snare, 150 BPM, catchy, a hint of sadness in the melody
```
構成：`[Intro: short hit] [Loop A] [Loop B] [Loop]`

#### M31 強いカゲ（中ボス）
```
chiptune, 16-bit, retro game soundtrack, instrumental, loopable, mini boss battle, tense, minor key, heavy pulsing bass, fast square wave riffs, 158 BPM, urgent
```

#### M32 ワスレモノ戦（章ボス）
```
chiptune, 16-bit, retro game soundtrack, instrumental, loopable, chapter boss battle, epic and emotional, someone's forgotten precious memory, dramatic chiptune lead, dark synth choir pad, pounding drums, 150 BPM, a sad music box motif in the bridge
```
構成：`[Intro: dramatic] [Battle A] [Battle B] [Bridge: music box, sad] [Loop]`
- ブリッジに「切ないオルゴール」を入れるのは、ボスがだれかの大事な忘れ物だから。

#### M33 れんけい発動（短いジングル・約4秒）
```
chiptune, 16-bit, retro game sound, instrumental, short jingle, team combo special attack, rising arpeggio, bright fanfare hit, 4 seconds
```

#### M34 勝利ジングル（約5秒）
```
chiptune, 16-bit, retro game sound, instrumental, short victory jingle, cheerful and a little silly, major key, 5 seconds
```

#### M35 全滅・朝になる（約6秒）
```
chiptune, 16-bit, retro game sound, instrumental, short game over jingle, gentle not scary, slow descending melody, ends with a soft morning bird-like chirp, 6 seconds
```
- 全滅は「朝になって団地に戻される」くらいのやさしさにする（残酷な表現はしない）。

### 1-5. 物語・感情

#### M40 切ない場面（303号室のテーマ・オルゴール版）
```
chiptune, 16-bit, retro game soundtrack, instrumental, loopable, sad emotional scene, slow music box and soft pulse wave piano, 70 BPM, bittersweet, gentle, remembering something lost
```
- M01をCoverして作る。

#### M41 ちょっといい話（あたたかい）
```
chiptune, 16-bit, retro game soundtrack, instrumental, loopable, heartwarming scene, soft electric piano and square wave melody, light strings pad, 84 BPM, kind and hopeful
```

#### M42 不気味・謎（ミオ・303号室の謎）
```
chiptune, 16-bit, retro game soundtrack, instrumental, loopable, mysterious scene, a girl who may not be real, thin high square wave melody, airy pad, slow 76 BPM, eerie but beautiful, not horror
```

#### M43 カゲモリのテーマ（若いころのサカキの影。主人公と顔が似ている）
```
chiptune, 16-bit, retro game soundtrack, instrumental, loopable, rival theme, shadow of the hero's grandfather when he was young, guardian of a hidden apartment complex, the home theme melody in a cold minor key, dark synth bass, ticking clock percussion, 120 BPM, lonely and proud
```

#### M44 入居決定（短いジングル・約5秒）
```
chiptune, 16-bit, retro game sound, instrumental, short jingle, new resident moves in, warm doorbell-like chime then happy fanfare, 5 seconds
```

#### M45 エンディング（303号室のテーマ・3種類）
エンディングは住人の数で3つに分かれる（ideas_story.md 12章）。同じメロディ（M01）をCoverして、エンドごとに音の厚みを変える。

| 曲 | エンド | Style |
|---|---|---|
| M45a | **みんなの部屋**（真）：全員そろう。303がにぎやかになり、サカキが管理人室に戻る | `chiptune, 16-bit, retro game soundtrack, instrumental, ending theme, the main theme in full, starts with solo music box, gradually adds all instruments, joyful full chiptune band with warm strings pad, celebratory and emotional, ends bright and peaceful, 96 BPM, 3 minutes` |
| M45b | **ただいま**（通常）：24部屋が埋まる。303は開くが少しさびしく、サカキはハザマに残る | `chiptune, 16-bit, retro game soundtrack, instrumental, ending theme, the main theme, warm square wave lead with soft electric piano, gentle and a little lonely, hopeful but quiet, a few instruments only, 88 BPM, 2 minutes 30 seconds` |
| M45c | **またいつか**（ほろ苦）：住人が少ない。303は一晩だけ開き、朝にはドアだけに戻る | `chiptune, 16-bit, retro game soundtrack, instrumental, ending theme, the main theme as a slow music box solo with faint triangle bass, bittersweet, a promise to meet again, morning birds at the very end, 72 BPM, 2 minutes` |

構成（共通）：`[Intro: music box] [Theme] [Theme: fuller] [Bridge] [Final Theme] [Outro: music box] [End]`
- M45cは「fuller」を入れず、最後までオルゴールと三角波だけにする。
- 0-4 B（歌あり）を選んだ場合は、M45aだけ歌ありにする案がおすすめ（Instrumentalをオフ、`instrumental` を `soft Japanese female vocal, gentle ballad` に差し替え）。

---

## 2. 効果音（ツール未定・汎用）

### 2-0. 書き方

- 各音に **英語の生成プロンプト**（生成AI用、0-5 A）と **作り方メモ**（jsfxr・ChipToneなど、0-5 B）を付けています。
- すべての英語プロンプトの先頭に、バイブル10章の共通前置きを付ける：
```
retro 16-bit game sound effect, square wave, triangle wave and noise, short, dry, no reverb
```
- 表の音（UI・会話・団地）は **丸くかわいく**（三角波・高め・やわらかい立ち上がり）、裏の音（戦闘・カゲ）は **少しにごらせる**（ノイズ・ビットクラッシュ・低め）。
- 書き出し：44.1kHz、モノラル、WAV（Godotでそのまま使う）。音量は −1dBを上限にそろえる。

### 2-1. UI（表）

| ID | 音 | 長さ | 英語プロンプト（前置きの後ろに付ける） | 作り方メモ |
|---|---|---|---|---|
| S01 | カーソル移動 | 0.05秒 | `tiny soft blip, cursor move, cute, high pitch triangle` | 三角波・高音・すぐ消える |
| S02 | 決定 | 0.15秒 | `bright two-note confirm, rising, round and cute` | 矩形波（50%）で2音上がる |
| S03 | キャンセル | 0.15秒 | `soft two-note cancel, falling, gentle` | 2音下がる |
| S04 | できない・ブブー | 0.2秒 | `low buzzy error, comedic, short` | 矩形波（12.5%）・低音 |
| S05 | ページめくり・回覧板 | 0.2秒 | `paper flip, quick noise swish, light` | ノイズの短いスイープ |
| S06 | 会話の文字送り（人） | 0.03秒 | `tiny talk blip, voice beep for text scrolling, cute` | 1文字ごと。キャラで高さを変える |
| S07 | 会話の文字送り（元カゲ） | 0.03秒 | `tiny talk blip, slightly warbly and hollow, cute but strange` | 少しビブラート |
| S08 | 回覧板が届く | 0.4秒 | `apartment intercom chime, ding-dong, retro, friendly` | ピンポン2音 |

### 2-2. 団地

| ID | 音 | 長さ | 英語プロンプト | 作り方メモ |
|---|---|---|---|---|
| S10 | 住人を部屋に置く | 0.2秒 | `soft pop, placing a piece on a board, satisfying` | 短いポップ |
| S11 | 住人を持ち上げる | 0.15秒 | `light lift up whoosh, cute` | 上がるスイープ |
| S12 | なかよし成立（1ライン） | 0.5秒 | `sparkle chime, line complete, happy rising arpeggio` | 3音のアルペジオ |
| S13 | れんけい成立（全部屋） | 0.8秒 | `big sparkle, full board complete, bright arpeggio with shimmer` | 5音＋キラキラ |
| S14 | 修繕（トンカチ） | 0.5秒 | `retro hammering, three quick knocks, comedic` | ノイズのコン×3 |
| S15 | 部屋が開く（修繕完了） | 0.8秒 | `door opening creak then bright jingle, new room unlocked` | きしみ＋ジングル |
| S16 | 内見に来る（ノック） | 0.3秒 | `two polite door knocks, wooden, retro` | ノイズのコンコン |
| S17 | 当たり部屋の抽選 | 0.8秒 | `lottery roulette ticking then ding, lucky` | 速いカチカチ→チーン |
| S18 | 家具を置く | 0.2秒 | `soft thud, placing furniture, cozy` | 低いトン |

### 2-3. ハザマ・探索（裏）

| ID | 音 | 長さ | 英語プロンプト | 作り方メモ |
|---|---|---|---|---|
| S20 | 境目が開く | 0.8秒 | `metal shutter rattling open then mysterious descending shimmer, slightly distorted` | ノイズのガラガラ＋下がるアルペジオ |
| S21 | 足音（ハザマ） | 0.05秒 | `soft footstep on concrete, dark, muffled` | 低いノイズ |
| S22 | 階段を下りる | 0.5秒 | `descending steps, four quick notes going down, dungeon` | 4音下がる |
| S23 | 宝箱をあける | 0.5秒 | `wooden box creak open, then sparkle` | きしみ＋キラ |
| S24 | ヒノカケラを拾う | 0.15秒 | `small glassy coin pickup, bright neon sparkle` | 高い2音 |
| S25 | ひろいもの（家具）を見つける | 0.4秒 | `item found, curious little fanfare` | 短いジングル |
| S26 | カゲに見つかる | 0.3秒 | `alert sting, short dissonant stab, bitcrushed` | 不協和音・ビットクラッシュ |
| S27 | 霧・ハザマの環境音（ループ） | 4秒 | `low airy drone, distant wind, faint neon hum, loopable ambience` | 長め。ループ用 |
| S28 | 夜明け・帰還 | 0.8秒 | `morning return, warm rising chime, birds chirp, relief` | 表の丸い音に戻す |

### 2-4. 戦闘（裏・少しにごらせる）

| ID | 音 | 長さ | 英語プロンプト | 作り方メモ |
|---|---|---|---|---|
| S30 | 通常攻撃（打つ） | 0.15秒 | `punchy hit, noise burst with low thump, slightly crunchy` | ノイズ＋低音 |
| S31 | 通常攻撃（ため） | 0.3秒 | `charge up, rising pitch whine, short` | 上がる矩形波（6章の「ため」1f目に合わせる） |
| S32 | 被弾 | 0.15秒 | `hurt, quick descending blip with noise` | 白フラッシュ1fと同時 |
| S33 | 会心・弱点 | 0.3秒 | `critical hit, sharp double impact, bright` | 2連打 |
| S34 | 防御・盾 | 0.2秒 | `metallic block, clang, short` | 金属っぽい矩形波 |
| S35 | 回復 | 0.5秒 | `healing, gentle rising arpeggio, soft and warm` | 緑の系統。やわらかい |
| S36 | 状態異常 | 0.4秒 | `status ailment, wobbling detuned tone, strange` | 紫の系統。ゆれる音 |
| S37 | カゲが消える（倒す） | 0.6秒 | `enemy dissolves, soft sad fade with sparkle, not violent` | 残酷にしない。さみしく消える |
| S38 | 味方ダウン | 0.4秒 | `ally down, comedic falling slide whistle, soft thud` | コミカルに |
| S39 | ワスレモノ登場 | 0.8秒 | `boss appears, deep rumble, distorted chord stab, dramatic` | 低いうなり＋和音 |

#### れんけい（系統ごと）
| ID | 系統 | 英語プロンプト |
|---|---|---|
| S40 | 赤（まんぷく） | `sizzling frying pan then powerful hit, appetizing, energetic` |
| S41 | 青（いしあたま） | `heavy stone thud then shield chime, solid` |
| S42 | 緑（おせっかい） | `soft chorus of chimes, warm healing wave` |
| S43 | 黄（まよなか） | `fast clock ticking then whoosh, speed burst` |
| S44 | 白（ものしり） | `book pages flutter then bright discovery ding` |
| S45 | 紫（うらがえし） | `reverse sound swell then flip, card turning, eerie` |

### 2-5. レア度の演出（4-3）

★が上がるほど **長く・高く・音が多く** する。★6だけ専用ファンファーレ。

| ID | ★ | 長さ | 英語プロンプト | 画面の揺れ（参考） |
|---|---|---|---|---|
| S51 | ★1 | 0.1秒 | `plain dull blip, item reveal, humble` | なし |
| S52 | ★2 | 0.2秒 | `simple clean ding, item reveal` | なし |
| S53 | ★3 | 0.3秒 | `pleasant two-note chime, item reveal, green sparkle` | なし |
| S54 | ★4 | 0.5秒 | `bright three-note arpeggio with shimmer, rare item reveal` | 小 |
| S55 | ★5 | 0.8秒 | `exciting rising arpeggio, sparkle burst, very rare item` | 中 |
| S56 | ★6 | 2.5秒 | `legendary fanfare, rainbow sparkle, triumphant chiptune brass-like square waves, drum roll then big hit` | 大＋虹の点滅 |
| S57 | ★6の前ぶれ | 1.0秒 | `suspense build, rising noise sweep, heartbeat` | ★6のときだけ、S56の前に鳴らす |

### 2-6. 物語用

| ID | 音 | 長さ | 英語プロンプト |
|---|---|---|---|
| S60 | 303のドアを開けたらすぐ壁 | 0.6秒 | `old door creak open, then a dull thud against concrete, comedic, short` |
| S65 | ドアの向こうに303号室ができる | 1.5秒 | `old door creaking open, soft whoosh of air from a new room, warm light swell, gentle magical chime` |
| S61 | 時計が0時を打つ | 2.0秒 | `old wall clock striking midnight, retro chiptune bell, slightly eerie` |
| S62 | 公衆電話・ダイヤル | 0.8秒 | `retro rotary phone dial clicks, nostalgic` |
| S63 | 街灯がつく（トモシビ） | 0.5秒 | `old street lamp flickering on, buzz then soft hum` |
| S64 | 思い出す（記憶が戻る） | 1.2秒 | `memory recall, reverse shimmer then gentle music box note` |

---

## 3. 映像（OP・イベント／ツール未定・汎用）

### 3-0. 書き方

- すべての英語プロンプトの先頭に、バイブル10章の共通前置きを付ける：
```
pixel art animation, 16-bit retro game cutscene, 12fps limited animation, 320x180 upscaled with nearest neighbor, no 3D, no realistic rendering
```
- さらに画像生成（キーフレーム）のときは、バイブル10章の画像用前置きも付ける。
- カメラは「固定」か「ゆっくりパン」だけ。ズーム・回転・手ぶれはしない。
- 色は表＝5-3「表」パレット、裏＝5-3「裏」パレット。**キャラの色は表でも裏でも同じ**。
- 1カット＝3〜8秒。動画AIは長いと絵がくずれるので、カットごとに作ってつなぐ。

### 3-1. OP「0時の303号室」（0-6 A・約75秒・音楽 M02）

| # | 秒 | 画面 | 英語プロンプト（前置きの後ろ） |
|---|---|---|---|
| 1 | 0–6 | 夕方の灯野市。海と山、遠くに団地。ゆっくり右へパン | `wide shot of a small Japanese seaside town at sunset, sea and mountains, old apartment complex on the outskirts, warm orange palette, slow pan right, birds flying` |
| 2 | 6–12 | 3階の外廊下。302と304のあいだの壁に、「303」の表札とドアだけがついている。住人がドアを開けると、すぐコンクリートの壁。「やっぱりね」と閉める。ドアのすき間に古い手紙が1通はさまっている | `3rd floor outdoor corridor of an old apartment complex, between doors 302 and 304 there is a door with a 303 nameplate set into the wall, a resident opens it and there is only a solid concrete wall right behind it, the resident shrugs and closes it, an old envelope tucked in the door gap, comedic, dusk light` |
| 3 | 12–18 | 主人公が、空き部屋になった管理人室の前をほうきで掃く。ほとんどの窓が暗い | `the young hero sweeping in front of an empty, unused caretaker office, run-down danchi building behind with only a few lit windows, comedic idle motion, sunset turning to evening` |
| 4 | 18–22 | 古い時計が0時。画面が一瞬止まる | `old wall clock hands reaching midnight, frame freezes, colors drain slightly` |
| 5 | 22–28 | 閉店したシャッターの隙間からネオン色の光がもれ、画面が左右にめくれて裏のパレットへ | `closed shop shutter in a dark shopping street, cyan and pink neon light leaking from the gap, the screen peels open left and right, warm palette swaps to cold purple palette with neon` |
| 6 | 28–36 | ハザマの全景。街を裏返した迷宮。カゲがうろつく | `underground labyrinth that looks like an upside-down version of the town, dark purple and blue, glowing neon fragments floating, small shadowy creatures wandering, slow downward pan` |
| 7 | 36–52 | 住人が1人ずつ見得を切る（2秒×8人）。ユズコ、ゲンゾウ、ミツキ、ポチタ、マネキチ、ニボシ、サキミキ、トメヨ | `quick character pose cut-in, [名前と見た目], dynamic comedic pose, name plate, cold neon background, character colors stay warm` |
| 8 | 52–60 | ワスレモノ（ボス）のシルエット。大きな影 | `giant silhouette of a boss made of forgotten things, glowing eyes, looming over the party, dramatic but not scary` |
| 9 | 60–66 | 霧の中、白いワンピースの少女（ミオ）がふり返る。輪郭が少し透ける | `girl in a white dress turning back in the mist, her outline slightly transparent, quiet moment` |
| 10 | 66–70 | 主人公と顔の似た影（カゲモリ＝若いころのサカキの影）が、裏返しの団地の屋上から見下ろす | `a shadow figure who looks like the hero (his grandfather's younger self), colored in cold neon palette, standing on the roof of an upside-down apartment complex, looking down, cold moonlight` |
| 11 | 70–75 | 夜明け、団地の前に全員集合。よく見ると3階だけ窓が1つ少ない → タイトルロゴ「おぼろ団地と303号室」 | `dawn, all residents gathered in front of the apartment complex, every window lit, but the 3rd floor has one window fewer than the other floors, nobody notices, the title logo appears with a sparkle: Japanese text おぼろ団地と303号室, the 303 part styled like an old apartment door nameplate` |

- カット7の [名前と見た目] は characters_30.md の「見た目（ドット絵用）」欄を英訳して入れる。
- 0-6 B／D を選んだ場合は、カット3を「真っ暗な団地の窓に1つずつ明かりが灯る」に差し替え、最後に「3階だけ窓が1つ少ない」ことに気づかせる。

### 3-2. 表→裏の切り替え（毎晩の夜回り・約3秒）

```
transition effect, the town screen peels open from the center to left and right like curtains, behind it the dark labyrinth appears, warm orange palette swaps to cold purple and neon palette, 3 seconds, loopable as a reusable transition
```
- Godotではシェーダー（パレット入れ替え）で作るのがおすすめ。この映像は見本として使う。
- 音：M20（境目ジングル）＋S20。

### 3-3. 章の区切り（303の手がかりカット・約6秒）

章の始まりに毎回、その章の「303の手がかり」（バイブル4章の章立て）を映す。

| 章 | 変化 | 英語プロンプト |
|---|---|---|
| 序章 | 空席の管理人室の机に、サカキの日誌 | `empty caretaker office, an old diary open on the desk with a line about room 303, a ring of keys, dusk light through the window, chapter title card` |
| 1章 | 303の表札とドア。開けるとすぐ壁 | `close-up of an old door with a 303 nameplate between doors 302 and 304, slightly open, solid concrete wall right behind it, chapter title card, dusk` |
| 2章 | 「灯野第三団地 303号室」あての古い手紙 | `close-up of an old envelope addressed to room 303 of Hino Daisan Danchi, held in a mail carrier's hand, in front of the 303 door, chapter title card, evening` |
| 3章 | 古い市報の団地の図面。真ん中に「みんなの部屋」 | `old faded city newsletter showing the apartment complex floor plan, the exact center room labeled as a shared room for everyone, chapter title card, night` |
| 4章 | ハザマ側の裏返しの団地にある303のドア。すき間から光 | `the 303 door in the upside-down shadow apartment complex, cold neon palette, warm light leaking from the gap under the door, chapter title card, midnight` |
| 終章 | 表の303のドアが開いている | `the 303 door between 302 and 304 standing open, a dim room visible beyond it, soft cyan glow, chapter title card, dawn` |

### 3-4. 入居イベント（約4秒・音楽 M44）

```
new resident moving in, character walks up to the apartment door with a small bag, door opens, warm light spills out, the window of that room lights up, cozy and happy, 4 seconds
```
- 元カゲの住人のとき：`a former shadow creature shaped like [もとの物], neon accent inside its outline, shyly entering` を足す。

### 3-5. ワスレモノ登場（章ボス・約6秒・音楽 M32／S39）

```
boss entrance, the floor of the labyrinth ripples, forgotten objects ([その章の忘れ物]) swirl together and form a giant creature, glowing neon eyes open, screen shakes slightly, dramatic but bittersweet, not gory, not horror
```

### 3-6. ★6を引いたとき（約2.5秒・S57→S56）

```
legendary item reveal, screen darkens, a single light falls, burst of rainbow sparkles cycling cyan pink and yellow, item silhouette appears then reveals, triumphant
```

### 3-8. 303号室ができる（終章の始まり・約8秒・音楽 M01フル／S65）

修繕がすべて終わった日の夕方。住人たちは「303は開けても壁」だと知っている。

| # | 画面 | 英語プロンプト |
|---|---|---|
| 1 | 最後の修繕が終わり、全部の窓に明かり | `the last renovation finished, every window of the apartment complex lit, dusk` |
| 2 | 主人公がいつものように303のドアを開けると、壁がなく、奥に部屋が続いている | `the young hero opens the 303 door expecting a wall, but instead a dim room stretches beyond it, soft cyan glow, gentle and mysterious` |
| 3 | 302と304の住人が顔を出し、二度見する | `residents of 302 and 304 peek out of their doors and do a comedic double take at the open 303 door` |

### 3-7. エンディング（3種類・音楽 M45a／b／c）

3つのエンドで、カットの並びは同じにして中身だけ変える（作る枚数を減らすため）。

| # | 共通の画面 | みんなの部屋（M45a） | ただいま（M45b） | またいつか（M45c） |
|---|---|---|---|---|
| 1 | 夜明けの団地 | `dawn over the apartment complex, every window lit including a new one on the 3rd floor, warm palette, slow pan up` | `dawn over the apartment complex, most windows lit, warm palette, slow pan up` | `late night over the apartment complex, only a few windows lit, one small light glowing on the 3rd floor, slow pan up` |
| 2 | 303号室の中 | `inside room 303, crowded and lively, all residents sharing food and laughing, a girl in a white dress (Mio) smiling in the middle, cozy and bright` | `inside room 303, the door open, a girl in a white dress (Mio) smiling, a few residents with her, the room still a little empty, soft warm light` | `inside room 303 at night, a few residents and a girl in a white dress (Mio) sitting together by a single lamp, quiet and warm` |
| 3 | 手紙 | `undelivered letters fly out of room 303 like glowing birds and land in every resident's hands, sparkle` | `undelivered letters fly out of room 303 like glowing birds, a few drift back inside, sparkle` | `a single undelivered letter glows and floats out the window into the night sky` |
| 4 | サカキ | `an old man (Sakaki, the former caretaker) walks back into the caretaker office and switches on the light, the hero greets him, warm reunion` | `an old man (Sakaki) stands at the edge of the underground labyrinth, waves goodbye with a smile, then turns back into the mist` | `an old man's silhouette (Sakaki) seen faintly through the mist of the labyrinth, he doesn't turn around` |
| 5 | 住人の「その後」（各3秒） | `epilogue vignette, [名前] in their room doing their favorite thing, cozy, warm` | 同じ | 同じ（人数が少ない） |
| 6 | しめのカット | `group photo in front of the apartment complex, everyone including Sakaki and Mio, camera flash, freeze frame, the end` | `group photo in front of the apartment complex, the hero and residents, Mio in the center, camera flash, freeze frame, the end` | `morning, the hero opens the 303 door and there is only a wall again, smiles softly, a calendar with one night circled, freeze frame, see you again` |

- エピローグ（5番）は住人ごとに1枚絵＋一言。なかよし度が高い住人は特別版の絵にする（ideas_story.md 12章）。
- 「みんなの部屋」だけ、団地の名前が「おぼろ」でなくなる演出（街の人が名前を思い出す）を6番の前に入れてもよい：`townspeople looking at the apartment complex and suddenly remembering its name, the faded name painted on the building becomes clear and readable`

---

## 4. 映像の後処理（動画AIを使うとき・0-7 B／C）

動画AIの出力もピクセルの大きさがバラバラなので、バイブル11章と同じ考えで直す。

1. 320×180にニアレストネイバーで縮小し、12fpsに落とす
2. 5-3のパレットに減色（表のカットは表パレット、裏のカットは裏パレット）
3. 1920×1080へ6倍で拡大

ffmpegでの例（palette.png はバイブル11章と同じもの）：
```
ffmpeg -i input.mp4 -i palette.png -filter_complex "fps=12,scale=320:180:flags=neighbor[s];[s][1:v]paletteuse=dither=none,scale=1920:1080:flags=neighbor" output.mp4
```

---

## 5. 決定の一覧（バイブル7章・8章への追記用）

| 項目 | 決定 |
|---|---|
| BGMの時代感 | スーファミ寄り16bit（チップ音色＋エレピ・ストリングス・オルゴールを少し） |
| メインテーマ | 「303号室のテーマ」1本を、OP・団地・切ない場面・エンディングでアレンジ違いで使う。303号室が現れる場面で初めてフルで鳴る |
| 団地のBGM | 同じ曲で3段階（序盤＝ソロ、中盤＝楽器が増える、終盤＝にぎやか） |
| エンディング曲 | 歌なし。エンディング3種（みんなの部屋／ただいま／またいつか）で同じメロディの厚みを変える |
| 効果音 | 文章プロンプトで生成AIに作らせ、足りない分をレトロ効果音メーカー（jsfxrなど）で補う |
| OP | 「0時の303号室」：夕方の団地 → 303のドアを開けるとすぐ壁 → 0時 → ハザマ → 住人の登場 → タイトル |
| 映像の作り方 | Geminiでカットごとの1枚絵を作り、Godotの中で動かす |

## 6. 作る順番（おすすめ）

メロディと音の明るさをそろえるため、元になる曲から作る。

1. **M01 303号室のテーマ**（Suno）：何回か生成して、覚えやすいメロディを1つ選ぶ。これが全体の基準になる。
2. M01をCoverして **M40（オルゴール版）・M45a／b／c（エンディング）** を作る。
3. **M10a 団地（序盤）** を作り、Coverして **M10b・M10c**、さらに逆さま・短調にして **M21d（裏返しの団地）**。
4. **M30 通常戦闘** を作り、音の明るさ・音量をM01とそろえる。ここまでで、序章が遊べる分の曲がそろう。
5. 残りのBGMとジングル（M20・M33・M34・M35・M44）。
6. 効果音は、序章で必ず鳴る **2-1 UI・2-2 団地・2-4 戦闘の基本（S30〜S38）・2-5 レア度** を先に作る。
7. 映像は **3-2 表→裏の切り替え** をGodotのシェーダーで先に作り、OPは住人の絵がそろってから。
