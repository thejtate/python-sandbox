import pyautogui, time

time.sleep(5)
pyautogui.click()
distance = 500

try: 
	while distance > 0:
		pyautogui.dragRel(distance, 0, duration=0.00001)
		distance -= 5
		pyautogui.dragRel(0, distance, duration=0.00001)
		pyautogui.dragRel(-distance, 0, duration=0.00001)
		distance -= 5 
		pyautogui.dragRel(0, -distance, duration=0.00001)
except KeyboardInterrupt: 
	print('Stopped')