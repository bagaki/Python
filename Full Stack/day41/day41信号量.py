import time
from threading import Semaphore, Thread


def func(sem, a,b):
    sem.acquire()
    time.sleep(1)
    print(a + b)
    sem.release()


sem = Semaphore(4)
for i in range(10):
    t = Thread(target=func, args=(sem, i, i+5))
    t.start()