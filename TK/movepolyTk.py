import time
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
canvas.create_polygon(10, 10, 10, 60, 50, 35) # 返り値で識別番号(ID)を返す
for x in range(0, 60):
    canvas.move(1, 5, 5) # 引数の意味 = (ID, 移動するx座標の値, 移動するy座標の値)
    tk.update()
    time.sleep(0.05)

for x in range(0, 60):
    canvas.move(1, -5, -5)
    tk.update()
    time.sleep(0.05)
