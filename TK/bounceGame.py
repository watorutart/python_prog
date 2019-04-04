from tkinter import *
import random
import time

class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id) # coordsの返り値は円の左上のx, y座標と右下のx, y座標の４つ
        if pos[1] <= 0:
            self.y = 1
        elif pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if self.hit_paddle(pos) == True:
            self.y = -3
        if pos[0] <= 0:
            self.x = 3
        elif pos[2] >= self.canvas_width:
            self.x = -3

class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.wait = True
        self.canvas.bind_all('<Button-1>', self.game_start)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0

    def game_start(self, evt):
        self.wait = False

    def turn_left(self, evt):
        self.x = -2

    def turn_right(self, evt):
        self.x = 2

tk = Tk()
tk.title("Game")
tk.resizable(0, 0) # 引数(0, 0)でウィンドウのサイズを固定
tk.wm_attributes("-topmost", 1) # 一番上のウィンドウに配置
canvas = Canvas(tk, width=500,
                height=400,
                bd=0, highlightthickness=0) # bd=0,highlightthickness=0でキャンバスの外側の線をなくす
canvas.pack()
tk.update()

paddle = Paddle(canvas, 'blue')
ball = Ball(canvas, paddle, 'red')
canvas.create_text(250, 250, text='左クリックでスタート！', font=('Courier', 30), tag="disp_start", fill="green")
gameover = canvas.create_text(250, 100, text='Game Over...', font=('Courier', 30), fill="red", state="hidden")

while True:
    if paddle.wait == False:
        canvas.delete("disp_start")
        if ball.hit_bottom == False:
            ball.draw()
            paddle.draw()
        elif ball.hit_bottom == True:
            print("game over")
            canvas.itemconfig(gameover, state="normal")
            tk.update_idletasks()
            tk.update()
            time.sleep(3)
            break
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)



# tk.mainloop()