import turtle

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


# スクリーンの設定
screen = turtle.Screen()
screen.setup(650, 650)
screen.title("moveTurtle")

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

screen.mainloop()
