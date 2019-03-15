import turtle

my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.pensize(4)

screen = turtle.Screen()
screen.setup(600, 600)
screen.title("タートル６")

for _ in range(6):
    my_turtle.circle(100)
    my_turtle.left(60)
screen.mainloop()
