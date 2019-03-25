import os.path
import turtle
import random

my_turtle = turtle.Turtle()
my_turtle.pensize(4)
my_turtle.shapesize(2)
my_turtle.shape("turtle")
screen = turtle.Screen()
screen.title("テキストファイルの読み込み")
screen.setup(600, 600)

dirname = os.path.dirname(__file__)
path = os.path.join(dirname, "tpos.txt")

with open(path, mode='r', encoding="utf8") as f:
    for line in f:
        line = line.rstrip("\n")
        pos = line.split(",")
        if pos[2] == "d":
            my_turtle.pendown()
        else :
            my_turtle.penup()
        x = int(pos[0])
        y = int(pos[1])
        my_turtle.setheading(my_turtle.towards(x, y))
        my_turtle.goto(x, y)
screen.mainloop()
