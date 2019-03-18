import turtle

def draw_line(x, y):
    my_turtle.ondrag(None)
    screen.onscreenclick(None)
    my_turtle.setheading(my_turtle.towards(x, y))
    my_turtle.setpos(x, y)
    my_turtle.ondrag(draw_line)
    screen.onscreenclick(move_turtle)

def move_turtle(x, y):
    my_turtle.ondrag(None)
    screen.onscreenclick(None)
    my_turtle.penup()
    my_turtle.setheading(my_turtle.towards(x, y))
    my_turtle.goto(x, y)
    my_turtle.pendown()
    my_turtle.ondrag(draw_line)
    screen.onscreenclick(move_turtle)

screen = turtle.Screen()
screen.setup(600, 600)
screen.title("おえかき")

my_turtle = turtle.Turtle()
my_turtle.pensize(3)
my_turtle.shape("circle")
my_turtle.speed(0)
my_turtle.color("black")

my_turtle.ondrag(draw_line)
screen.onscreenclick(move_turtle)
screen.mainloop()
