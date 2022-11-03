from pico2d import *
import game_framework
import game_world
from grass import Grass
from boy import Boy
from ball import Ball


boy = None
grass= None
ball = None

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        else:
            boy.handle_event(event)


# 초기화
def enter():
    global boy, grass, ball
    boy = Boy()
    grass = [Grass(y) for y in (30, 45)]
    ball = None
    game_world.add_object(grass[0], 2)
    game_world.add_object(boy, 1)
    game_world.add_object(grass[1], 0)

# 종료
def exit():
    global boy, grass, ball
    del boy
    del grass
    del ball

def update():
    for game_object_li in game_world.world:
        for game_object in game_object_li:
            game_object.update()

def draw_world():
    for game_object_li in game_world.world:
        for game_object in game_object_li:
            game_object.draw()

def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def pause():
    pass

def resume():
    pass


def test_self():
    import play_state

    pico2d.open_canvas()
    game_framework.run(play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()
