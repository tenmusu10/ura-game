from PIL import Image, ImageDraw, ImageFont
import os
OUT = os.path.dirname(os.path.abspath(__file__)) + "/"
os.makedirs(OUT, exist_ok=True)

def hx(h): h=h.lstrip('#'); return (int(h[0:2],16),int(h[2:4],16),int(h[4:6],16),255)
OL=hx('1B1626')
C = {
 'O':OL,'S':hx('FCE3C6'),'s':hx('F2B98A'),'k':hx('C97F5A'),
 'h':hx('8C6E5D'),'W':hx('F4F1F8'),'w':hx('E8D6C0'),
 'F':hx('F27D52'),'f':hx('C97F5A'),'A':hx('E8D6C0'),'a':hx('BFA08A'),
 'L':hx('9A97B0'),'B':hx('8C6E5D'),'.':(0,0,0,0),
}

def from_rows(rows, w, h):
    im = Image.new('RGBA',(w,h),(0,0,0,0))
    for y,r in enumerate(rows):
        r = r.ljust(w,'.')[:w]
        for x,ch in enumerate(r):
            if ch!='.': im.putpixel((x,y),C[ch])
    return im

def up(im, k): return im.resize((im.width*k, im.height*k), Image.NEAREST)

# ---------- ユズコ 24x32 ----------
yuzu = [
"........................",
"........OOOOOOOO........",
"......OOWWWWWWWWOO......",
".....OWWWWWWWWWWWwO.....",
"....OWWWWWWWWWWWWwwO....",
"....OhhhhhhhhhhhhhhO....",
"...OhhSSSSSSSSSSSShhO...",
"...OhSSSSSSSSSSSSSShO...",
"...OhSSOSSSSSSSOSSShO...",
"...OhSSOSSSSSSSOSSShO...",
"...OhsSSSSSSSSSSSSshO...",
"...OhsSSSSSOOSSSSSshO...",
"....OhssSSSSSSSSsshO....",
".....OOssssssssssOO.....",
".......OOOOOOOOOO.......",
"......OOFFFFFFFFOO......",
".....OFFFAAAAAAFFFO.....",
"....OFFfOAAAAAAOfFFO....",
"....OFFfOAAAAAAOfFFO....",
"....OFFfOAAAAAAOfFFO....",
"....OSSOAAAAAAAaOSSO....",
".....OOOAAAAAAaaOOO.....",
".......OAAAAAAaaO.......",
".......OAAAAAAaaO.......",
".......OAAAAAAaaO.......",
".......OFFFFFFFfO.......",
".......OOOOOOOOOO.......",
"........OSsO.OSkO.......",
"........OSsO.OSkO.......",
".......OBBBO.OBBBO......",
".......OOOOO.OOOOO......",
"........................",
]
base = from_rows(yuzu,24,32)
# ladle in right hand (viewer's right)
d = ImageDraw.Draw(base)
for y in range(12,21): base.putpixel((20,y),hx('9A97B0'))
for y in range(12,21): base.putpixel((21,y),OL)
for (x,y) in [(19,9),(20,9),(21,9),(22,9),(19,10),(22,10),(19,11),(22,11),(20,11),(21,11)]:
    base.putpixel((x,y),OL)
base.putpixel((20,10),hx('9A97B0')); base.putpixel((21,10),hx('E8D6C0'))

def idle_frames(im, feet_from=27):
    frames=[]
    for dy in [0,1,0,-1]:
        f = Image.new('RGBA',im.size,(0,0,0,0))
        top = im.crop((0,0,im.width,feet_from))
        f.paste(im.crop((0,feet_from,im.width,im.height)),(0,feet_from))
        if dy<0: f.paste(im.crop((0,feet_from,im.width,feet_from+1)),(0,feet_from-1))
        f.alpha_composite(top,(0,dy)) if dy>=0 else f.alpha_composite(top.crop((0,-dy,im.width,feet_from)),(0,0))
        frames.append(f)
    return frames
idle = idle_frames(base)
sheet = Image.new('RGBA',(24*4,32),(0,0,0,0))
for i,f in enumerate(idle): sheet.paste(f,(24*i,0))
base.save(OUT+"yuzuko_24x32.png"); sheet.save(OUT+"yuzuko_idle_strip.png")
frames_up=[up(f,10) for f in idle]
frames_up[0].save(OUT+"yuzuko_idle.gif",save_all=True,append_images=frames_up[1:],duration=166,loop=0,disposal=2,transparency=0)

# ---------- カゲ: ゴミブクロ 32x32 ----------
K1,K2,K3=hx('3A2D5C'),hx('7A5FB8'),hx('B07CD9'); NE=hx('4FF2E0')
kage = Image.new('RGBA',(32,32),(0,0,0,0))
mask=set()
import math
for y in range(32):
    for x in range(32):
        # bag body: ellipse
        if ((x-15.5)/11.5)**2+((y-20)/10)**2<=1: mask.add((x,y))
        # knot
        if ((x-15.5)/3.5)**2+((y-8)/2.5)**2<=1: mask.add((x,y))
        if 13<=x<=18 and 9<=y<=12 and abs(x-15.5)<=1.5+(y-9)*0.6: mask.add((x,y))
        # ears of knot
        if ((x-11)/2.6)**2+((y-6)/1.6)**2<=1 or ((x-20)/2.6)**2+((y-6)/1.6)**2<=1: mask.add((x,y))
# wobbly bottom (ghostly)
for x in range(32):
    for y in range(27,32):
        if (x//3)%2==0 and y>=29: mask.discard((x,y))
for (x,y) in mask:
    v=(x-15.5)*0.6+(y-18)*0.8
    col = K3 if v<-6 else (K2 if v<5 else K1)
    kage.putpixel((x,y),col)
# outline
for y in range(32):
    for x in range(32):
        if (x,y) not in mask and any((x+dx,y+dy) in mask for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]):
            kage.putpixel((x,y),OL)
# eyes (neon, 2px tall), sad brows, crack
for (x,y) in [(11,17),(11,18),(20,17),(20,18)]: kage.putpixel((x,y),NE)
for (x,y) in [(10,15),(11,15),(20,15),(21,15)]: kage.putpixel((x,y),OL)
kage.putpixel((12,14),OL); kage.putpixel((19,14),OL)
for (x,y) in [(14,22),(15,22),(16,22),(17,22),(13,23),(18,23)]: kage.putpixel((x,y),OL)
for (x,y) in [(23,12),(24,13),(23,14),(24,15),(25,16)]: kage.putpixel((x,y),NE)
kage.save(OUT+"kage_gomibukuro_32x32.png")

# ---------- 3x5 digits ----------
DIG={'0':["111","101","101","101","111"],'1':["010","110","010","010","111"],'2':["111","001","111","100","111"],
'3':["111","001","111","001","111"],'4':["101","101","111","001","001"],'5':["111","100","111","001","111"],'?':["111","001","011","000","010"]}
def text(im,x,y,s,col):
    for i,ch in enumerate(s):
        for r,row in enumerate(DIG[ch]):
            for c,b in enumerate(row):
                if b=='1': im.putpixel((x+i*4+c,y+r),col)

# ---------- 背景: 3階の廊下 320x180 ----------
bg = Image.new('RGBA',(320,180),hx('E8D6C0'))
P=ImageDraw.Draw(bg)
P.rectangle((0,0,319,19),fill=hx('BFA08A')); P.rectangle((0,20,319,22),fill=hx('8C6E5D'))
P.line((0,23,319,23),fill=OL)
# ceiling lamps
for lx in [64,160,256]:
    P.rectangle((lx-4,23,lx+4,26),fill=hx('F4F1F8'),outline=OL)
# wall rain stains
for sx in [30,118,214,300]:
    for yy in range(24,60,2): bg.putpixel((sx,yy),hx('BFA08A'))
doors_x=[20,84,148,212,276]
for i,dx in enumerate(doors_x):
    num=str(301+i)
    clean = (i==2)
    # door
    P.rectangle((dx,50,dx+28,128),fill=hx('3F7FA6'),outline=OL)
    P.rectangle((dx+1,51,dx+3,127),fill=hx('6FB7D9'))     # light from left
    P.line((dx+27,51,dx+27,127),fill=hx('1B1626'))
    P.rectangle((dx+22,88,dx+24,91),fill=hx('FFC857'),outline=OL)  # knob
    P.rectangle((dx+9,58,dx+19,61),fill=hx('8C6E5D'),outline=OL)   # mail slot
    # number plate
    P.rectangle((dx+6,40,dx+22,48),fill=hx('F4F1F8'),outline=OL)
    text(bg,dx+9,42,num,OL)
    if not clean:
        # frosted window + meter box + grime
        P.rectangle((dx+34,62,dx+48,84),fill=hx('6FB7D9'),outline=OL)
        P.line((dx+41,62,dx+41,84),fill=OL)
        P.rectangle((dx+36,96,dx+46,108),fill=hx('9A97B0'),outline=OL)
        for gy in range(110,128,3): bg.putpixel((dx+5+(gy%5),gy),hx('8C6E5D'))
        P.rectangle((dx+6,100,dx+12,104),fill=hx('BFA08A'))
# floor
P.rectangle((0,129,319,141),fill=hx('8C6E5D')); P.line((0,129,319,129),fill=OL)
for fx in range(0,320,16): P.line((fx,130,fx,141),fill=hx('BFA08A'))
# sunset behind railing
for y in range(142,180):
    for x in range(320):
        t=(y-142)/38
        c = hx('FFC857') if t<0.35 else hx('F27D52')
        if 0.3<t<0.4 and (x+y)%2==0: c=hx('F27D52')
        bg.putpixel((x,y),c)
# distant sea
P.rectangle((0,170,319,179),fill=hx('3F7FA6'))
for x in range(0,320,2): bg.putpixel((x,169),hx('6FB7D9'))
# railing
P.rectangle((0,146,319,150),fill=hx('BFA08A'),outline=OL)
for rx in range(4,320,10): P.rectangle((rx,151,rx+2,179),fill=hx('BFA08A'),outline=OL)
bg.save(OUT+"bg_303_corridor_320x180.png")

# ---------- UI: 部屋マス ----------
CW,CH=22,18
def cell(state):
    im=Image.new('RGBA',(CW,CH),(0,0,0,0)); D=ImageDraw.Draw(im)
    if state=='303':
        D.rectangle((0,0,CW-1,CH-1),fill=hx('E8D6C0'),outline=OL)
        D.rectangle((7,3,14,CH-1),fill=hx('3F7FA6'),outline=OL)
        D.line((8,4,8,CH-2),fill=hx('6FB7D9'))
        im.putpixel((12,10),hx('FFC857'))
        return im
    D.rectangle((0,0,CW-1,CH-1),fill=hx('BFA08A'),outline=OL)
    win=(4,3,CW-5,CH-4)
    if state=='broken':
        D.rectangle(win,fill=hx('241C3A'),outline=OL)
        D.line((3,6,CW-4,9),fill=hx('8C6E5D'),width=2); D.line((3,11,CW-4,8),fill=hx('8C6E5D'),width=2)
    elif state=='empty': D.rectangle(win,fill=hx('3A2D5C'),outline=OL)
    elif state in ('lived','lucky','selected'):
        D.rectangle(win,fill=hx('FFC857'),outline=OL)
        D.rectangle((5,4,7,CH-6),fill=hx('F27D52')); D.rectangle((CW-8,4,CW-6,CH-6),fill=hx('F27D52'))
        if state=='lucky':
            for (x,y) in [(10,0),(11,0),(10,1),(11,1),(10,2)]: im.putpixel((x,y),hx('FF5FA2'))
        if state=='selected': D.rectangle((0,0,CW-1,CH-1),outline=hx('4FF2E0'))
    return im
layout=[['broken','broken','lived','broken','broken'],
        ['broken','lived','lucky','lived','broken'],
        ['empty','lived','303','selected','empty'],
        ['broken','selected','lived','selected','broken'],
        ['broken','broken','empty','broken','broken']]
grid=Image.new('RGBA',(5*CW+6*2,5*CH+6*2),hx('241C3A'))
for r,row in enumerate(layout):
    for c,st in enumerate(row): grid.alpha_composite(cell(st),(2+c*(CW+2),2+r*(CH+2)))
grid.save(OUT+"ui_room_grid.png")

# ---------- こせい札 8x8 ----------
cols=['F27D52','3F7FA6','4E8C4A','FFC857','E8D6C0','7A5FB8']
sym={
 'red':  ["........","........","..XXXX..",".X....X.","..XXXX..","........"],  # bowl
 'blue': ["..XXXX..","..X..X..","..X..X..","...XX...","........","........"],  # shield
 'green':["........","..X.X...",".XXXXX..","..XXX...","...X....","........"],  # heart
 'yel':  ["...XX...","..X.....","..X.....","...XX...","........","........"],  # moon
 'white':["..XX....",".X..X...","..XX....","....X...",".....X..","........"],  # magnifier
 'pur':  ["........","....XX..",".....X..","..X..X..","...XX...","........"],  # tail
}
tags=Image.new('RGBA',(6*10,10),(0,0,0,0))
for i,(k,cc) in enumerate(zip(sym,cols)):
    t=Image.new('RGBA',(8,8),(0,0,0,0)); D=ImageDraw.Draw(t)
    D.rectangle((0,0,7,7),fill=hx(cc),outline=OL)
    for c in [(0,0),(7,0),(0,7),(7,7)]: t.putpixel(c,(0,0,0,0))
    for y,row in enumerate(sym[k]):
        for x,b in enumerate(row):
            if b=='X' and 0<x<7 and 0<y+1<7: t.putpixel((x,y+1),OL if k in('white','yel') else hx('F4F1F8'))
    tags.alpha_composite(t,(1+i*10,1))
tags.save(OUT+"ui_kosei_tags.png")

# ---------- まとめ ----------
font=ImageFont.truetype('/usr/share/fonts/opentype/unifont/unifont_jp.otf',16)
S=4
W=1540; Hh=1060
sheet2=Image.new('RGBA',(W,Hh),hx('120F1F')); D=ImageDraw.Draw(sheet2)
def place(img,k,x,y,label,bgc=hx('F4F1F8')):
    u=up(img,k)
    D.rectangle((x-4,y-4,x+u.width+3,y+u.height+3),fill=bgc)
    sheet2.alpha_composite(u,(x,y)); D.text((x,y+u.height+10),label,font=font,fill=hx('E8D6C0'))
place(base,8,30,30,"ユズコ 24×32（×8）")
for i,f in enumerate(idle): place(f,5,260+i*130,90,"待機%d"%(i+1))
place(kage,7,820,30,"カゲ「ゴミブクロ」32×32（×7）",bgc=hx('3A2D5C'))
place(bg,3,30,340,"303の廊下 320×180（×3）　真ん中の303だけ窓もメーターも無い")
place(grid,4,1020,340,"編成画面のマス（×4）",bgc=hx('241C3A'))
D.text((1020,800),"ドアだけ＝303／ピンク＝当たり部屋",font=font,fill=hx('E8D6C0'))
D.text((1020,820),"水色の枠＝夜回りに選んだ部屋",font=font,fill=hx('E8D6C0'))
place(tags,8,1020,870,"こせい札 8×8（赤青緑黄白紫）",bgc=hx('F4F1F8'))
sheet2.convert('RGB').save(OUT+"preview_sheet.png")
print("ok")

# =================== 主人公とカゲモリ ===================
C.update({'Y':hx('FFC857'),'y':hx('C97F5A'),'J':hx('3F7FA6'),'j':hx('241C3A'),'K':hx('9A97B0'),'N':hx('F4F1F8')})
hero_rows = [
"........................",
"........O.OOOOOO.O......",
".......OhOhhhhhhOhO.....",
".....OOhhhhhhhhhhOO.....",
"....OhhhhhhhhhhhhhhO....",
] + yuzu[5:15] + [
"......OOYYYYYYYYOO......",
".....OYYYONNNNOYYYO.....",
"....OYYyONNNNNNOyYYO....",
"....OYYyONNKKNNOyYYO....",
"....OYYyONNKNNNOyYYO....",
"....OSSOYNNNNNNYOSSO....",
".....OOOYYNNNNYyOOO.....",
".......OYYNNNNYyO.......",
".......OJJJJJJJJO.......",
".......OJJJJJJJjO.......",
"........OJJO.OJjO.......",
"........OJJO.OJjO.......",
"........OJJO.OJjO.......",
".......ONNNO.ONNNO......",
".......OOOOO.OOOOO......",
"........................",
]
hero = from_rows(hero_rows,24,32)
# key string
for (x,y) in [(10,16),(11,17),(13,16),(12,17)]: hero.putpixel((x,y),hx('C97F5A'))

def walk_frames(im, split=25):
    top = im.crop((0,0,24,split))
    L = im.crop((0,split,12,32)); R = im.crop((12,split,24,32))
    out=[]
    for body,ly,ry in [(0,0,0),(1,-2,0),(0,-1,0),(0,0,0),(1,0,-2),(0,0,-1)]:
        f = Image.new('RGBA',(24,32),(0,0,0,0))
        f.alpha_composite(L,(0,split+ly)); f.alpha_composite(R,(12,split+ry))
        f.alpha_composite(top,(0,body))
        out.append(f)
    return out

def save_anim(frames, name, ms):
    sheet = Image.new('RGBA',(24*len(frames),32),(0,0,0,0))
    for i,f in enumerate(frames): sheet.paste(f,(24*i,0))
    sheet.save(OUT+name+"_strip.png")
    ups=[up(f,10) for f in frames]
    ups[0].save(OUT+name+".gif",save_all=True,append_images=ups[1:],duration=ms,loop=0,disposal=2,transparency=0)

hero.save(OUT+"hero_24x32.png")
hero_idle = idle_frames(hero); hero_walk = walk_frames(hero)
save_anim(hero_idle,"hero_idle",166); save_anim(hero_walk,"hero_walk",100)

# カゲモリ：主人公の顔立ち＋サカキの鍵束、色だけ裏のパレット
night = {hx('FCE3C6'):hx('B07CD9'),hx('F2B98A'):hx('7A5FB8'),hx('C97F5A'):hx('3A2D5C'),hx('8C6E5D'):hx('241C3A'),
         hx('FFC857'):hx('6B6FA3'),hx('F4F1F8'):hx('8FA3C7'),hx('3F7FA6'):hx('3A2D5C'),hx('241C3A'):hx('120F1F'),hx('9A97B0'):hx('4FF2E0')}
kage_mori = hero.copy()
for y in range(32):
    for x in range(24):
        p = kage_mori.getpixel((x,y))
        if p in night: kage_mori.putpixel((x,y),night[p])
for (x,y) in [(7,8),(7,9),(15,8),(15,9)]: kage_mori.putpixel((x,y),hx('4FF2E0'))
# 鍵束（腰）
for (x,y) in [(17,21),(18,21),(18,22),(17,23),(19,23)]: kage_mori.putpixel((x,y),hx('4FF2E0'))
kage_mori.save(OUT+"kagemori_24x32.png")
save_anim(idle_frames(kage_mori),"kagemori_idle",166)

sheet3=Image.new('RGBA',(1180,620),hx('120F1F')); D=ImageDraw.Draw(sheet3)
def place3(img,k,x,y,label,bgc):
    u=up(img,k); D.rectangle((x-4,y-4,x+u.width+3,y+u.height+3),fill=bgc)
    sheet3.alpha_composite(u,(x,y)); D.text((x,y+u.height+10),label,font=font,fill=hx('E8D6C0'))
place3(hero,8,30,30,"主人公 24×32（×8）",hx('F4F1F8'))
for i,f in enumerate(hero_walk): place3(f,5,260+i*130,30,"歩き%d"%(i+1),hx('F4F1F8'))
place3(kage_mori,8,30,320,"カゲモリ（色だけ裏）",hx('3A2D5C'))
for i,f in enumerate(hero_idle): place3(f,5,260+i*130,320,"主人公 待機%d"%(i+1),hx('F4F1F8'))
sheet3.convert('RGB').save(OUT+"preview_sheet_hero.png")
print("hero ok")
