import pgzrun
import random
WIDTH=500
HEIGHT=500
e=Actor("dog")
e.x=250
e.y=250
msg="Shoot the dog "
def draw():
    screen.fill("red")
    e.draw()
    screen.draw.text(msg,(150,50))
def on_mouse_down(pos):
    global msg
    if e.collidepoint(pos):
        msg=""
        e.x=random.randint(0,400)
        e.y=random.randint(0,400)
    else:
        msg=""
pgzrun.go()