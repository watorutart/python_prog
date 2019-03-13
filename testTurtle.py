# encoding utf-8

import turtle

# タートルを生成
my_turtle = turtle.Turtle()
# スクリーンを取得
screen = turtle.Screen()
screen.setup(800, 800)
screen.title("タートル")

my_turtle.shape("turtle")
my_turtle.pensize(4)

# タートルを動かす
my_turtle.forward(150)
my_turtle.left(90)
my_turtle.forward(150)
my_turtle.right(90)
my_turtle.forward(150)
my_turtle.left(90)
my_turtle.forward(150)

screen.mainloop()
