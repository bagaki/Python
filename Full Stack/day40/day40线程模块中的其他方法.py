import time
import threading


def wahah(n):
    time.sleep(0.5)
    print(n, threading.current_thread(), threading.get_ident())  # 线程id


for i in range(10):
    threading.Thread(target=wahah, args=(1,)).start()
print(threading.active_count())
print(threading.current_thread())
print(len(threading.enumerate()))