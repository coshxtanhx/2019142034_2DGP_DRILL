import turtle
import random

def order_move_w():
    turtle.stamp()
    turtle.setheading(90)
    turtle.forward(50)

def order_move_a():
    turtle.stamp()
    turtle.setheading(180)
    turtle.forward(50)

def order_move_s():
    turtle.stamp()
    turtle.setheading(270)
    turtle.forward(50)

def order_move_d():
    turtle.stamp()
    turtle.setheading(0)
    turtle.forward(50)

def restart():
    turtle.reset()

turtle.shape('turtle')

turtle.onkey(order_move_w, 'w')
turtle.onkey(order_move_a, 'a')
turtle.onkey(order_move_s, 's')
turtle.onkey(order_move_d, 'd')
turtle.onkey(restart, 'Escape')
turtle.listen()
