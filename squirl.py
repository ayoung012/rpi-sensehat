from sense_hat import SenseHat
from time import sleep
import random

s = SenseHat()

k = 0
r = 0
g = 0
pi = 0
pu = 0

# determines a position for a coloured pixel

while(True):

    pix = s.get_pixels()

    if k == r:
        r = random.randint(0 if k == len(pix)-1 else k+1, len(pix)-1)
    if k == g:
        #g = random.randint(k, len(pix)-1)
        g = random.randint(0 if k == len(pix)-1 else k+1, len(pix)-1)
    if k == pi:
        pi = 1000
    if k == pu:
        #pu = random.randint(k, len(pix)-1)
        pu = random.randint(0 if k == len(pix)-1 else k+1, len(pix)-1)

    for i in range(0, len(pix)):
        if i == k:
            val = 255
        else:
            if (k % 4) == 0:
                val = max(0,pix[i][j] - 9)
            else:
                val = pix[i][j]

        # red
        for j in range(1):
            pix[i][j] = val
        # blue
        pix[i][2] = 100

        #red
        if i == r:
            pix[r] = [255,0,0]
        #green
        if i == g:
            pix[g] = [0,255,0]
        #purple
        if i == pu:
            pix[pu] = [255,0,255]
        #pink
        if i == pi:
            pix[pi] = [255,100,255]

        #white
        #if i == r and k < 20 or k > 200:
        #    pix[i] = [100,100,100]
    #######################

    s.set_pixels(pix)
    k = (k + 1)%len(pix)
    sleep(0.08)

