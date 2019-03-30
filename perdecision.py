import turtle
import random
import math

def backorigin():
    # 原点に戻る
    my_turtle.seth(90)
    my_turtle.goto(0,0)

def tup():
    # 前に進む
    my_turtle.seth(90)
    if 290 >= my_turtle.ycor():
        my_turtle.forward(7)

def tdown():
    # 後ろに下がる
    my_turtle.seth(90)
    if my_turtle.ycor() >= -300:
        my_turtle.forward(-7)

def tleft():
    # 左に進む
    screen.onkeypress(None, "Left")
    my_turtle.seth(180)
    if my_turtle.xcor() >= -300:
        my_turtle.forward(7)
    screen.delay(0.001)
    screen.onkeypress(tleft, "Left")

def tright():
    # 右に進む
    screen.onkeypress(None, "Right")
    my_turtle.seth(0)
    if 300 >= my_turtle.xcor():
        my_turtle.forward(7)
    screen.delay(0.001)
    screen.onkeypress(tright, "Right")


def resetangle():
    screen.onkeypress(None, "Left")
    screen.onkeypress(None, "Right")
    x = my_turtle.xcor()
    y = my_turtle.ycor()
    screen.delay(0.005)
    my_turtle.seth(90)
    my_turtle.forward(0)
    my_turtle.goto(x, y)
    screen.delay(0.01)
    screen.onkeypress(tleft, "Left")
    screen.onkeypress(tright, "Right")

def is_hit(target, turtle):
    # タートルとターゲットの衝突判定
    diff = math.sqrt(
    math.pow(target.xcor()- turtle.xcor(), 2)
             + math.pow(target.ycor() - turtle.ycor(), 2))
    return True if diff < 40 else False

def game():
    for t in targets:
        # 衝突チェック
        if is_hit(t, my_turtle):
            # タートルがターゲットにぶつかったらゲームオーバー
            screen.onkeypress(None, "Left")
            screen.onkeypress(None, "Right")
            screen.onkeypress(None, "Up")
            screen.onkeypress(None, "Down")
            screen.tracer(1)
            my_turtle.color("gray")
            # タートルを震わせる
            for _ in range(10):
                my_turtle.right(15)
                my_turtle.left(15)
            time_text.goto(-300, 0)
            time_text.write("ゲームオーバー", font=("helvetica", 60))
            return
    # 画面をアップデート
    screen.update()
    screen.ontimer(game, 10)


# スクリーンの設定
screen = turtle.Screen()
screen.setup(650, 650)
screen.title("moveTurtle")

targets = [] # ターゲットを格納するリスト
num_of_targets = 6 # ターゲットの数
colors = ["blue", "green", "black", "purple", "pink", "yellow", "orange"] # ターゲットの色

# ターゲットを描画
for y in range(num_of_targets):
    t = turtle.Turtle()
    t.ht()
    t.penup()
    t.color(random.choice(colors))
    t.shape("square")
    t.shapesize(2)
    t.sety(-100 + y * 50)
    t.setx(-100 + y * 50)
    t.st()
    targets.append(t)

# タートルの設定
my_turtle = turtle.Turtle()
my_turtle.ht() # hideturtle
my_turtle.penup()
my_turtle.shape("turtle")
my_turtle.shapesize(2)
my_turtle.color("red")
my_turtle.goto(0, -280)
my_turtle.seth(90)
my_turtle.st() # showturtle

# キーイベントの設定
screen.listen()
screen.onkeypress(tleft, "Left")
screen.onkeypress(tright, "Right")
screen.onkeypress(tup, "Up")
screen.onkeypress(tdown, "Down")
screen.onkeyrelease(resetangle, "Left")
screen.onkeyrelease(resetangle, "Right")
screen.onkey(backorigin, "s")

# 経過時間表示テキスト用
time_text = turtle.Turtle()
time_text.penup()
time_text.hideturtle()
time_text.goto(0, -300)

# トレーサーをオフ
screen.tracer(0)

game()

screen.mainloop()
