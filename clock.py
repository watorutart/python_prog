import datetime
import turtle

screen = turtle.Screen()
screen.setup(450, 350)
screen.tracer(0) # 画面のちらつきを防止。ただしタートルの移動などのアニメーションが行われなくなる

time_turtle = turtle.Turtle()
time_turtle.hideturtle()
time_turtle.setposition(-150, -80)

date_turtle = turtle.Turtle()
date_turtle.penup()
date_turtle.hideturtle()
date_turtle.setposition(-170, 30)

weekdays = ["月", "火", "水", "木", "金", "土", "日"]

def clock():
    now = datetime.datetime.now()
    wday = weekdays[now.weekday()]

    date = f"{now.year:}年{now.month}月{now.day}日({wday})"
    date_turtle.clear()
    date_turtle.write(date, font=("helvetica", 30))

    time = f"{now.hour:02d}:{now.minute:02d}:{now.second:02d}"
    time_turtle.clear()
    time_turtle.write(time, font=("helvetica", 50))

    screen.ontimer(clock, 100)

clock()
screen.mainloop()
