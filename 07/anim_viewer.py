from pico2d import *
from math import *

def deg_to_rad(deg):
    return deg / 180 * pi

def update_pack():
    update_canvas()
    delay(0.05)
    get_events()

def renders(x, y, frame, deg):
    img1_ySize = 971
    img1.clip_draw(2 + 72 * (8 - deg // 45), img1_ySize - (127 + 67 * (frame % 7)), 69, 64, x, y)

def go_up(x):
    frame = 0
    for y in range(80, 520+1, 10):
        clear_canvas()
        renders(x, y, frame, 360)
        frame += 1
        update_pack()

def go_down(x):
    frame = 0
    for y in range(520, 80-1, -10):
        clear_canvas()
        renders(x, y, frame, 0)
        frame += 1
        update_pack()

def U_turn_upper(x):
    frame = 0
    for deg in range(360, 1, -45):
        clear_canvas()
        renders(40 + x + 40 * cos(deg_to_rad(deg/2)), 520 + 40 * sin(deg_to_rad(deg/2)), frame, deg)
        frame += 1
        update_pack()

def U_turn_lower(x):
    frame = 0
    for deg in range(360, 721, 45):
        clear_canvas()
        renders(40 + x + 40 * cos(deg_to_rad(deg/2)), 80 + 40 * sin(deg_to_rad(deg/2)), frame, deg-360)
        frame += 1
        update_pack()

def turn_right(x):
    frame = 0
    for deg in range(360, 180-1, -45):
        clear_canvas()
        renders(40 + x + 40 * cos(deg_to_rad(deg/2)), 80 + 40 * sin(deg_to_rad(deg/2)), frame, deg)
        frame += 1
        update_pack()

def do_burrow():
    img1_ySize = 971
    for frame in range(0, 9):
        clear_canvas()
        img1.clip_draw(2 + frame * 63, img1_ySize - 584, 60, 52, 360, 120)
        frame += 1
        update_pack()

def do_unburrow():
    img1_ySize = 971
    for frame in range(0, 6):
        clear_canvas()
        img1.clip_draw(2 + frame * 63, img1_ySize - 638, 60, 50, 360, 120)
        frame += 1
        update_pack()

def array_set(cnt):
    listBase = [0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0]
    return_value = (listBase[0+cnt:7+cnt])
    return_value.reverse()
    return return_value

def do_attack():
    img1_ySize = 971
    for frame in range(0, 19):
        clear_canvas()
        img1.clip_draw(2 + 8 * 63, img1_ySize - 584, 60, 52, 360, 120)
        gasiFrame = array_set(frame)
        for cnt in range(7):
            if(gasiFrame[cnt]):
                img1.clip_draw(3 + (gasiFrame[cnt]-1) * 30, img1_ySize - 805, 20, 33, 360 + 40*(1+cnt), 125)
        frame += 1
        update_pack()

open_canvas()
img1 = load_image('lurker.png')

go_up(160)
U_turn_upper(160)
go_down(160+80)
U_turn_lower(160+80)
turn_right(160+80*2)
do_burrow()
delay(1)
for _ in range(3):
    do_attack()
    delay(0.7)
do_unburrow()

close_canvas()