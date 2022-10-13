from pico2d import *
from play_state import *

boy = None
grass = None
running = None
# 초기화
def enter():
    global boy, grass, running
    boy = Boy()
    grass = Grass()
    running = True
# 종료
def exit():
    global boy, grass
    del boy
    del grass

def update():
    boy.update()

def draw():
    clear_canvas()
    grass.draw()
    boy.draw()
    update_canvas()
open_canvas()
enter()