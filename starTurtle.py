import turtle

my_turtle = turtle.Turtle()
my_turtle.pensize(2)

screen = turtle.Screen()
screen.title("タートル８")
screen.setup(600, 600)


def star(pos, size=100, color="black"):
    my_turtle.penup()
    my_turtle.goto(pos[0], pos[1])
    my_turtle.pendown()
    my_turtle.color(color)
    for _ in range(5):
        my_turtle.forward(size)
        my_turtle.right(144)

star((0, 0), size=200)
star((100, 200), size=200, color="green")
star((-300, 250), size=250, color="gray")
star((-50, 200), size=100, color="blue")
star((-250, -100), size=300, color="purple")

screen.mainloop()
