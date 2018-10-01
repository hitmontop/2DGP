from pico2d import*
import random
open_canvas()

background = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

W, H = 800, 600
frame = 0
x, y = 0, 0

def draw_line(p1, p2):
    global x, y
    global frame
    for i in range(0, 100+1, 2):
        t = i/100
        x = (1-t)*p1[0]+t*p2[0]
        y = (1-t)*p1[1]+t*p2[1]
        frame = (frame+1) % 8

        if p2[1]-p1[1] >= 0:
            char_runs_right()
        else:
            char_runs_left()


def char_runs_right():
    global x, y
    global frame
    clear_canvas()
    background.draw(W//2,H//2)
    character.clip_draw(frame*100,100,100,100,x, y)
    update_canvas()

    get_events()

def char_runs_left():
    global x, y
    global frame
    clear_canvas()
    background.draw(W // 2, H // 2)
    character.clip_draw(frame * 100, 0, 100, 100, x, y)
    update_canvas()

    get_events()
size = 6
points = [(random.randint(300, 600), random.randint(300, 600)) for i in range(size)]
n = 1

while True:
    draw_line(points[n-1], points[n])
    n = (n+1) % size

