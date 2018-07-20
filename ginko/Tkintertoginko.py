#!/usr/bin/env python
# coding:utf-8


''''
人
类名： User
属性：姓名  身份证号  电话号  卡
行为：


卡
类名： Card
属性： 卡号  密码  余额
行为：


银行
类名：bank
属性：用户列表  提款机


提款机
类名：ATM
属性：用户字典
行为：开户；查询；取款；存款；转账；改密码；锁定；解锁；补卡；销户


管理员
类名：admin
属性：
行为：管理员界面   管理员验证  系统功能界面
'''

import os
import time
import pickle
import tkinter

from admin import Admin
from atm import ATM


def main():

    # 管理员对象
    admin = Admin()  # 管理员账号

    # 管理员开机
    admin.printAdminView()
    if admin.adminOption():
        return -1

    # # 存储所有用户的信息
    # allUsers = {}

    filePath = os.path.join(os.getcwd(), "allUsers.txt")
    f = open(filePath, 'rb')
    allUsers = pickle.load(f)

    # 提款机对象
    atm = ATM(allUsers)

    while True:
        admin.printSysFunctView()
        # 等待用户操作
        option = input("Please input your option:")
        if option == "1":
            atm.createUsers()

        elif option == "2":
            atm.searchUserInfo()
        elif option == "3":
            atm.withdrawals()
        elif option == "4":
            atm.saveMoney()
        elif option == "5":
            print("转账")
        elif option == "6":
            print("改密")
        elif option == "7":
            atm.lockUser()
        elif option == "8":
            atm.unlockUser()
        elif option == "9":
            print("补卡")
        elif option == "0":
            print("销户")
        elif option == "q":
            if not admin.adminOption():
                # 将当前系统账户信息，保存到文件中

                f= open(filePath, "wb")
                pickle.dump(atm.allUsers, f)
                f.close()
                return -1


        time.sleep(3)






if __name__  ==  '__main__':
    main()