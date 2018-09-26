from multiprocessing import Manager, Process, Lock


# def main(dic):
#     dic['count'] -= 1
#     print(dic)
#
#
# if __name__ == '__main__':
#     m = Manager()
#     dic = m.dict({'count':100})
#     p_lst = []
#     p = Process(target=main, args=(dic,))
#     p.start()
#     p.join()
#     print('主进程：', dic)


def main(dic, lock):
    lock.acquire()
    dic['count'] -= 1
    lock.release()


if __name__ == '__main__':
    m = Manager()
    lock = Lock()
    dic = m.dict({'count':100})
    p_lst = []
    for i in range(50):
        p = Process(target=main, args=(dic, lock))
        p.start()
        p_lst.append(p)
    for i in p_lst:
        i.join()
    print('主进程：', dic)