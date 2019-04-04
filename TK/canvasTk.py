from tkinter import *
import random

def random_rectangle(width, height, fill_color):
    x1 = random.randrange(width)
    y1 = random.randrange(width)
    x2 = x1 + random.randrange(width)
    y2 = y1 + random.randrange(height)
    canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color)

tk = Tk()
canvas = Canvas(tk, width=500, height=500)
canvas.pack()
canvas.create_line(0, 0, 500, 500)
canvas.create_rectangle(10, 10, 50, 50)
colors = ["blue", "green", "purple", "pink", "yellow", "orange"]

for _ in range(100):
    color = random.choice(colors)
    random_rectangle(400, 400, color)

tk.mainloop()
