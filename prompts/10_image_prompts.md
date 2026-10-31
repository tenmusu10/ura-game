# 画像・モーション プロンプト集（Gemini用）v0.2

> 土台は 00_world_bible.md（v1.2）。試しに手で描いたドット絵は ura-game/preview/ にあります。サイズ・色・描き方・モーションのフレーム数はすべてバイブルの5章・6章に従います。
> プロンプト本文は英語（Geminiが安定するため）、説明は日本語です。`{ }` の部分を差し替えて使います。

---

## 0. 先に選んでほしいこと（方向性）

ここだけ選べば、残りのプロンプトはそのまま使えます。★はおすすめ。

### 0-1. 同じキャラを何枚も描くときの作り方

| 案 | やり方 | 良い点 | 弱い点 |
|---|---|---|---|
| **A ★** | 先に「設定画（正面・背面・横＋バストアップ）」を1枚作り、以降のモーションは毎回その画像を添付して描かせる | 顔や色がいちばんぶれない | 1キャラにつき1手間多い |
| B | モーション1種類ずつ、文章だけで毎回描かせる | 速い | キャラが毎回少しずつ別人になる |
| C | 全モーションを1枚の大きなシートに一気に描かせる | 1回で済む | コマが多すぎて崩れやすい。手直しが多い |

### 0-2. 背景色（あとで透過にする色）

| 案 | 色 | メモ |
|---|---|---|
| **A ★** | マゼンタ #FF00FF | パレットに無い色なので抜きやすい。★5ピンク #FF5FA2 とは十分離れている |
| B | 緑 #00FF00 | 定番だが、緑系統の色 #4E8C4A・#7DBF6E や水色 #4FF2E0 と近く、抜けすぎることがある |
| C | 白 #FFFFFF | Geminiが一番素直に出すが、白い服（ミオ）や★2の白と混ざる |

### 0-3. 生成時の大きさ（Geminiは小さい画像を正確に出せないため）

| 案 | やり方 |
|---|---|
| **A ★** | 1ドット＝8×8の大きさで描かせる（24×32のキャラなら 192×256 の枠）。後でニアレストネイバーで1/8に縮小 |
| B | 大きさは指定せず、後処理で無理やり24×32に縮める | 手直しが増える |

### 0-4. 主人公の見た目（バイブルで主人公は未決定）

**保留**：主人公は管理人ではなく「31人目の住人」で、名前はプレイヤーが付けます（2026-10-31）。主人公は行方不明の先代管理人サカキ（#28）の孫です。見た目は「主人公とストーリー章立てを決める」スレッドで決まりしだい、2-4に英文を入れます。

---

## 1. 共通の前置き

### 1-1. 全素材に付ける（バイブル10章のまま）

```
16-bit pixel art, retro JRPG style, limited palette, 1px dark purple outline (#1B1626), flat shading with at most 2 shadow tones, light from top-left, no anti-aliasing, no gradients, clean readable silhouette, cute 2.5-head-tall chibi proportions, nostalgic run-down Japanese public housing complex (danchi) in a small seaside town meets mysterious underground labyrinth, comedic but slightly bittersweet mood
```

### 1-2. キャラ・カゲ・アイコン（透過したい素材）に足す

```
single character only, centered, full body visible, solid flat magenta background (#FF00FF) with no shadow on the ground, no text, no watermark, no border, crisp square pixels, every pixel drawn as an 8x8 block on a strict pixel grid
```

### 1-3. 背景に足す

```
background art only, no characters, 16:9 composition (320x180 game screen), tile-based look built from 16x16 tiles, subtle dithering allowed only in the sky and fog, every pixel drawn as a 6x6 block on a strict pixel grid
```

### 1-4. 毎回の最後に足す「やめてほしいこと」

Geminiには否定の欄が無いので、文の最後に入れます。

```
Avoid: blurry edges, soft gradients, anti-aliasing, painterly texture, 3D render, realistic proportions, black outlines (use #1B1626), text or letters, extra limbs, cropped body.
```

### 1-5. 色を守らせる一文

表（昼）の素材：
```
Use only these colors: #1B1626, #FCE3C6, #F2B98A, #C97F5A, #F27D52, #FFC857, #8C6E5D, #BFA08A, #E8D6C0, #6FB7D9, #3F7FA6, #7DBF6E, #4E8C4A, #F4F1F8, #9A97B0.
```
裏（ハザマ）の背景：
```
Use only these colors: #1B1626, #120F1F, #241C3A, #3A2D5C, #4B4A7A, #6B6FA3, #8FA3C7, #4FF2E0, #FF5FA2, #FFE66B, #7A5FB8, #B07CD9.
```
キャラは表でも裏でも同じ色（バイブル5-3）なので、キャラには常に表の一文を使い、必要な色（ネオン1色など）だけ足します。

---

## 2. キャラクター

### 2-1. 設定画（0-1 案A の最初の1枚）

```
{1-1 共通}
Character reference sheet for a game sprite. Subject: {見た目の英文（2-4の表）}.
Show the same character 4 times in a row, evenly spaced, same size: front view, back view, side view facing right, and a 64x64 bust-up portrait with a neutral face. Field sprite size 24x32 pixels (drawn at 8x scale, each view in a 192x256 area).
Eyes are 2-pixel tall vertical lines, mouth is a 1-pixel line, expression shown with eyebrows and mouth.
{1-2 透過用} {1-5 表の色} {1-4 やめてほしいこと}
```

### 2-2. 会話用バストアップ（64×64、表情セット）

設定画を添付して使います。

```
{1-1 共通}
Using the attached character as the exact reference (same face, hair, colors, clothes), draw a 64x64 pixel bust-up portrait set for dialogue, drawn at 8x scale. 6 expressions in a 3x2 grid, same framing and size in every cell: neutral, happy laughing, angry, sad, surprised, embarrassed with a sweat drop.
Comedic, exaggerated expressions using eyebrows and mouth only.
{1-2 透過用} {1-5 表の色} {1-4}
```

### 2-3. 元カゲの住人に足す一文

```
This resident is a former Kage: a forgotten object that came alive. Keep the clear shape of the original object ({もとの物}). Inside the outline, add exactly one neon accent color ({#4FF2E0 / #FF5FA2 / #FFE66B のどれか1つ}) as a thin glowing seam, so it reads as "from the other side". Cute, not scary.
```

### 2-4. 見た目の英文（全員分）

2-1〜2-2の `{見た目の英文}` に入れます。元カゲ（★印）は2-3も足します。ネオン色は3色が3人ずつになるように割り振りました（たたき台）。characters_30.md 第2版に対応。

**主人公（31人目の住人・見た目は保留）**

| 案 | 英文 |
|---|---|
| 未定 | {ストーリーのスレッドで決まった見た目を英文で入れる}, the grandchild of the former caretaker Sakaki: share one small family resemblance with him (for example the same eyebrow shape or a hand-me-down cardigan). 名前はプレイヤーが付けるため、名札などに文字は描かない |

**住人30人**

| # | 名前 | 英文 | 元カゲのネオン |
|---|---|---|---|
| 1 | ユズコ | a cheerful woman in her 20s, triangle headscarf, apron, holding a ladle | |
| 2 | ゲンゾウ | a big old man with white hair, work overalls, yellow hard hat, arms crossed, stubborn face | |
| 3 | ミツキ | a late-teen student in a hoodie, headphones around the neck, dark circles under the eyes | |
| 4 | トメヨ | a tiny old lady in a white kappogi apron, round glasses, holding a teacup | |
| 5 | ポチタ ★ | a small black fuzzy shadow shaped like a stuffed puppy, one ear missing, a red collar | #FF5FA2 |
| 6 | マネキチ ★ | a one-armed store mannequin in a business suit, painted-on eyebrows, stiff pose | #4FF2E0 |
| 7 | フミオ | a man in his 30s in an old-fashioned post office uniform and cap, big leather mail bag, holding one undelivered letter | |
| 8 | ニボシ | a fat orange tabby cat with a white tail tip, smug face | |
| 9 | サキミキ | twin elementary school kids side by side, yellow school hats, randoseru backpacks, one twin wears an eyepatch | |
| 10 | ミオ | a pale girl in a plain white dress, the edges of her outline slightly see-through, a lonely but gentle smile | |
| 11 | カサジロウ ★ | a cheap clear vinyl umbrella with broken ribs, the handle is its face | #4FF2E0 |
| 12 | カタッポ ★ | a single red knitted wool glove walking on its fingers | #4FF2E0 |
| 13 | ペンタ | a small penguin with an aquarium lost-child tag around its neck, holding a shiny trinket in its beak | |
| 14 | カナエ | a high school girl in a red movie theater usher vest and cap, holding a popcorn cup | |
| 15 | ゴウダ | a former delinquent with a pompadour, belly warmer (haramaki), towel over the shoulder | |
| 16 | シズカ | a librarian with long black hair, cardigan, carrying a tall stack of books | |
| 17 | リョウ | a struggling band guy in a leather jacket, guitar case on the back | |
| 18 | ジハンキ ★ | an old vending machine with stubby legs, its buttons are the eyes | #FF5FA2 |
| 19 | チヨノ | a middle-aged woman in a flower-pattern apron, holding a watering can | |
| 20 | キナコ | a woman in her 30s with a candy shop (dagashi-ya) apron, hair in a bun, holding a ramune bottle | |
| 21 | ボンボン ★ | an old stopped pendulum wall clock with little legs, the pendulum swings like a tail | #FFE66B |
| 22 | レイジ | a night-shift security guard, uniform cap, flashlight, a bread roll for a late snack | |
| 23 | マワリ ★ | an old clipboard-style neighborhood notice board (kairanban) hanging from a string, walking | #FFE66B |
| 24 | ミチノスケ | a thin man in his 60s, old station master cap, pocket watch on a chain, white gloves | |
| 25 | ミナト | a suntanned young ex-fisherman, rubber boots, holding a harpoon | |
| 26 | ヒナコ ★ | a hina doll girl in a slightly faded twelve-layered kimono | #FF5FA2 |
| 27 | ユメミ | a woman in her 30s, beret, ink-stained hands, holding a pen | |
| 28 | サカキ | the former caretaker, an old man with white hair, worn cardigan, big ring of keys | |
| 29 | トモシビ ★ | an old street lamp from the danchi entrance, the light bulb is its face and flickers | #FFE66B |
| 30 | カゲモリ | the shadow of Sakaki (#28) as a young man: a young caretaker with the same face shape and eyebrows as the protagonist (his grandchild), worn cardigan, a ring of keys, colored only with the night palette (#241C3A, #3A2D5C, #7A5FB8, #B07CD9, neon #4FF2E0 eyes) | （全身が裏の色） |

※30 カゲモリは「主人公の設定画」と「サカキの設定画」の2枚を添付し、「顔立ちは主人公、服と鍵束はサカキ、年は若く、色だけ裏のパレット」と頼むと、血のつながりが出ます。

---

## 3. モーション（スプライトシート）

### 3-1. 作り方

- 設定画（2-1）を必ず添付する（0-1 案A）。
- Geminiは横に長すぎる画像が苦手なので、**格子（グリッド）で描かせて、後で横一列に並べ直します**（7章のコマンド）。
- 向きは下・上・横の3方向。左は横を反転して作る（バイブル6章）。1回の生成で1モーション×1方向。

### 3-2. モーション共通の型

```
{1-1 共通}
Sprite animation sheet. Using the attached character as the exact reference (same proportions, face, colors, outline), draw the "{モーション名}" animation facing {down (toward the viewer) / up (away from the viewer) / right (side view)}.
{コマ数} frames arranged in a {格子} grid, read left to right, top to bottom. Every cell is exactly the same size (192x256, the 24x32 sprite at 8x scale), the character stays in the same position in every cell with feet on the same baseline, nothing crosses the cell borders.
{各コマの説明（3-3の表）}
Comical, exaggerated timing: strong anticipation, 1-frame squash on landing.
{1-2 透過用} {1-5 表の色} {1-4}
```

### 3-3. 各モーションの差し込み文

| モーション | コマ・格子 | 各コマの説明（英文） |
|---|---|---|
| 待機 | 4コマ・2×2 | `Frame 1: standing relaxed. Frame 2: body 1 pixel lower (breathing in). Frame 3: same as frame 1. Frame 4: body 1 pixel higher (breathing out). Only the body moves, feet stay planted.` |
| 歩き | 6コマ・3×2 | `A 6-frame walk cycle: contact (left foot forward), down, pass, contact (right foot forward), down, pass. Arms swing opposite to legs. Head bobs 1 pixel.` |
| 走り | 6コマ・3×2 | `A 6-frame run cycle, leaning forward, longer strides than walking, one frame with both feet off the ground, arms pumping, hair and clothes trailing behind.` |
| 攻撃 | 5コマ・3×2（最後の1マスは空ける） | `Frame 1: wind-up, pulling back the {武器・道具} with a big anticipation pose. Frame 2: fast swing, body stretched forward. Frame 3: follow-through with a 1-color afterimage smear of the swing. Frames 4-5: returning to the ready pose. Leave the 6th cell empty.` |
| 被弾 | 2コマ・2×1 | `Frame 1: the whole character flashed pure white (#F4F1F8 silhouette with #1B1626 outline). Frame 2: hurt face, knocked back 1 pixel away from the attacker.` |
| ダウン | 4コマ・2×2 | `Frame 1: stagger with a dizzy face. Frame 2: knees buckle. Frame 3: falling over. Frame 4: lying flat on the ground with swirly comedic eyes (not violent, no blood).` |
| 喜び | 4コマ・2×2 | `Frame 1: crouch to prepare a jump (squash). Frame 2: jumping up with arms raised and a big smile. Frame 3: peak of the jump. Frame 4: landing with a 1-frame squash.` |

`{武器・道具}` はキャラの持ち物（おたま、ヘルメットで頭突き、懐中電灯、ギター、銛…）。元カゲは体ごと体当たり、でOKです。

### 3-4. 戦闘用の構え（任意・大きめ）

戦闘画面でキャラを大きく見せたい場合の追加案です（バイブルに無いサイズなので、使うならバイブルに追記が必要）。

```
{1-1 共通}
Battle stance sprite, 48x48 pixels drawn at 8x scale, three-quarter view facing left toward the enemy, using the attached character as the exact reference.
{1-2} {1-5} {1-4}
```

---

## 4. カゲ（雑魚 32×32）とワスレモノ（ボス 64〜96）

### 4-1. 雑魚カゲの型

```
{1-1 共通}
Enemy sprite for a dungeon RPG, 32x32 pixels drawn at 8x scale (256x256). A "Kage": a forgotten thing that became a lonely, grumpy shadow creature. Subject: {カゲの英文}.
Body colored with #7A5FB8 and #B07CD9, with one neon glow color ({#4FF2E0 / #FF5FA2 / #FFE66B}) for the eyes and cracks. Eerie and a little sad, but cute rather than scary. No gore.
{1-2} {1-4}
```

カゲの色替え（同じ形で強い版）は、生成した画像を添付して「体色だけ変えて」と頼みます：
```
Recolor the attached enemy only: change the body colors to {#3A2D5C and #6B6FA3} and the glow to {#FF5FA2}. Keep every pixel position the same.
```

### 4-2. 雑魚カゲのたたき台（階層ごと・各3体）

バイブルの出身地＝階層に合わせました。名前は仮です。

| 階層 | カゲ | 英文 |
|---|---|---|
| シャッター街 | シャッターガエル | a frog-like creature made of a rusty rolled-down shop shutter, its mouth is the shutter slot |
| | ポイントカード | a flock of expired stamp cards flapping like bats |
| | フクビキ | a lottery drum (garapon) that spits out blank balls |
| 水びたしの倉庫街 | ナガレブイ | a lost fishing buoy with a single eye, bobbing |
| | ニモツ | a soggy cardboard box with a crab claw sticking out |
| | アミモドキ | a tangled fishing net shaped like a jellyfish |
| 坂と階段の迷路 | テスリ | a long wobbly handrail snake |
| | ジテンシャ | an abandoned bicycle that rides itself downhill |
| | ポスト | a stray old red postbox that bites with its slot |
| 団地を裏返した階層 | ベランダ | a hanging laundry ghost made of forgotten clothes on a pole |
| | ゴミブクロ | a ghostly garbage bag left out on the wrong day |
| | ドアスコープ | a peephole eye floating inside an apartment door frame |
| 最深部 | ナマエナシ | a blank name tag floating with a sad face |
| | ヘヤフダ | a stray apartment door number plate with no number, crawling like a spider |
| | ワスレガオ | a smooth faceless shadow person, only neon eyes |

### 4-3. ワスレモノ（章ボス）の型

章のストーリーが未決定なので型だけ置きます。章が決まったら `{ }` を埋めます。

```
{1-1 共通}
Boss enemy sprite, {64x64 / 96x96} pixels drawn at {8x / 6x} scale. A "Wasuremono": a huge, important thing that someone in town forgot, now a giant shadow. Subject: {ボスの英文}, connected to the resident {関係する住人} who lost it.
Imposing silhouette that fills the frame, body #3A2D5C/#7A5FB8/#B07CD9 with neon #4FF2E0, #FF5FA2 and #FFE66B details, a faint glow around the outline. Melancholic and grand, not grotesque.
{1-2} {1-4}
```

例（たたき台）：閉館した図書館の本が積み重なった巨人（シズカ）、海に消えた漁船（ミナト）、届かなかった手紙の山（フミオ）。

---

## 5. 背景（320×180）

### 5-1. 型

```
{1-1 共通}
{1-3 背景用}
Scene: {場面の英文}.
{1-5 表 または 裏の色}
{1-4}
```

### 5-2. 場面の英文

**表（昼の灯野市）**

| 場面 | 英文 |
|---|---|
| おぼろ団地（灯野第三団地）・外観（序盤） | a small, run-down 2-story concrete danchi apartment building at the edge of a seaside town, most windows dark and boarded, rain stains on the walls, overgrown weeds, an old street lamp at the entrance, late afternoon light |
| 団地の看板（灯野第三団地） | close-up of a faded old signboard at the danchi entrance, peeling paint, rust stains, weeds at the base（※文字は後で手描きで入れる。Geminiに文字を描かせない） |
| 3階の廊下（表・重要） | the 3rd-floor outdoor corridor of an old danchi, a row of steel apartment doors with small number plates, the door in the middle looks exactly like the others but has no window beside it and no meter box, slightly too clean, late afternoon light, quietly uncanny（※番号と表札は後で手描き。真ん中を「303」にする） |
| 303のドアを開けると（表・重要） | close-up of that middle apartment door swung open, and right behind the door frame there is only a flat concrete wall, no room at all, a cold draft of dust, comedic but eerie |
| 集合ポスト（表・重要） | a row of old metal mailboxes on the danchi ground floor, one mailbox in the middle of the 3rd-floor row has a slot that is taped shut and dusty, as if it belongs to a room nobody has seen（※ポストの番号は後で手描き。テープの箱を「303」にする） |
| 団地の図面（管理人室・重要） | an old yellowed architectural floor plan of a danchi pinned on a corkboard, a 5x5 grid of rooms, the room in the very center is drawn and circled in faded red pencil（※部屋番号は後で手描き） |
| 303号室が現れる（終章・表） | the same open door as the attached image, but now behind it there is a real room: a cozy shared common room for all the residents, a big low table, mismatched cushions, old photos and keepsakes on the shelves, warm light, morning（※「303のドアを開けると」を添付して描き替える） |
| 303号室（ハザマ側・重要） | inside the inside-out underground copy of the danchi, the room behind door 303 that only exists on this side: a dim, dusty common room with a long low table, faded cushions in a circle, a forgotten party banner, everything tinted in night colors with faint neon #4FF2E0 dust in the air, lonely and quiet |
| 団地・外観（終盤） | the same danchi grown to 5 floors, most windows lit warmly, laundry on balconies, flowers in pots, evening |
| 管理人室（だれもいない・メニュー背景） | a cramped caretaker's office inside a danchi, left empty: a desk with a black rotary phone and an open old diary, an empty chair pushed back, a ring of keys still on its hook, a corkboard with yellowed notices, a small TV, dust in a beam of light, nobody in the room |
| 団地の部屋（空き室） | an empty old Japanese apartment room, tatami floor, sliding paper doors, a leaking ceiling stain, a single bare light bulb |
| 商店街 | a quiet shopping arcade (shotengai) with half the shutters closed, a dagashi candy shop still open, paper lanterns, a public phone booth |
| 港 | a small fishing port at sunset, old boats, stacked crates, seagulls, a rusty crane |
| 坂の上 | a steep hillside neighborhood with long stone stairs, old houses, a view of the sea far below |

**裏（ハザマ）**

| 階層 | 英文 |
|---|---|
| 境目（入口） | a closed shop shutter at midnight with a thin glowing neon seam in the middle, as if the world is about to flip inside out |
| シャッター街の階層 | an upside-down underground version of a shopping arcade, shutters on the ceiling and floor, floating price tags, neon signs flickering in cold colors, fog |
| 水びたしの倉庫街の階層 | flooded warehouses underground, knee-deep dark water reflecting neon, floating crates and buoys |
| 坂と階段の迷路の階層 | impossible stairs going in every direction like a maze, handrails twisting, doors on walls |
| 団地を裏返した階層 | an inverted danchi corridor, apartment doors in endless rows, balconies hanging downward, laundry floating |
| 最深部 | a vast dark void with a floating copy of the danchi lit in neon, countless closed apartment doors drifting like stars |

### 5-3. タイル（16×16）

```
{1-1 共通}
Top-down 16x16 tileset for a dungeon RPG, drawn at 8x scale, arranged in a 4x4 grid of 16 tiles with clear borders: {floor, floor variant, wall top, wall front, corner pieces, door, stairs down, treasure chest closed/open, puddle, crack, neon fragment pickup}.
Theme: {階層の英文}. Tiles must connect seamlessly.
{1-5 裏の色} {1-4}
```

---

## 6. UI

### 6-1. アイコン（16×16：ひろいもの・アイテム）

```
{1-1 共通}
Item icon, 16x16 pixels drawn at 16x scale (256x256), single object centered: {物の英文}. Readable at tiny size, thick silhouette, 1px #1B1626 outline.
{1-2} {1-5 表の色} {1-4}
```
例：ヒノカケラ＝`a small glowing crystal shard, neon #4FF2E0 core with #FFE66B sparkle`／うらがえし札＝`a paper charm card, front warm, back side showing night colors`／家具＝`a small low wooden chabudai table`、`a potted window-side plant` など。

★の光（外側の光）はGeminiに描かせず、Godotのシェーダーか枠画像で後から付けるのがおすすめです（★6の虹の点滅もそちらで）。

### 6-2. こせい札（8×8・系統6色）

8×8は小さすぎてGeminiでは崩れるので、**形だけ作って色は手で塗る** がおすすめです。

```
{1-1 共通}
A set of 6 tiny badge icons, each 8x8 pixels drawn at 32x scale, in a 3x2 grid, same rounded tag shape with a different simple symbol inside: a rice bowl (red group), a shield (blue group), a heart with a leaf (green group), a crescent moon (yellow group), a magnifying glass (white group), a curled cat tail (purple group). Fill colors: #F27D52, #3F7FA6, #4E8C4A, #FFC857, #E8D6C0, #7A5FB8.
{1-2} {1-4}
```

### 6-3. ウィンドウ枠・メニュー

```
{1-1 共通}
UI kit for a retro JRPG, drawn at 6x scale: a dialogue window frame designed like a neighborhood notice board (kairanban) with a clipboard clip on top, a smaller menu window, a selection cursor shaped like a small key, and a name plate. Frames made of 9-slice friendly corners and edges. Warm paper color #E8D6C0 with #8C6E5D wood edges and #1B1626 outline.
{1-2} {1-4}
```
裏（夜回り中）用は同じ型で `dark paper #241C3A with #6B6FA3 edges and a thin neon #4FF2E0 line` に差し替え。

### 6-4. 団地の部屋マス（編成画面）

```
{1-1 共通}
UI tiles for a 5x5 apartment grid screen, drawn at 6x scale: one apartment window cell in 6 states arranged in a row — a cell with no window, only a single closed apartment door standing on a plain wall (the door-only room 303, shown from the 3x3 stage on; different from the broken rooms), locked and broken (boarded window, cracks), repaired and empty (dark window), occupied (warm lit window with curtains), lucky room (lit with a small festive paper ornament), selected for the night patrol (window outlined in neon #4FF2E0).
{1-2} {1-5 表の色} {1-4}
```

---

## 7. 後処理（バイブル11章に追加する手順の案）

格子で描かせたシートを、横一列のスプライトシートにする例（6コマ・3×2・24×32）：

```
magick sheet.png -fuzz 10% -transparent "#FF00FF" -crop 3x2@ +repage -filter point -resize 24x32! +append +dither -remap palette.png walk_down.png
```

- 5コマ（攻撃）のときは、最後の空きマスを捨ててから `+append` する。
- 背景（6倍で描かせたもの）：`magick bg.png -filter point -resize 320x180! +dither -remap palette.png bg_out.png`
- 縮小後に、目（縦2px）と輪郭（1px）だけ Aseprite で直す。

---

## 8. 作る順番（おすすめ）

1. 主人公とユズコの設定画 → 待機・歩き（絵柄の基準を決める）
2. 団地外観・3階の廊下・集合ポスト・団地の図面・管理人室（物語の顔）
3. 雑魚カゲ1階層ぶん＋ハザマ背景1つ（夜回りが1回遊べる量）
4. UIの枠とアイコン
5. 残りの住人を★の高い順に
