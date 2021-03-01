import turtle
A = turtle.Pen()
turtle.bgcolor("blue")
A.speed(0)
S = 2
c = ["red", "pink", "white", "orange", "black", "purple", "grey", "light blue", "dark blue", "cyan"]

for N in range(360):
    A.pencolor(c[N % S])
    A.forward(N * 3 / S + N)
    A.left(360/S + 1)
    A.width(N*S/80)


turtle.done()



