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

setpos(0,0)  # nastavi posici na -50, 50
setheading(90)


# nakresli cervenou caru od [10,20] do [100,200]

penup()
setpos (10, 20)
pendown()
color("red")
setpos (100, 200)


## nakresli elipsu

color("green")

import math

a = 150 # ellipse width
b = 90 # ellipse height

#turtle.seth(45)
#turtle.tilt(45)

for i in range(361):
  t = i * (math.pi / 180)
  x = a * math.sin(t)
  y = b * math.cos(t) - b
  #turtle.goto(x,y)
  tilt = 25 * (math.pi / 180)
  x1 = x * math.cos(tilt) + y * math.sin(tilt)
  y1 = x*math.sin(tilt) - y*math.cos(tilt)
  goto(x1,y1)

exitonclick()