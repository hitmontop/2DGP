from pico2d import *
from math import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x=400
y=90

init_x=400
init_y=300
r=210
degree = 90

while True:
    while x<800:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x=x+5
        delay(0.01)
        
    while y<600:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y=y+5
        delay(0.01)

    while x>0:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x=x-5
        delay(0.01)

    while y>90:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y=y-5
        delay(0.01)

    while x<400:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x=x+5
        delay(0.01)

    while (degree <= 450):          
        x= 400 + cos(radians(degree))*r
        y= 300 - sin(radians(degree))*r
        
        degree= degree+10
       
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        
        delay(0.01)
        
    degree=90
