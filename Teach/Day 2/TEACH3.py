import turtle
A = turtle.Pen()
A.speed(0)
A.pencolor("red")
for x in range (1, 300):
    A.circle(200)
    A.left(360 / (x))

turtle.done()
