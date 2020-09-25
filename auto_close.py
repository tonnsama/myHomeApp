import time
import os

from keyLock import lock, unlock
from sensor import isClosed

WAIT_TIME = 10
active_file = os.path.dirname(os.path.abspath(__file__)) + '/active_state'

lock()


while True:
	with open(active_file, 'r') as f:
		active = int(f.read())

	if active:

		unlock()

		print('Open the door')
		start = time.time()
		while isClosed():
			if time.time() - start > WAIT_TIME:
				break
			time.sleep(0.1)

		time.sleep(2)
		print('The door is opened. Close the door.')

		while not isClosed():
			time.sleep(0.1)

		time.sleep(1)

		lock()

		print('The door is locked')

		with open(active_file, 'w') as f:
			f.write('0')

	time.sleep(0.1)
