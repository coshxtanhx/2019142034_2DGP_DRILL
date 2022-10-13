from pico2d import *

import game_framework

image = None

def enter():
    global image
    image = load_image('title.png')

def exit():
    global image
    del image

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                import logo_state
                game_framework.change_state(logo_state)
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                import play_state
                game_framework.change_state(play_state)

def draw():
    clear_canvas()
    image.draw(400,300)
    update_canvas()

def update():
    pass

def pause():
    pass

def resume():
    pass






