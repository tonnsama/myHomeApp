import sys
import os
import time
from keyLock import lock, unlock


state_file = os.path.dirname(os.path.abspath(__file__)) + '/key_state'
active_file = os.path.dirname(os.path.abspath(__file__)) + '/active_state'

lock()

while True:

	with open(active_file, 'r') as f:
		active = int(f.read())

	if active:
		print('active')
		with open(state_file, 'r') as f:
			state = int(f.read())

		if state == 1:
			print('unlocking')
			unlock()
			with open(state_file, 'w') as f:
				f.write('0')
		elif state == 0:
			print('locking')
			lock()
			with open(state_file, 'w') as f:
				f.write('1')
		with open(active_file, 'w') as f:
			f.write('0')

	time.sleep(0.1)
