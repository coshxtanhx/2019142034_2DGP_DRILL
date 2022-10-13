import pico2d
import play_state
import game_framework

image = None

def enter():
    global image
    image = pico2d.load_image('add_delete_boy.png')

def exit():
    global image
    del image

def update():
    pass

def draw():
    pico2d.clear_canvas()
    play_state.draw_world()
    image.draw(400, 300)
    pico2d.update_canvas()

def handle_events():
    events = pico2d.get_events()
    for event in pico2d.get_events():
        if event.type == pico2d.SDL_QUIT:
            game_framework.quit()
        elif event.type == pico2d.SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.pop_state()
                case pico2d.SDLK_p:
                    play_state.boys_num += 1
                    play_state.boy.append(play_state.Boy())
                    game_framework.pop_state()
                case pico2d.SDLK_m:
                    if(play_state.boys_num > 1):
                        play_state.boys_num -= 1
                        play_state.boy.pop()
                    game_framework.pop_state()