from tkinter import *
import random
import time

# global speed_up

class Ball:
    # global speed_up
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
        self.score = 0

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False

    def draw(self):
        global speed_up
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id) # coordsの返り値は円の左上のx, y座標と右下のx, y座標の４つ
        if pos[1] <= 0:
            self.y = 3 + speed_up
        elif pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if self.hit_paddle(pos) == True:
            self.score += 10
            self.y = -3 - speed_up
            if self.paddle.x != 0:
                self.x = self.paddle.x * 2
            else :
                self.x = random.randint(-3, 4) + speed_up
            if self.score%50 == 0:
                speed_up += 1
            if self.score%80 == 0:
                speed_up -= 0.5
            if self.score%200 == 0:
                speed_up -= 2

        if pos[0] <= 0:
            self.x = 3 + speed_up
        elif pos[2] >= self.canvas_width:
            self.x = -3 - speed_up

class Paddle:
    # global speed_up
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
        global speed_up
        self.x = -2 - speed_up

    def turn_right(self, evt):
        global speed_up
        self.x = 2 + speed_up

tk = Tk()
tk.title("Game")
tk.resizable(0, 0) # 引数(0, 0)でウィンドウのサイズを固定
tk.wm_attributes("-topmost", 1) # 一番上のウィンドウに配置
canvas = Canvas(tk, width=500,
                height=400,
                bd=0, highlightthickness=0) # bd=0,highlightthickness=0でキャンバスの外側の線をなくす
canvas.pack()
tk.update()

speed_up = 0

paddle = Paddle(canvas, 'blue')
ball = Ball(canvas, paddle, 'red')
canvas.create_text(250, 250, text='左クリックでスタート！', font=('Courier', 30), tag="disp_start", fill="green")
gameover = canvas.create_text(250, 100, text='Game Over...', font=('Courier', 30), fill="red", state="hidden")
disp_score = canvas.create_text(400, 10, text=f'score : {ball.score:10d}')

while True:
    if paddle.wait == False:
        canvas.delete("disp_start")
        canvas.itemconfig(disp_score, text=f'score : {ball.score:10d}')
        if ball.hit_bottom == False:
            ball.draw()
            paddle.draw()
        elif ball.hit_bottom == True:
            print("game over")
            canvas.itemconfig(gameover, state="normal")
            tk.update_idletasks()
            tk.update()
            time.sleep(2)
            break
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)



# tk.mainloop()
