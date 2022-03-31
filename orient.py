from sense_hat import SenseHat
s = SenseHat()


while(True):
	o = s.get_orientation()
	pitch = int(o['yaw'])
	for i in range(0,8):
		print(pitch)
	for i in range(0,8):
		s.set_pixel(0,i,[int(pitch/1.42),int(pitch/1.42),int(pitch/1.42)])
