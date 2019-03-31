import turtle
import random
import math
import time

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
    shot_color = random.choice(colors)
    # 弾の生成
    for y in range(num_of_targets):
        t = turtle.Turtle()
        t.ht()
        t.penup()
        t.sety(250)
        t.setx(0)
        t.color(shot_color)
        t.shape("square")
        t.shapesize(1)
        t.st()
        t.speed(1)
        t.goto(pos + y, 320)
        t.seth(180)
        targets.append(t)

def isexist():
    for t in targets:
        if t.xcor() >= -350 + count*2 and 350 >= t.xcor() and t.ycor() >= -350 and 350 >= t.ycor():
            return False
        else :
            t.ht()
    return True

def attack_spread(i, t, angle):
    # 弾道を拡散に
    t.seth(angle + (i - 3) * 10)
    t.forward(7)
    t.tilt(3)

def deg_own_shot(t):
    # 弾と自機の角度を求める
    xt = t.xcor()
    yt = t.ycor()
    xown = my_turtle.xcor()
    yown = my_turtle.ycor()
    v_x = 0
    v_y = 0
    if xt >= xown:
        v_x = abs(xt - xown)
    else :
        v_x = abs(xown - xt)
    if yt >= yown:
        v_y = abs(yt - yown)
    else :
        v_y = abs(yown - yt)
    print("(v_x, v_y) = (" + str(v_x) + "," + str(v_y) + ")")
    rad = math.atan2(v_y, v_x)
    deg = math.degrees(rad)
    if xt < xown :
        return 360 - deg
    else :
        return 180 + deg

def attack_ownaim(i, t):
    # 弾道を自機狙いに
    if t.heading() == 180:
        angle = deg_own_shot(t)
        t.seth(angle)
        print("ownshot angle = " + str(angle))
    t.forward(8 - i*0.5)
    t.tilt(3)

def game():
    global count
    global pattern

    if isexist() :
        targets.clear()
        count += pattern
        if count >= 18:
            pattern = random.randint(1,5)
            count = pattern + random.randint(0, 3)
    if len(targets) == 0:
        if count%2 == 0:
            make_shot(-100)
        else :
            make_shot(100)
    for i, t in enumerate(targets):
        if count%3 == 0:
            attack_ownaim(i, t)
        else :
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
            my_turtle.seth(90)
            for _ in range(6):
                my_turtle.right(15)
                my_turtle.left(15)
            screen.delay(2)
            time.sleep(1.5)
            time_text.goto(-300, 0)
            time_text.write("ゲームオーバー", font=("helvetica", 60))
            my_turtle.ht()
            screen.update()
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
pattern = 1

game()

screen.mainloop()
