from sense_hat import SenseHat
from time import sleep

circle = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [96, 100, 96], [96, 100, 96], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [96, 100, 96], [96, 100, 96], [96, 100, 96], [96, 100, 96], [0, 0, 0], [0, 0, 0], [0, 0, 0], [96, 100, 96], [96, 100, 96], [0, 0, 0], [0, 0, 0], [96, 100, 96], [96, 100, 96], [0, 0, 0], [96, 100, 96], [96, 100, 96], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [96, 100, 96], [96, 100, 96], [96, 100, 96], [96, 100, 96], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [96, 100, 96], [96, 100, 96], [0, 0, 0], [96, 100, 96], [96, 100, 96], [0, 0, 0], [0, 0, 0], [96, 100, 96], [96, 100, 96], [0, 0, 0], [0, 0, 0], [0, 0, 0], [96, 100, 96], [96, 100, 96], [96, 100, 96], [96, 100, 96], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [96, 100, 96], [96, 100, 96], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

s = SenseHat()
waste = s.get_pressure()
base_intensity = 200
sleep(0.5)

base = s.get_pressure()

while(True):
    pressure = s.get_pressure()

    rel_intensity = pressure / base

    pressure_diff = rel_intensity - float(round(rel_intensity))

    #print(pressure_diff)
    intensity = float(base_intensity) + (pressure_diff * 10)

    print(intensity)
    colour = (int(intensity),0,0)
    s.clear(colour)

