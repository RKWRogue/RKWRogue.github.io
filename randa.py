import tkinter
import random

BPM = 120
measure = 1 # 小節数
white = 0 # 白数字
grid = 0
green = 320 # 緑数字
time = 5 * green / 3
scratch = 0
pattern = [0, 0, 0, 0, 0, 0, 0, 0]
sheet = []
flag = 0
# BPM調整を実行する
def click_BPMmm():
    global BPM
    if BPM > 10:
        BPM -= 10
    dspBPM2["text"] = str(BPM)

def click_BPMm():
    global BPM
    if BPM > 1:
        BPM -= 1
    dspBPM2["text"] = str(BPM)

def click_BPMp():
    global BPM
    if BPM < 999:
        BPM += 1
    dspBPM2["text"] = str(BPM)

def click_BPMpp():
    global BPM
    if BPM < 990:
        BPM += 10
    dspBPM2["text"] = str(BPM)

#　小節数変化を実行する
def click_measuremm():
    global measure
    if measure > 10:
        measure -= 10
    dspmeasure2["text"] = str(measure)

def click_measurem():
    global measure
    if measure > 1:
        measure -= 1
    dspmeasure2["text"] = str(measure)

def click_measurep():
    global measure
    if measure < 64:
        measure += 1
    dspmeasure2["text"] = str(measure)

def click_measurepp():
    global measure
    if measure < 55:
        measure += 10
    dspmeasure2["text"] = str(measure)

#　白数字調整を実行する
def click_whitemm():
    global white
    global grid
    if white > 9:
        white -= 10
        grid = 11 * white / 20
    dspwhite2["text"] = str(white)
    cvs.delete("hide")
    cvs.create_rectangle(40, 0, 380, 550 * white / 1000, fill="black", outline="black", width=1, tag="hide")

def click_whitem():
    global white
    global grid
    if white > 0:
        white -= 1
        grid = 11 * white / 20
    dspwhite2["text"] = str(white)
    cvs.delete("hide")
    cvs.create_rectangle(40, 0, 380, 550 * white / 1000, fill="black", outline="black", width=1, tag="hide")

def click_whitep():
    global white
    global grid
    if white < 999:
        white += 1
        grid = 11 * white / 20
    dspwhite2["text"] = str(white)
    cvs.delete("hide")
    cvs.create_rectangle(40, 0, 380, 550 * white / 1000, fill="black", outline="black", width=1, tag="hide")

def click_whitepp():
    global white
    global grid
    if white < 990:
        white += 10
        grid = 11 * white / 20
    dspwhite2["text"] = str(white)
    cvs.delete("hide")
    cvs.create_rectangle(40, 0, 380, 550 * white / 1000, fill="black", outline="black", width=1, tag="hide")

#　緑数字調整を実行する
def click_greenmm():
    global green
    global time
    if green > 10:
        green -= 10
        time = 5 * green / 3
    dspgreen2["text"] = str(green)

def click_greenm():
    global green
    global time
    if green > 1:
        green -= 1
        time = 5 * green / 3
    dspgreen2["text"] = str(green)

def click_greenp():
    global green
    global time
    if green < 999:
        green += 1
        time = 5 * green / 3
    dspgreen2["text"] = str(green)

def click_greenpp():
    global green
    global time
    if green < 990:
        green += 10
        time = 5 * green / 3
    dspgreen2["text"] = str(green)

# 譜面を作る

def makesheet():
    global measure
    global BPM
    global grid
    global time
    interval = 15000 * (550-grid) / BPM / time
    x = [1, 2, 3, 4, 5, 6, 7]
    sheet0 = [[600, 0, 0, 0, 0, 0, 0, 0, 0] for i in range (measure * 16)]
    for i in range(measure * 16):
        sheet0[i][0] += interval * i
    if scratch != 0:
        for i in range(measure * 16):
            if i % scratch == 0:
                sheet0[i][1] = 1
    for i in range(measure * 16):
        r = i % 8
        num = pattern[r]
        if (i == 0):
            y = random.sample(x, num)
            for j in range(len(y)):
                sheet0[0][y[j] + 1] = 1
        else:
            b = []
            for j in range(1, 8):
                if (sheet0[i-1][j + 1] == 0):
                    b.append(j)
            z = random.sample(b, num)
            for j in range(len(z)):
                sheet0[i][z[j] + 1] = 1
    return sheet0
# ランダムで譜面を生成、同じレーンに2つのノーツが連続しないようにしている

# パターンを読み込んで譜面を作る
def click_selected():
    global scratch
    global sheet
    sch = scratch1.get()
    if sch != '':
        scratch = int(sch)
    ptn1 = pattern1.get()
    if ptn1 != '':
        pattern[0] = int(ptn1)
    ptn2 = pattern2.get()
    if ptn2 != '':
        pattern[1] = int(ptn2)
    ptn3 = pattern3.get()
    if ptn3 != '':
        pattern[2] = int(ptn3)
    ptn4 = pattern4.get()
    if ptn4 != '':
        pattern[3] = int(ptn4)
    ptn5 = pattern5.get()
    if ptn5 != '':
        pattern[4] = int(ptn5)
    ptn6 = pattern6.get()
    if ptn6 != '':
        pattern[5] = int(ptn6)
    ptn7 = pattern7.get()
    if ptn7 != '':
        pattern[6] = int(ptn7)
    ptn8 = pattern8.get()
    if ptn8 != '':
        pattern[7] = int(ptn8)
    if flag == 0:
        sheet = makesheet()

# 譜面を流す
def play():
    global grid
    global time
    global sheet
    global flag
    flag = 1
    cvs.delete("Note")
    cvs.delete("Line")
    for i in range(measure * 16):
        if -50 < sheet[i][0] < 550:
            for j in range (1, 9):
                if sheet[i][j] == 1:
                    if (j == 1):
                        cvs.create_line(40 ,550-sheet[i][0], 90, 550-sheet[i][0], fill="red", width=12, tag="Note")
                    elif (j % 2 == 1):
                        cvs.create_line(100+40*(j-2) ,550-sheet[i][0], 100+40*(j-1), 550-sheet[i][0], fill="blue", width=12, tag="Note")
                    else:
                        cvs.create_line(100+40*(j-2) ,550-sheet[i][0], 100+40*(j-1), 550-sheet[i][0], fill="black", width=12, tag="Note")
            if i % 16 == 0:
                cvs.create_line(40 ,550-sheet[i][0], 380, 550-sheet[i][0], fill="silver", width=5, tag="Line")
    cvs.delete("hide")
    cvs.create_rectangle(40, 0, 380, 550 * white / 1000, fill="black", outline="black", width=1, tag="hide")
    for i in range (measure * 16):
        sheet[i][0] -= 6 * (550 - grid) / time
    if sheet[measure * 16 - 1][0] > -65:
        root.after(5, play)
    else:
        flag = 0
#時間の処理さえ正確にできればなぁ...
def click_start():
    global flag
    if flag == 0:
        play()
        
root = tkinter.Tk()
root.title("RANDA Random")
root.geometry("750x600")
root.resizable(False, False)
cvs = tkinter.Canvas(root, width=750, height=600, bg="white")
cvs.pack()
cvs.create_line(40, 0, 40, 600, fill="black", width=2)
cvs.create_line(95, 0, 95, 600, fill="black", width=6)
cvs.create_line(140, 0, 140, 600, fill="black", width=2)
cvs.create_line(180, 0, 180, 600, fill="black", width=2)
cvs.create_line(220, 0, 220, 600, fill="black", width=2)
cvs.create_line(260, 0, 260, 600, fill="black", width=2)
cvs.create_line(300, 0, 300, 600, fill="black", width=2)
cvs.create_line(340, 0, 340, 600, fill="black", width=2)
cvs.create_line(380, 0, 380, 600, fill="black", width=2)
cvs.create_line(40, 550, 380, 550, fill="black", width=2)
# レーンを書いている

title = tkinter.Label(root, text="乱打ランダム生成", font=("Times New Roman", 30))
title.place(x=430, y=30)

# BPM表記、設定

dspBPM1 = tkinter.Label(root, text="・BPM", font=("Times New Roman", 20))
dspBPM1.place(x=420, y=90)

BPMmm = tkinter.Button(root, text="<<", font=("Times New Roman", 20), command=click_BPMmm)
BPMmm.place(x=470, y=120)

BPMm = tkinter.Button(root, text="<", font=("Times New Roman", 20), command=click_BPMm)
BPMm.place(x=500, y=120)

dspBPM2 = tkinter.Label(root, text=str(BPM), font=("Times New Roman", 20))
dspBPM2.place(x=520, y=120)

BPMp = tkinter.Button(root, text=">", font=("Times New Roman", 20), command=click_BPMp)
BPMp.place(x=560, y=120)

BPMpp = tkinter.Button(root, text=">>", font=("Times New Roman", 20), command=click_BPMpp)
BPMpp.place(x=580, y=120)

# 小節数

dspmeasure1 = tkinter.Label(root, text="・小節数", font=("Times New Roman", 20))
dspmeasure1.place(x=420, y=150)

measuremm = tkinter.Button(root, text="<<", font=("Times New Roman", 20), command=click_measuremm)
measuremm.place(x=470, y=180)

measurem = tkinter.Button(root, text="<", font=("Times New Roman", 20), command=click_measurem)
measurem.place(x=500, y=180)

dspmeasure2 = tkinter.Label(root, text=str(measure), font=("Times New Roman", 20))
dspmeasure2.place(x=520, y=180)

measurep = tkinter.Button(root, text=">", font=("Times New Roman", 20), command=click_measurep)
measurep.place(x=560, y=180)

measurepp = tkinter.Button(root, text=">>", font=("Times New Roman", 20), command=click_measurepp)
measurepp.place(x=580, y=180)

# 白数字

dspwhite1 = tkinter.Label(root, text="・SUDDEN+", font=("Times New Roman", 20))
dspwhite1.place(x=420, y=210)

whitemm = tkinter.Button(root, text="<<", font=("Times New Roman", 20), command=click_whitemm)
whitemm.place(x=470, y=240)

whitem = tkinter.Button(root, text="<", font=("Times New Roman", 20), command=click_whitem)
whitem.place(x=500, y=240)

dspwhite2 = tkinter.Label(root, text=str(white), font=("Times New Roman", 20))
dspwhite2.place(x=520, y=240)

whitep = tkinter.Button(root, text=">", font=("Times New Roman", 20), command=click_whitep)
whitep.place(x=560, y=240)

whitepp = tkinter.Button(root, text=">>", font=("Times New Roman", 20), command=click_whitepp)
whitepp.place(x=580, y=240)

# 緑数字

dspgreen1 = tkinter.Label(root, text="・緑数字", font=("Times New Roman", 20))
dspgreen1.place(x=420, y=270)

greenmm = tkinter.Button(root, text="<<", font=("Times New Roman", 20), command=click_greenmm)
greenmm.place(x=470, y=300)

greenm = tkinter.Button(root, text="<", font=("Times New Roman", 20), command=click_greenm)
greenm.place(x=500, y=300)

dspgreen2 = tkinter.Label(root, text=str(green), font=("Times New Roman", 20))
dspgreen2.place(x=520, y=300)

greenp = tkinter.Button(root, text=">", font=("Times New Roman", 20), command=click_greenp)
greenp.place(x=560, y=300)

greenpp = tkinter.Button(root, text=">>", font=("Times New Roman", 20), command=click_greenpp)
greenpp.place(x=580, y=300)

# 皿

dspscratch1 = tkinter.Label(root, text="・スクラッチ", font=("Times New Roman", 20))
dspscratch1.place(x=420, y=330)

scratch1 = tkinter.Entry(width = 2)
scratch1.place(x=470, y=360)

dspscratch2 = tkinter.Label(root, text="ノートごと", font=("Times New Roman", 20))
dspscratch2.place(x=500, y=360)

# パターン

dsppattern1 = tkinter.Label(root, text="・パターン", font=("Times New Roman", 20))
dsppattern1.place(x=420, y=390)

pattern1 = tkinter.Entry(width = 1)
pattern1.place(x=470, y=420) 

pattern2 = tkinter.Entry(width = 1)
pattern2.place(x=490, y=420)

pattern3 = tkinter.Entry(width = 1)
pattern3.place(x=510, y=420)

pattern4 = tkinter.Entry(width = 1)
pattern4.place(x=530, y=420)

pattern5 = tkinter.Entry(width = 1)
pattern5.place(x=550, y=420)

pattern6 = tkinter.Entry(width = 1)
pattern6.place(x=570, y=420)

pattern7 = tkinter.Entry(width = 1)
pattern7.place(x=590, y=420)

pattern8 = tkinter.Entry(width = 1)
pattern8.place(x=610, y=420)

# 譜面を確定させる
selected = tkinter.Button(root, text="更新", font=("Times New Roman", 20), command=click_selected)
selected.place(x=520, y=450)

start = tkinter.Button(root, text="スタート", font=("Times New Roman", 20), command=click_start)
start.place(x=500, y=500)


root.mainloop()
