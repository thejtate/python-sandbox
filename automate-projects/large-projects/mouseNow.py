#! python3
# mouseNow.py - Displays the mouse cursor's current position.

import pyautogui

print('Press Ctrl-C to quit.')

try:
	while True:
		# Get and print the mouse coordinates
		x,y = pyautogui.position()
		positionStr = 'X: '+str(x).rjust(4)+'| Y: '+str(y).rjust(4)
		pixelColor = pyautogui.screenshot().getpixel((x,y))

		positionStr += 'RGB: (Red - '+str(pixelColor[0]).rjust(3)
		positionStr += ', Green - '+str(pixelColor[1]).rjust(3)
		positionStr += ', Blue - '+str(pixelColor[2]).rjust(3)+')'

		print(positionStr, end='')
		print('\b' * len(positionStr), end='', flush=True)

except KeyboardInterrupt: 
	print('\nDone')