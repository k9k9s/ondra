from turtle import *
speed(10000)
color("black")

forward(100)

circle(80)  # nakresli kruh o polomeru 80

forward(100)

circle(80, extent = 180)  # nakresli pul-kruh o polomeru 80


setheading(90)  # nastavi sipku nahoru
forward(100)
setheading(180)  # nastavi sipku doleva
forward(100)



# stamp()  # tohle nevim co dela

setpos(-50,50)  # nastavi posici na -50, 50
forward(100)


exitonclick()