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
        my_turtle.forward(step)

def tdown():
    # 後ろに下がる
    my_turtle.seth(90)
    if my_turtle.ycor() >= -300:
        my_turtle.forward(-step)

def tleft():
    # 左に進む
    screen.onkeypress(None, "Left")
    my_turtle.seth(180)
    if my_turtle.xcor() >= -300:
        my_turtle.forward(step)
    screen.delay(0.001)
    screen.onkeypress(tleft, "Left")

def tright():
    # 右に進む
    screen.onkeypress(None, "Right")
    my_turtle.seth(0)
    if 300 >= my_turtle.xcor():
        my_turtle.forward(step)
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
    math.pow(target.xcor() - turtle.xcor(), 2)
             + math.pow(target.ycor() - turtle.ycor(), 2))
    return True if diff < 25 else False

def make_shot(pos):
    # 弾の生成
    for y in range(num_of_targets):
        t = turtle.Turtle()
        t.ht()
        t.penup()
        t.sety(250)
        t.setx(0)
        t.color(random.choice(colors))
        t.shape("square")
        t.shapesize(1)
        t.st()
        t.speed(1)
        t.goto(pos + y, 250)
        targets.append(t)

def isexist():
    for t in targets:
        if t.xcor() >= -350 and 350 >= t.xcor() and t.ycor() >= -350 and 350 >= t.ycor():
            return False
    return True

def attack_spread(i, t, angle):
    t.seth(angle + (i - 3) * 10)
    t.forward(6)
    t.tilt(3)

def game():
    global count

    if isexist() :
        targets.clear()
        count += 1
    if len(targets) == 0:
        if count%2 == 0:
            make_shot(-100)
        else :
            make_shot(100)
    for i, t in enumerate(targets):
        attack_spread(i, t, 270)

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
screen.bgcolor("black")
screen.title("moveTurtle")

targets = [] # ターゲットを格納するリスト
num_of_targets = 6 # ターゲットの数
colors = ["blue", "green", "purple", "pink", "yellow", "orange"] # ターゲットの色

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

step = 8

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
time_text.color("white")
time_text.penup()
time_text.hideturtle()
time_text.goto(0, -300)

# トレーサーをオフ
screen.tracer(0)

count = 1

game()

screen.mainloop()
