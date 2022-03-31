import sense_hat
s = sense_hat.SenseHat()
from math import pi
from math import sin
from time import sleep
from random import randint

def random_colour():
    return [randint(0, 255),randint(0, 255),randint(0, 255)]

def xy(x,y, c):
    n = (x/7) * 2*pi
    intensity = (sin(y+c+n-pi/4)+1) / 2
    return tuple(int(intensity*colour) for colour in random_colour)

rand = randint(0,100) 
print(rand)
if rand != 5:
    exit()

c = 0
random_colour = random_colour()
while(c<16):
    pix = [[0]*8]*8
    for x in range(0, 8):
        for y in range(0, 8):
            r,g,b = xy(x,y, c)
            s.set_pixel(x,y, r,g,b)
    c+=1
    sleep(0.06)
    s.clear()
