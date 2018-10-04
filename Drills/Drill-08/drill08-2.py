from pico2d import*
import random

open_canvas(800,600)

background = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

W, H = 800, 600
frame = 0
x, y = 0, 0

def draw_curve_4_points(p1, p2, p3, p4):
    global x, y
    global frame

    # draw p4-p1
    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * p4[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p1[0] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p2[0] + (t ** 3 - t ** 2) * p3[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p4[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p1[1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p2[1] + (t ** 3 - t ** 2) * p3[1]) / 2
        if p2[1]-p1[1] >= 0:
            char_runs_right()
        else:
            char_runs_left()


    # draw p2-p3
    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*p1[0] + (3*t**3 - 5*t**2 + 2)*p2[0] + (-3*t**3 + 4*t**2 + t)*p3[0] + (t**3 - t**2)*p4[0])/2
        y = ((-t**3 + 2*t**2 - t)*p1[1] + (3*t**3 - 5*t**2 + 2)*p2[1] + (-3*t**3 + 4*t**2 + t)*p3[1] + (t**3 - t**2)*p4[1])/2
        if p2[1]-p1[1] >= 0:
            char_runs_right()
        else:
            char_runs_left()


    # draw p3-p4
    for i in range(50, 100, 2):
        t = i / 100
        x = (2*t**2-3*t+1)*p2[0]+(-4*t**2+4*t)*p3[0]+(2*t**2-t)*p4[0]
        y = (2*t**2-3*t+1)*p2[1]+(-4*t**2+4*t)*p3[1]+(2*t**2-t)*p4[1]
        if p2[1]-p1[1] >= 0:
            char_runs_right()
        else:
            char_runs_left()


    # draw p4-p1
    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * p3[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p4[0] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p1[0] + (t ** 3 - t ** 2) * p2[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p3[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p4[1] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p1[1] + (t ** 3 - t ** 2) * p2[1]) / 2
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




size = 10
n=0
points = [(random.randint(50, 50), random.randint(550, 550)) for i in range(size)]

while True:
    draw_curve_4_points(points[n], points[n+1],points[n-1],points[n])
    n = (n+1) % size
