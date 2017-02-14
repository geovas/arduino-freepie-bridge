from serial import Serial
global a

if starting:
	global a
	starting = False
	a = Serial()
	a.port = 'COM6'
	a.open()

ans = ord( a.read(1) ) 

if (ans & 0x40):

	keyboard.setKey(Key.RightArrow, not (ans & 0x01))	   # Right
	keyboard.setKey(Key.LeftArrow,  not (ans & 0x02))	   # Left
	keyboard.setKey(Key.DownArrow,  not (ans & 0x04)) 	   # Down
	keyboard.setKey(Key.UpArrow,	not (ans & 0x08)) 	   # Up

	mouse.leftButton  = not (ans & 0x20)				   # B
	mouse.rightButton = not (ans & 0x10)				   # C

else:
	keyboard.setKey(Key.Space, not (ans & 0x10)) 	 	   # Start
	mouse.middleButton  = not (ans & 0x20)				   # A

