from pico2d import *
open_canvas()

character = load_image('animation_sheet.png')

def move_to_1():
    pass

def move_to_2():
    x, y = 203, 535
    x2, y2 = 132, 243

    frame = 0
    dir = x2-x
    # s = (x2-x) / (y2-y)
    # d = ((((x2-x)**2) / ((y2-y)**2))**0.5)/10
    dx = (x2-x)/10.0
    dy = (y2-y)/10.0

    while x > 132:
        clear_canvas_now()
        if dir >= 0:
            character.clip_draw(frame * 100, 100, 100, 100, x, y)
        else:
            character.clip_draw(frame * 100, 0, 100, 100, x, y)

        update_canvas()
        frame = (frame + 1) % 8
        x += dx
        y += dy


        delay(0.01)

def move_to_3():
    pass
def move_to_4():
    pass
def move_to_5():
    pass
def move_to_6():
    pass
def move_to_7():
    pass
def move_to_8():
    pass
def move_to_9():
    pass
def move_to_10():
    pass

def make_character_move():
    move_to_1()
    move_to_2()
    move_to_3()
    move_to_4()
    move_to_5()
    move_to_6()
    move_to_7()
    move_to_8()
    move_to_9()
    move_to_10()

while True:
    make_character_move()



close_canvas()
