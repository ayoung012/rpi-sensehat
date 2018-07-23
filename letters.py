# Runs on Python3
from sense_hat import SenseHat
from time import sleep
from random import randint
import sys

sense = SenseHat()

sense.rotation = 90

def pick_random_colour():
    return (randint(0, 155),randint(0, 155),randint(0, 155))


while(True):
    for c in sys.argv[1]:
        sense.show_letter(c, pick_random_colour())
        sleep(0.5)
        sense.clear()
        sleep(0.1)
