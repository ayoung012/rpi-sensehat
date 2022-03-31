# Runs on Python3
import sense_hat
import sys,tty,termios
class _Getch:
    def __call__(self):
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(3)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch


s = sense_hat.SenseHat()
s.rotation = 270

x = 0
y = 0

def arrow_key():
        inkey = _Getch()
        while(1):
                k=inkey()
                if k!='':break
        if k=='\x1b[A':
                return "up"
        elif k=='\x1b[B':
                return "down"
        elif k=='\x1b[C':
                return "right"
        elif k=='\x1b[D':
                return "left"
        else:
                print(k)
                print("not an arrow key!")
                s.clear()
                quit()

def xy(e, x,y):
    
    mv = {'left': (7,0),
            'right': (1,0),
            'down': (0,1),
            'up': (0,7),
            'middle':(0,0)}
    dx,dy = mv[e]
    x = (x + dx)%8
    y = (y + dy)%8
    return x,y

while(True):
    x,y = xy( arrow_key(), x,y)
    s.set_pixel(x,y, 100,100,100)
    pix = s.get_pixels()

    for i in range(0, len(pix)):
        for j in range(3):
            if pix[i][j] > 0:
                pix[i][j] -= 1

    s.set_pixels(pix)

