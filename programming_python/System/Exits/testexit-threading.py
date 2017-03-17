import sys
import threading
import time


def action():
    sys.exit()  # or raise SystemExit()
    print('not reached')


threading.Thread(target=action).start()
time.sleep(2)
print('Main exit')
