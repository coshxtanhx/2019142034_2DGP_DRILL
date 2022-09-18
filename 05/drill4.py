import turtle

c = 0

turtle.speed(0)

turtle.penup()
turtle.goto(-250, -250)
turtle.pendown()

while(c < 6):
    turtle.forward(500)
    turtle.penup()
    turtle.goto(-250, (c + 1) * 100 - 250)
    turtle.pendown()
    c += 1

turtle.penup()
turtle.goto(-250, -250)
turtle.pendown()
turtle.left(90)
c = 0

while(c < 6):
    turtle.forward(500)
    turtle.penup()
    turtle.goto(-250 + (c+1)*100, -250)
    turtle.pendown()
    c += 1

turtle.exitonclick()
