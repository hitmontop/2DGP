from pico2d import*
import game_framework
import random

# Boy Run Speed
# fill expressions correctly
PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM/ 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
# fill expressions correctly
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class UpState:
    @staticmethod
    def enter(ghost):
        print("UpState enter")

    @staticmethod
    def exit(ghost):
        pass

    @staticmethod
    def do(ghost):
        distance = game_framework.frame_time * RUN_SPEED_PPS
        ghost.y = ghost.y + distance

        ghost.frame = (ghost.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        ghost.image.opacify(random.randint(0, 100)/100)

        if ghost.y - ghost.py >= PIXEL_PER_METER * 3:
            ghost.add_event(SpinState)


    @staticmethod
    def draw(ghost):
        ghost.image.clip_draw(int(ghost.frame) * 100, 300, 100, 100, ghost.x, ghost.y)


class SpinState:
    @staticmethod
    def enter(ghost):
        print("Spin enter")

    @staticmethod
    def exit(ghost):
        pass

    @staticmethod
    def do(ghost):
        print("Spin do")

    @staticmethod
    def draw(ghost):
        pass



class Ghost:

    def __init__(self, x, y):
        self.px, self.py = x, y
        self.x, self.y = x, y
        self.image = load_image('animation_sheet.png')
        self.frame = 0

        self.event_que = []
        self.cur_state = UpState
        self.cur_state.enter(self)


    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self)
            self.cur_state = event
            self.cur_state.enter(self)

    def draw(self):
        self.cur_state.draw(self)