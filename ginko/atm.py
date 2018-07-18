#!/usr/bin/env python
# coding:utf-8


from card import Card
from user import User
import random

class ATM(object):

    def __init__(self, allUsers):
        self.allUsers = allUsers

    def createUsers(self):
        # 目标：向用户字典种添加一对键值对(卡号：用户)
        name = input("Please input your name:")
        idCard = input("Please input id card number:")
        phone = input("Please input phone number:")

        prestor = int(input("Please input prestor number:"))
        if prestor < 0:
            print("prestor number is error! create account is false...")
            return -1

        onePwd = input("Please set your password:")
        # 验证密码
        if not self.checkPwd(onePwd):
            print("Password is wrong!! Create worry...")
            return -1

        # 所有需要的信息就集全了
        cardStr = self.randomCardId()
        # print(cardId)
        card = Card(cardStr, onePwd, prestor)

        user = User(name, idCard, phone, card)
        # 存到字典
        self.allUsers[cardStr] = user
        print("Create success! Please remenber your number ({})".format(cardStr))


    def searchUserInfo(self):

        cardNum = input("Please input your card ID:")
        # 验证是否存在改卡号
        user = self.allUsers.get(cardNum)
        self.checkIDPwd()
        print("Account: {}  Number: {}".format(user.card.cardId, user.card.cardMoney))

    def withdrawals(self):
        cardNum = input("Please input your card ID:")
        # 验证是否存在改卡号
        user = self.allUsers.get(cardNum)

        if not user:
            print("This ID is not exit")
            return -1

        # 判断是否被锁定
        if user.card.cardLock:
            print("This card was locked! Please Unlock it...")
            return -1

        # 验证密码
        if not self.checkPwd(user.card.cardPwd):
            print("The password is wrong! get money is false!")
            user.card.cardLock = True
            return -1

        money = int(input("Please input get money number:"))
        if money > user.card.cardMoney:
            print("The money is not enoury! withdrawals is false....")
            return -1

        if money >= 0:
            print("The input number is wrong! withdrawals is false....")
            return -1

        user.card.cardMoney -= money
        print("withdrawals is success! Number in card: {}".format(user.card.cardMoney))

    def saveMoney(self):
        cardNum = input("Please input your card ID:")
        # 验证是否存在改卡号
        user = self.allUsers.get(cardNum)

        if not user:
            print("This ID is not exit")
            return -1

        # 判断是否被锁定
        if user.card.cardLock:
            print("This card was locked! Please Unlock it...")
            return -1

        # 验证密码
        if not self.checkPwd(user.card.cardPwd):
            print("The password is wrong! get money is false!")
            user.card.cardLock = True
            return -1

        money = int(input("Please input save money number:"))
        user.card.cardMoney += money
        print("Svae money is success! Number in card: {}".format(user.card.cardMoney))

    def transferMoney(self):
        pass

    def charngPwd(self):
        pass

    def lockUser(self):
        cardNum = input("Please input your card ID:")
        # 验证是否存在改卡号
        user = self.allUsers.get(cardNum)

        if not user:
            print("This ID is not exit! Lock false")
            return -1

        if user.card.cardLock:
            print("This card was locked! Please unlock....")
            return -1

        # 验证密码
        if not self.checkPwd(user.card.cardPwd):
            print("The password is wrong! Lock is false!")
            return -1

        tempIdCard = input("Please input your ID number:")
        if tempIdCard != user.idCard:
            print("ID number si wrong!! Lock false...")
            return -1

        # locking
        user.card.cardLock = True
        print("Locking ...")

    def unlockUser(self):
        cardNum = input("Please input your card ID:")
        # 验证是否存在改卡号
        user = self.allUsers.get(cardNum)

        if not user:
            print("This ID is not exit")
            return -1

        # 判断是否被锁定
        if not user.card.cardLock:
            print("This card was not locked! Not need to unlock...")
            return -1

        # 验证密码
        if not self.checkPwd(user.card.cardPwd):
            print("The password is wrong! Unlock is false!")
            return -1

        tempIdCard = input("Please input your ID number:")
        if tempIdCard != user.idCard:
            print("ID number is wrong!! Unlock false...")
            return -1

        # 解锁
        user.card.cardLock = False
        print("Unlock is success!")

    def NewCard(self):
        pass

    def killUser(self):
        pass


    # 验证密码
    def checkPwd(self, realPwd):
        for i in range(3):
            tmpPwd = input("Please input your password:")
            if tmpPwd == realPwd:
                return True
        return False

    # 生成卡号
    def randomCardId(self):
        str = ""
        for i in range(6):
            ch = chr(random.randrange(ord('0'), ord('9') + 1))
            str += ch
        # 判断是否重复
        if not self.allUsers.get(str):
            return str

    def checkIDPwd(self):
        cardNum = input("Please input your card ID:")
        # 验证是否存在改卡号
        user = self.allUsers.get(cardNum)

        if not user:
            print("This ID is not exit")
            return -1

        # 判断是否被锁定
        if user.card.cardLock:
            print("This card was locked! Please Unlock it...")
            return -1

        # 验证密码
        if not self.checkPwd(user.card.cardPwd):
            print("The password is wrong! Search is false!")
            user.card.cardLock = True
            return -1