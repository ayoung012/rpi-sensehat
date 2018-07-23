# Runs on Python3
import sense_hat
s = sense_hat.SenseHat()

x = 0
y = 0

def xy(e, x,y):
    
    mv = {'left': (7,0),
            'right': (1,0),
            'down': (0,1),
            'up': (0,7),
            'middle':(0,0)}
    if(e.action == 'pressed'):
        dx,dy = mv[e.direction]
        x = (x + dx)%8
        y = (y + dy)%8
    return x,y

while(True):
	x,y = xy( s.stick.wait_for_event(), x,y)
	s.set_pixel(x,y, 100,100,100)
