import time
from threading import Timer


def func():
    print('time the same')

while True:
    t = Timer(5, func).start()
    time.sleep(5)