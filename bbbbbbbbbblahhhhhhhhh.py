from turtle import *
speed(10)
color("blue")
pismeno = textinput("blah","co chceš sakra za tvar ????????????????????????? ")
def pismeno_d():
    left(90)
    forward(115)
    right(90)

    for i in range(46):
        forward(4)
        right(4)
    right(176)
    penup()
    forward(75)

def pismeno_n():
    left(90)
    forward(100)
    right(150)
    forward(120)
    left(150)
    forward(100)
    left(180)
    forward(100)

if pismeno == "n":
    pismeno_n()
else:
    pismeno_d()












exitonclick()