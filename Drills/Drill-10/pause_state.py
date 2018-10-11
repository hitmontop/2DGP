import game_framework
from pico2d import*
import main_state

name = "PauseState"
pause_button = None

class PauseButton:
    def __init__(self):
        self.image = load_image('pause.png')

    def draw(self):
        self.image.draw(400, 300)

    def update(self):
        pass


def enter():
    global pause_button
    pause_button = PauseButton()



def exit():
    global pause_button
    del(pause_button)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
                game_framework.pop_state()


def draw():
    clear_canvas()
    pause_button.draw()
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass

