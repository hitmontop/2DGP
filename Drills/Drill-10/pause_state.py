import game_framework
from pico2d import*
import main_state

name = "PauseState"
pause_button = None
pause_time = 0.0

class PauseButton:
    def __init__(self):
        self.image = load_image('pause.png')
        self.frame = 0

    def draw(self):
        if self.frame % 5000 > 0:
            self.image.draw(400, 300)

    def update(self):
        self.frame = (self.frame + 1) % 10000



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
    main_state.draw()
    pause_button.draw()
    update_canvas()


def update():
    pause_button.update()

def pause():
    pass


def resume():
    pass

