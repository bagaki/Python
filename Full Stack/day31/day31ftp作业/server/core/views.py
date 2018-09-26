import os
import pickle
from core.user import User
from conf import settings


def login(msg):
    # 从userinfo文件里，读取用户名和密码，并验证
    with open(settings.user_info, 'r') as f:
        f.read()
    pass


def register(msg):
    # 创建一个属于这个用的家目录，并记录下来
    # 记录用户的初始磁盘配额
    # 记录文件大小
    # 记录用户当前所在的目录
    user_obj = User(msg['name'])
    pickle_path = os.path.join(settings.pickle_path, msg['username'])
    with open(pickle_path, 'wb') as f:
        pickle.dump(user_obj, f)
    os.mkdir(user_obj.home)

    # 把用户名密码写进userinfo文件里，并记录用户名
    with open(settings.user_info, 'a') as f:
        f.write('{}|{}|{}'.format(msg['username'], msg['password'], pickle_path))
    return True



def upload(msg):
    print(msg)


def download(msg):
    print(msg)