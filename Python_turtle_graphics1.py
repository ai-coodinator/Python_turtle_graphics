import turtle

tur=turtle.Turtle()
scr=turtle.Screen()
scr.bgcolor('black')
tur.pencolor('white')

x=0
y=20

tur.speed(0)
tur.penup()
tur.pendown()
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
while True:
    tur.pencolor(colors[y%6])
    tur.forward(x)
    tur.right(y)
    x +=3
    y +=1
    if y==300:
        break

tur.hideturtle()
turtle.done()
