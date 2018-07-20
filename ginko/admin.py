#!/usr/bin/env python
# coding:utf-8

import time


class Admin(object):

    admin = "1"
    password = "123"

    def printAdminView(self):
        print("********************************************************************")
        print("*                                                                  *")
        print("*                                                                  *")
        print("*                       欢迎登录银行！！                            *")
        print("*                                                                  *")
        print("*                                                                  *")
        print("********************************************************************")




    def printSysFunctView(self):
        print("********************************************************************")
        print("*          开户(1)                                  查询（2）       *")
        print("*          取款(3)                                  存款（4）       *")
        print("*          转账(5)                                  改密（6）       *")
        print("*          锁定(7)                                  解锁（8）       *")
        print("*          补卡(9)                                  销户（0）       *")
        print("*                                                   退出(q)         *")
        print("********************************************************************")

    def adminOption(self):
        inputAdmin = input("Please input admin account:")

        if self.admin != inputAdmin:
            print("Account is worry!!")
            return -1
        inputPwd = input("Please input admin password:")
        if self.password != inputPwd:
            print("Password is worry!!")
            return -1

        # 能执行到这说名账号密码正确
        print("Option success! Please waiting...")
        time.sleep(3)
        return 0

