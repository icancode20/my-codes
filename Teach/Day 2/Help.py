import turtle
A = turtle.Pen()
A.speed(0)
A.pencolor("red")
B = input("What is your name? ")
for x in range (200):
    A.penup()
    A.forward(x)
    A.pendown()
    A.write(B)
    A.left(91)

turtle.done()