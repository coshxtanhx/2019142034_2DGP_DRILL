from pico2d import *
# import game_world

PIXEL_PER_METER = (10.0 / 0.3) # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

def convert_dir_int_to_str(idir):
    sdir = ''
    if(idir == -1):
        sdir = 'h'
    return sdir

def frame_to_grid(f):
    w, h = 182, 169
    x = w * (f % 5)
    y = h * (2 - (f // 5))
    return x, y, w, h

class Bird:
    image = None

    def __init__(self, x = 400, y = 300, d = 1):
        if Bird.image == None:
            Bird.image = load_image('bird_animation.png')
        self.x, self.y = x, y
        self.frame = 0
        self.direction = d

    def draw(self):
        self.image.clip_composite_draw(*frame_to_grid(int(self.frame)), \
            0.0, convert_dir_int_to_str(self.direction)\
                , self.x, self.y, 182, 169)

    def update(self):
        import game_framework
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        # self.x += self.velocity
        self.x += self.direction * RUN_SPEED_PPS * game_framework.frame_time
        if self.x < 25:
            # game_world.remove_object(self)
            self.direction = 1
        elif(self.x > 1000 - 25):
            self.direction = -1
