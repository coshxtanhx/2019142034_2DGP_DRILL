from pico2d import *
from random import *

TUK_WIDTH, TUK_HEIGHT = 900, 600


def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        # elif event.type == SDL_MOUSEMOTION:
        #     x, y = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass



open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
arrow = load_image('hand_arrow.png')

running = True
sx, sy = TUK_WIDTH // 2, TUK_HEIGHT // 2
x, y = sx, sy
ax, ay = x, y
frame = 0
t = 0
direction = 0 # 1: right 0: left

hide_cursor()

def check_direction(): # 1: right 0: left
    global direction
    if ax > sx:
        return 0
    elif ax < sx:
        return 1
    else:
        return direction

def reset_world():
    global ax, ay
    global sx, sy
    global t
    ax, ay = randint(0, TUK_WIDTH), randint(0, TUK_HEIGHT)
    t = 0
    sx, sy = x, y

def update_world():
    global x, y
    global t
    t += 0.003
    x = (1-t) * sx + t * ax
    y = (1-t) * sy + t * ay
    if t >= 1.0:
        reset_world()

reset_world()

while running:
    update_world()
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    arrow.draw(ax, ay)
    direction = check_direction()
    character.clip_draw(frame * 100, 100 * (1 - direction), 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8

    handle_events()

close_canvas()




