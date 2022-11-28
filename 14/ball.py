import random
from pico2d import *
import game_world

class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.fall_speed = random.randint(0, 1600), 70, 0

    def __del__(self):
        print(454545)

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.y -= (self.fall_speed // 50)

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def handle_collision(self, other, group):
        if group == 'boy:ball':
            game_world.remove_object(self)

class Big_Ball(Ball):
    MIN_FALL_SPEED = 50
    MAX_FALL_SPEED = 200
    image = None
    def __init__(self):
        if Big_Ball.image == None:
            Big_Ball.image = load_image('ball41x41.png')
        self.x, self.y = random.randint(40, 1555), random.randint(400, 500)
        self.fall_speed = random.randint(Big_Ball.MIN_FALL_SPEED, Big_Ball.MAX_FALL_SPEED)

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def handle_collision(self, other, group):
        if group == 'grass:bigball':
            self.y = (other.get_bb())[3] + 20
