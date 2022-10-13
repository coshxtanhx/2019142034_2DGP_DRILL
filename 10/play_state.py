from pico2d import *
import game_framework
import item_state
import boy_num_state

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.dir = 1 # 1: right
        self.image = load_image('animation_sheet.png')
        self.item = None
        self.ball_image = load_image('ball21x21.png')
        self.big_ball_image = load_image('ball41x41.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir * 1
        if self.x > 800:
            self.x = 800
            self.dir = -1
        if self.x < 0:
            self.x = 0
            self.dir = 1

    def draw(self):
        if(self.item == 'Ball'):
            self.ball_image.draw(self.x+10, self.y+50)
        elif(self.item == 'BigBall'):
            self.big_ball_image.draw(self.x+10, self.y+50)

        if(self.dir == 1):
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
                #import title_state
                #game_framework.change_state(title_state)
            elif event.key == SDLK_i:
                game_framework.push_state(item_state)
            elif event.key == SDLK_b:
                game_framework.push_state(boy_num_state)

boy = []
grass = None
running = None

boys_num = 1

# 초기화
def enter():
    global boy, grass, running
    boy += [Boy()]
    grass = Grass()
    running = True
# 종료
def exit():
    global boy, grass
    del boy
    del grass

def update():
    for i in range(boys_num):
        boy[i].update()

def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def draw_world():
    grass.draw()
    for i in range(boys_num):
        boy[i].draw()

def pause():
    pass

def resume():
    pass

enter()