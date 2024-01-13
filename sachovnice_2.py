from turtle import *

# nastaveni pozice a smeru
penup()
setpos(0,0)  # nastavi posici na -50, 50
setheading(90)
pendown()

# kresleni
for x in range(0, 9):
    x1 = x * 10
    penup()
    setpos(x1 , 0)
    pendown()
    forward(90)

# nastaveni pozice a smeru
penup()
setpos(0,90)  # nastavi posici na -50, 50
setheading(180)
pendown()

for y in range(0, 10):
    y1 = y * 10

    penup()
    setpos(80, y1)
    pendown()
    forward(90)

left(90)
forward(90)



exitonclick()

