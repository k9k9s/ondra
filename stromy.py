from turtle import *
speed(10)

def listnetystrom():
    forward(20)
    right(90)
    forward(2)
    left(5)
    forward(2)
    left(5)
    forward(2)
    left(5)
    forward(2)
    left(5)
    forward(2)
    left(5)
    forward(2)
    left(5)
    left(5)
    forward(2)
    left(5)
    forward(2)
    left(5)
    forward(2)
    left(5)
    forward(2)
    left(5)
    forward(2)
    left(5)
    left(5)
    forward(2)
    left(5)
    forward(2)
    left(5)
    forward(2)
    left(5)
    forward(2)
    left(5)
    forward(2)
    left(5)
    left(5)
    forward(2)
    left(5)
    forward(2)
    left(5)
    forward(2)
    left(5)
    forward(2)
    left(5)
    forward(2)
    left(5)
    left(5)
    forward(2)
    left(5)
    forward(2)
    left(5)
    forward(2)
    left(5)
    forward(2)
    left(5)
    forward(2)
    left(5)
    left(5)
    forward(2)
    left(5)
    forward(2)
    left(5)
    forward(2)
    left(5)
    forward(2)
    left(5)
    forward(2)
    left(5)
    left(5)
    forward(2)
    left(5)
    forward(2)
    left(5)
    forward(2)
    left(5)
    forward(2)
    left(5)
    forward(2)
    left(5)
    left(5)
    forward(2)
    left(5)
    forward(2)
    left(5)
    forward(2)
    left(5)
    forward(2)
    left(5)
    forward(2)
    left(5)
    left(5)
    forward(2)
    left(5)
    forward(2)
    left(5)
    forward(2)
    left(5)
    forward(2)
    left(5)
    forward(2)
    left(5)
    left(5)
    forward(2)
    left(5)
    forward(2)
    left(5)
    forward(2)
    left(5)
    forward(2)
    left(5)
    forward(2)
    left(5)
    left(5)
    forward(2)
    left(5)
    forward(2)
    left(5)
    forward(2)
    left(5)
    forward(2)
    left(5)
    forward(2)
    left(5)
    left(5)
    forward(2)
    left(5)
    forward(2)
    left(5)
    forward(2)
    left(5)
    forward(2)
    left(5)
    left(5)
    forward(2)
    left(5)
    forward(2)
    left(5)
    forward(2)
    right(100)
    forward(24)
    right(90)



def strecha():
    color("red")
    begin_fill()
    left(135)
    forward(21)
    left(90)
    forward(8)
    right(135)
    forward(10)
    left(135)
    forward(5)
    left(45)
    forward(10)
    right(45)
    forward(8)
    end_fill()
    color("black")

def dum():
    strecha()
    #konec strechy
    left(135)
    forward(30)
    right(90)
    forward(30)
    right(90)
    forward(30)
    right(90)
    forward(30)

def strom(kmen):
    #kmen = 250

    forward(5)
    left(90)
    forward(kmen)
    right(90)
    forward(15)
    left(135)
    forward(15)
    right(135)
    forward(10)
    left(135)
    forward(25)
    left(90)
    forward(25)
    left(135)
    forward(10)
    right(135)
    forward(15)
    left(135)
    forward(15)
    right(90)
    forward(kmen)




sd = textinput("blah", "co chceš sakra za tvar ????????????????????????? ")
if sd == ("sd"):
    #dum
    dum()

    #konec domu
    left(180)
    forward(30)
    right(90)
    forward(50)
    left(180)

    strom(5)
    right(90)
    forward(50)
    left(180)

    strom(100)
    right(90)
    forward(50)
    left(180)

    strom(20)
    right(90)
    forward(50)
    left(180)

    strom(25)
    left(90)
    forward(280)
    left(90)

    listnetystrom()


exitonclick()