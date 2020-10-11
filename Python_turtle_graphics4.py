import turtle

tur = turtle.Turtle()
scr=turtle.Screen()
scr.bgcolor('black')
tur.pencolor('white')

tur.speed(0)
tur.penup()
tur.goto(-400,-250)
tur.pendown()

for i in range(500):
    tur.forward(850)
    tur.right(244)

    if i==50:
    	tur.pencolor('red')
    if i==80:
    	tur.pencolor('blue')
    if i==120:
    	tur.pencolor('green')
    if i==150:
    	tur.pencolor('purple')
    if i==190:
    	tur.pencolor('SaddleBrown')
    if i==220:
    	tur.pencolor('OrangeRed')
    if i==260:
    	tur.pencolor('Orchid')
    if i==300:
    	tur.pencolor('Aquamarine')
    if i==350:
    	tur.pencolor('Teal')
    if i==400:
    	tur.pencolor('DarkViolet')
    if i==450:
    	tur.pencolor('Maroon')
    if i==499:
    	tur.pencolor('SlateBlue')

turtle.done()
