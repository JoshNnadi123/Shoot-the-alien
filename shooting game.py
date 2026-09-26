import pgzrun
import random
WIDTH=400
HEIGHT=400
a=Actor("alien")
a.x=200
a.y=200
msg="Shoot the alien"
def draw():
    screen.fill("red")
    a.draw()
    screen.draw.text(msg,(150,50))
def on_mouse_down(pos):
    global msg
    if a.collidepoint(pos):
        msg="Good Shot"
        a.x=random.randint(0,400)
        a.y=random.randint(0,400)
    else:
        msg="Bad shot"
pgzrun.go()