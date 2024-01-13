from turtle import *

speed(10000000)




color("blue")

def cary(pocet):

    for x in range(-500, pocet+1):
        x1 = (x * x)/500

        xcrtvrt = x1/4
        xzbytek = x1 - xcrtvrt
        xosmina = xcrtvrt/3
        xzbytekosminy = xcrtvrt - xosmina
        xmalinko = xzbytek/30
        xzbytekmalika = xzbytek - xmalinko

        color("purple")
        setheading(90)
        forward(xosmina)
        color("blue")
        forward(xzbytekosminy)
        color("yellow")
        forward(xmalinko)
        color("green")
        forward(xzbytekmalika)
        penup()
        setheading(270)
        forward(x1)
        setheading(0)
        forward(1)
        pendown()



penup()
setpos(-700,-400)
pendown()
cary(499)












exitonclick()