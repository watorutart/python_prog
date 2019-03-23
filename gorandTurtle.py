import turtle
import math
import random

my_turtle = turtle.Turtle()
screen = turtle.Screen()
screen.setup(600, 600)
my_turtle.pensize(2)
my_turtle.shapesize(2)
my_turtle.shape("turtle")

X_LIMIT = 300
Y_LIMIT = 300
all_pos = []

for _ in range(20):
    all_pos.append((random.randint(-X_LIMIT, X_LIMIT), random.randint(-Y_LIMIT, Y_LIMIT)))

# 原点に近い座標順に並び替え
all_pos.sort(key=lambda p: math.sqrt(pow(p[0], 2) + pow(p[1], 2)))

for pos in all_pos:
    my_turtle.setheading(my_turtle.towards(pos))
    my_turtle.goto(pos)

screen.mainloop()
