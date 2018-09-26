from multiprocessing import Process


def func():
    num = input('>>> ')
    print(num)


if __name__ == '__main__':
    Process(target=func).start()


# 子进程里不能有input