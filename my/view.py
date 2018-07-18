# coding:utf-8


'''
管理员界面
类名： View
属性：账号、密码
行为：管理员初始化界面   管理员登录   系统功能界面   管理员注销

系统功能：开户、查询、取款、存款、转账、改密、销户、退出
'''


from check import Check
import time


class View(object):

    def __init__(self, admin, pwd):
        self.admin = admin
        self.pwd = pwd

    def initface(self):
        print("--------------------------------------")
        print("                                      ")
        print("            loading......             ")
        print("                                      ")
        print("--------------------------------------")
        time.sleep(1)
        return

    # 登录界面
    def login(self):
        print("--------------------------------------")
        print("                                      ")
        print("            Admin login.....          ")
        print("                                      ")
        print("--------------------------------------")

        check = Check()
        check.userName(self.admin, self.pwd)

        print("--------------Login success-----------")
        print("          Please wait a moment...     ")
        del check
        time.sleep(1)
        return

    # 退出界面
    def logout(self):
        print("--------------------------------------")
        print("                                      ")
        print("            Admin logout....          ")
        print("                                      ")
        print("--------------------------------------")

        # 确认是否退出
        check = Check()
        if not check.isSure("退出"):
            return False

        check.userName(self.admin, self.pwd)
        print("-------------Logout success-----------")
        print(" It is closing...Please wait a moment ")
        del check
        time.sleep(1)
        return True

    # 系统功能界面
    '''
    系统功能：开户、查询、取款、存储、转账、销户、挂失、解锁、改密、退出
    '''
    def sysInit(self):
        print("---------Welcome to My Bank-----------")
        print("*    开户(1)             登录(2)      *")
        print("*    找回密码(3)          挂失(4)      *")
        print("*                        退出(q)      *")
        print("--------------------------------------")

    def sysInterface(self):
        print("---------Welcome to My Bank-----------")
        print("*    查询(1)             取款(2)      *")
        print("*    存款(3)             转账(4)      *")
        print("*    改密(4)             解锁(6)      *")
        print("*    销户(7)             退出(q)      *")
        print("--------------------------------------")