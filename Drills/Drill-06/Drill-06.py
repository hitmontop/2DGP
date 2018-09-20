from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
    global running
    global x, y
    global sx, sy
    global newx, newy
    global is_running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running == False
        elif SDL_MOUSEBUTTONDOWN:
            if is_running == False:
                x1, y1 = x2, y2
                x2, y2= x,y
                is_running = True


open_canvas(KPU_WIDTH,KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

running = True
is_running = False

x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
x1, y1 = KPU_WIDTH // 2, KPU_HEIGHT // 2
x2, y2 = KPU_WIDTH // 2, KPU_HEIGHT // 2

frame = 0

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    hand.draw(x, y)
    update_canvas()
    frame = (frame + 1) % 8

    delay(0.02)
    handle_events()

close_canvas()




