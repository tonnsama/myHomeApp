import time
from keyLock import lock, unlock


print('locking...')
lock()
time.sleep(2)
print('unlocking...')
unlock()
time.sleep(2)

