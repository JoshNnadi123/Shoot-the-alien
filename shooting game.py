import pgzrun
WIDTH=400
HEIGHT=400
a=Actor("alien")
a.x=200
a.y=200
def draw():
    screen.fill("red")
    a.draw()
pgzrun.go()