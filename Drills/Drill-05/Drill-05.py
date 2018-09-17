from pico2d import *
open_canvas()

character = load_image('animation_sheet.png')

def move_p1_to_p2(x, y, x2, y2):

    frame = 0
    direc = x2-x
    # s = (x2-x) / (y2-y)
    # d = ((((x2-x)**2) / ((y2-y)**2))**0.5)/10
    dx = (x2-x)/10.0
    dy = (y2-y)/10.0

    if direc <= 0:
        while x > x2:
            clear_canvas_now()
            character.clip_draw(frame * 100, 0 , 100, 100, x, y)
            update_canvas()
            frame = (frame + 1) % 8
            x += dx
            y += dy
            delay(0.05)

    else:
        while x < x2:
            clear_canvas_now()
            character.clip_draw(frame * 100, 100, 100, 100, x, y)
            update_canvas()
            frame = (frame + 1) % 8
            x += dx
            y += dy
            delay(0.05)


def make_character_move():
    move_p1_to_p2(203, 535, 132, 243)
    move_p1_to_p2(132, 243, 535, 470)
    # move_p1_to_p2(535, 470, 477, 203)
    # move_p1_to_p2(477, 203, 715, 136)
    # move_p1_to_p2(715, 136, 316, 225)
    # move_p1_to_p2(316, 225, 510, 92)
    # move_p1_to_p2(510, 92, 692, 518)
    # move_p1_to_p2(692, 518, 682, 336)
    # move_p1_to_p2(682, 336, 712, 349)
    # move_p1_to_p2(712, 349, 203, 535)


while True:
    make_character_move()



close_canvas()
