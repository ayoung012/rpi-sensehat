# Only runs on Python 2.7
import socket
import fcntl
import struct
from time import sleep

from sense_hat import SenseHat

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

# print get_ip_address('eth0')
print(get_ip_address('wlan0'))

s = SenseHat()

ip = get_ip_address('wlan0').split(".")

for i in range(0,10):
    count = 0
    for c in ip[3]:
        s.show_letter(c)
        if count is 0:
            s.set_pixel(7,7, 100,100,100)
        count+=1
        sleep(1)
        s.clear()
        sleep(0.1)
