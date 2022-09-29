from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1000, 600

def set_limits(x,y):
    extra_pixel = 40
    if x < extra_pixel:
        x = extra_pixel
    elif x > KPU_WIDTH - extra_pixel:
        x = KPU_WIDTH - extra_pixel
    if y < extra_pixel:
        y = extra_pixel
    elif y > KPU_HEIGHT - extra_pixel:
        y = KPU_HEIGHT - extra_pixel
    return x, y

def handle_events():
    global running
    global x, y
    global dirx, diry
    global vector, isIdle
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dirx += 1
                vector = 0
                isIdle = False
            elif event.key == SDLK_LEFT:
                dirx -= 1
                vector = 1
                isIdle = False
            elif event.key == SDLK_UP:
                diry += 1
                isIdle = False
            elif event.key == SDLK_DOWN:
                diry -= 1
                isIdle = False
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dirx -= 1
                isIdle = True
            elif event.key == SDLK_LEFT:
                dirx += 1
                isIdle = True
            elif event.key == SDLK_DOWN:
                diry += 1
                isIdle = True
            elif event.key == SDLK_UP:
                diry -= 1
                isIdle = True


open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
vector = 0 # 1은 왼쪽, 0은 오른쪽
isIdle = True
dirx = 0
diry = 0

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    x,y = set_limits(x,y)
    character.clip_draw(frame * 100, 100 - 100 * vector + 200 * isIdle, 100, 100, x, y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    x += dirx * 10
    y += diry * 10
    delay(0.04)

close_canvas()