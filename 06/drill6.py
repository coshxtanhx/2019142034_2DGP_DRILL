from pico2d import *
from math import *

def deg_2_rad(deg):
    return deg / 180 * pi

open_canvas()

grass = load_image('grass.png')
chrc = load_image('character.png')

grass.draw_now(400, 30)
chrc.draw_now(0, 90)

x = 400
y = 90
deg = 0
move_flag = 0; # 0: 네모 / 1: 원운동
while(1):
    clear_canvas_now()
    grass.draw_now(400, 30)
    chrc.draw_now(x, y)
    if move_flag == 0:
        if y == 90 and x < 800:
            x += 4
        elif x == 800 and y < 600:
            y += 3
        elif y == 600 and x > 0:
            x -= 4
        elif x == 0 and y > 90:
            y -= 3
    else:
        x = 210 * cos(deg_2_rad(deg + 270)) + 400
        y = 210 * sin(deg_2_rad(deg + 270)) + 300
        deg += 4
    if(deg == 360):
        deg = 0
        move_flag = 0
        x, y = 400, 90
    elif (move_flag == 0 and x == 400 and y == 90):
        move_flag = 1

    delay(0.01)
