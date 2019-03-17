import turtle

def move_turtle(x, y):
    my_turtle.setheading(my_turtle.towards(x, y))
    my_turtle.goto(x,y)

screen = turtle.Screen()
screen.setup(600, 600)
screen.title("タートル９")

my_turtle = turtle.Turtle()
my_turtle.pensize(5)
my_turtle.shapesize(3)
my_turtle.shape("turtle")

screen.onscreenclick(move_turtle)
screen.mainloop()
