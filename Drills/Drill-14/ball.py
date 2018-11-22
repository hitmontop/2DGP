import random
from pico2d import *
import game_world
import game_framework
import main_state

class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y = random.randint(0, main_state.background.w), random.randint(0, main_state.background.h)

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw(self):
        cx, cy = 800//2 - (main_state.background.window_left + 400 - self.x) , 600//2 - (main_state.background.window_bottom +300 - self.y)
        self.image.draw(cx, cy)


    def update(self):
        pass

