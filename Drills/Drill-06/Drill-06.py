from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
hand = load_image('hand_arrow.png')
character = load_image('animation_sheet.png')


def handle_events():

    global running
    global x, y
    global click_x, click_y
    global is_char_running

    events = get_events()

    for event in events:

        if event.type == SDL_QUIT:
            running = False

        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, KPU_HEIGHT - 1 - event.y

        elif is_char_running == False:
            if event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
                click_x, click_y = x, y
                is_char_running = True


running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
click_x, click_y = 0, 0
char_x, char_y = 0, 0
is_char_running = False
temp_dir = True
frame = 0
hide_cursor()

def draw_gather():
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, char_x, char_y)
    hand.draw(x, y)
    update_canvas()
    handle_events()

def char_running_right():
    global click_x, click_y
    global char_x, char_y
    global frame
    global is_char_running
    global temp_dir

    temp_dir = True
    dx, dy = (click_x - char_x)/10, (click_y - char_y)/10

    for i in range(0, 10):
        clear_canvas()

        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        character.clip_draw(frame * 100, 100 * 1, 100, 100, char_x, char_y)
        hand.draw(x, y)

        delay(0.05)

        char_x, char_y = char_x + dx, char_y + dy
        frame = (frame + 1) % 8

        update_canvas()
        handle_events()

    is_char_running = False


def char_running_left():
    global click_x, click_y
    global char_x, char_y
    global frame
    global is_char_running
    global temp_dir

    temp_dir = False

    dx, dy = (char_x - click_x) / 10, (char_y - click_y) / 10

    for i in range(0, 10):
        clear_canvas()

        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        character.clip_draw(frame * 100, 0, 100, 100, char_x, char_y)
        hand.draw(x, y)

        delay(0.05)

        char_x, char_y = char_x - dx, char_y - dy
        frame = (frame + 1) % 8

        update_canvas()
        handle_events()

    is_char_running = False


while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)


    if temp_dir:
        character.clip_draw(0, 100, 100, 100, char_x, char_y)
    else:
        character.clip_draw(0, 0, 100, 100, char_x, char_y)
    hand.draw(x, y)

    frame = (frame + 1) % 8

    update_canvas()

    if is_char_running:
        if click_x - char_x >= 0:
            char_running_right()
        else:
            char_running_left()

    handle_events()





