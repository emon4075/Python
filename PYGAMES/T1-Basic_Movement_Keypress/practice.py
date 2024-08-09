from pygame import *

init()
window = display.set_mode((430, 700))
display.set_caption("First Game")

x = 20
y = 20

run = True
while run:
    time.delay(100)
    for e in event.get():
        if e.type == QUIT:
            run = False
    