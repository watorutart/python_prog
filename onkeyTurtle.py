import turtle
import sys
import os

dirname = os.path.dirname(__file__)
path = os.path.join(dirname, "tpos2.txt")

my_turtle = turtle.Turtle()
screen = turtle.Screen()
screen.setup(600, 600)
screen.title("テキストファイルの書き出し")
my_turtle.pensize(3)
my_turtle.shapesize(2)
my_turtle.shape("turtle")

# タートルの位置
pos = []

def up():
    my_turtle.penup()

def down():
    my_turtle.pendown()

def quit():
    with open(path, mode="w", encoding="utf8") as f:
        for p in pos:
            f.write(f"{int(p[0])},{int(p[1])},{p[2]}\n")
    sys.exit()

def draw_line(x, y):
    if my_turtle.isdown():
        pos.append((x, y, "d"))
    else :
        pos.append((x, y, "u"))
    my_turtle.setheading(my_turtle.towards(x, y))
    my_turtle.setpos(x, y)

screen.listen() # キーイベントを有効にする
screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(quit, "q")
screen.onscreenclick(draw_line)

screen.mainloop()
