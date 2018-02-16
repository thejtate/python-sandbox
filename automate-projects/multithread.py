#! python3
# Simple example of multithreading

import time, threading 

def takeANap():
	time.sleep(7)
	print('Wake up!')

threadObj = threading.Thread(target=takeANap)
threadObj.start()

print('End of program.')