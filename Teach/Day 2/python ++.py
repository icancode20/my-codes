import turtle
A = turtle.Pen()
turtle.bgcolor("black")
A.speed(0)
colors = ["red", "blue", "white"]
for x in range (150):
    A.pencolor(colors[x % 3])
    A.forward(x)
    A.left(120)

A.goto(10,10)
for N in range (200):
    A.pencolor(colors[N % 2])
    A.circle(N)
    A.left(45)


turtle.done()