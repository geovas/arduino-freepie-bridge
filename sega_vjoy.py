from serial import Serial
global a

if starting:
	global a
	starting = False
	a = Serial()
	a.port = 'COM6'
	a.open()
	
	vJoy[0].setButton(0,False)
	vJoy[0].setButton(1,False)
	vJoy[0].setButton(2,False)
	vJoy[0].setButton(3,False)

	vJoy[0].setButton(4,False)
	vJoy[0].setButton(5,False)
	vJoy[0].setButton(6,False)
	vJoy[0].setButton(7,False)
	

ans = ord( a.read(1) ) 

if (ans & 0x40):
	vJoy[0].setButton(0,not (ans & 0x01)) # Right
	vJoy[0].setButton(1,not (ans & 0x02)) # Left
	vJoy[0].setButton(2,not (ans & 0x04)) # Down
	vJoy[0].setButton(3,not (ans & 0x08)) # Up
	vJoy[0].setButton(4,not (ans & 0x10)) # C
	vJoy[0].setButton(5,not (ans & 0x20)) # B
	

else:
	vJoy[0].setButton(7,not (ans & 0x10)) # A
	vJoy[0].setButton(6,not (ans & 0x20)) # Start
