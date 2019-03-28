import turtle
import math
import random
import datetime

def tleft():
    # 左に回転
    my_turtle.left(10)

def tright():
    # 右に回転
    my_turtle.right(10)

def tup():
    # スピードアップ
    global step
    if step <= 10:
        step += 1

def tdown():
    # スピードダウン
    global step
    if step > 0:
        step -= 1

def is_hit(target, turtle):
    # タートルとターゲットの衝突判定
    diff = math.sqrt(
    math.pow(target.xcor()- turtle.xcor(), 2)
             + math.pow(target.ycor() - turtle.ycor(), 2))
    return True if diff < 40 else False

def game():
    global count

    # 壁にぶつかったらタートルを跳ね返す
    if math.fabs(my_turtle.xcor()) >= X_LIMIT:
        angle = 180 - my_turtle.heading()
        my_turtle.setheading(angle)
    if my_turtle.ycor() >= Y_LIMIT:
        angle = 360 - my_turtle.heading()
        my_turtle.setheading(angle)

    my_turtle.forward(step)

    # ターゲットを移動する
    for t in targets:
        t.forward(random.randrange(10))
        t.tilt(3)

        # 壁にぶつかったら反転
        if math.fabs(t.xcor()) > X_LIMIT:
            t.right(180)
            t.forward(10)

        # 衝突チェック
        if is_hit(t, my_turtle):
            # ヒットしたタートルを灰色にしてtargetsから取り除く
            t.color("#EEEEEE")
            targets.remove(t)
            r_text.clear()
            r_text.write(
            f"残りターゲット{len(targets)}",
            font=("helvetica", 24)
            )

    # 経過時間を計算する
    now = datetime.datetime.now()
    etime = now - stime

    # ターゲットが残っていれば経過時間を更新
    if len(targets) > 0:
        sec = etime.seconds + etime.microseconds /1000000
        time_text.clear()
        time_text.write(f"経過時間: {sec:1f}秒",
                        font=("helvetica", 24))
    else :
        time_text.goto(-280, 0)
        time_text.write("ミッション完了!", font=("helvetica", 60))
        screen.update()
        return

    # タートルが下の壁にぶつかったらゲームオーバー
    if my_turtle.ycor() < -Y_LIMIT:
        screen.tracer(1)
        my_turtle.color("red")
        # タートルを震わせる
        for _ in range(10):
            my_turtle.right(15)
            my_turtle.left(15)
        time_text.goto(-300, 0)
        time_text.write("ゲームオーバー", font=("helvetica", 60))
    else :
        # 画面をアップデート
        screen.update()
        screen.ontimer(game, 10)

screen = turtle.Screen()
screen.setup(700, 700)
screen.title("ゲーム")

# タートルを描画する
my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.shapesize(3)
my_turtle.color("red")
my_turtle.penup()

targets = [] # ターゲットを格納するリスト
num_of_targets = 6 # ターゲットの数
colors = ["blue", "green", "black", "purple", "pink", "yellow", "orange"] # ターゲットの色

# ターゲットを描画
for y in range(num_of_targets):
    t = turtle.Turtle()
    t.penup()
    t.color(random.choice(colors))
    t.shape("square")
    t.shapesize(2)
    t.sety(y * 100 - 300)
    t.setx(-300 + random.randrange(3) * 100)
    targets.append(t)

# トレーサーをオフ
screen.tracer(0)

# スタート時間
stime = datetime.datetime.now()

# キーイベント
screen.listen()
screen.onkey(tleft, "Left")
screen.onkey(tright, "Right")
screen.onkey(tup, "Up")
screen.onkey(tdown, "Down")

# 残りターゲット表示テキスト用
r_text = turtle.Turtle()
r_text.penup()
r_text.hideturtle()
r_text.goto(-320, -300)
r_text.write(f"残りターゲット：{len(targets)}", font=("helvetica", 24))

# 経過時間表示テキスト用
time_text = turtle.Turtle()
time_text.penup()
time_text.hideturtle()
time_text.goto(0, -300)

# 経過時間
e_time = 0

# 境界
X_LIMIT = 300
Y_LIMIT = 300

# タートルのループごとの移動距離
step = 3
# タートルの角度
angle = 40
my_turtle.left(angle)

# ゲーム開始
game()
screen.mainloop()
