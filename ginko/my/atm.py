''''
atm机：
类名：ATM
属性：
行为（被操作）：开户、查询、取款、存款、转账、销户、挂失、解锁、改密、退出
'''

from check import Check
from card import Card
from readappendcard import ReadCard, AppendCard
import random
import time


class ATM(object):

    def __init__(self):
        self.check = Check()
        self.readCard = ReadCard()
        self.appendCard = AppendCard()
        self.cards = self.readCard.read()

    # 显示功能界面
    def funcShow(self, option):
        if option != "Found Back":
            print("--------------------------------------")
            print("                                      ")
            print("        Here is {} option view        ".format(option))
            print("                                      ")
            print("--------------------------------------")
        else:
            print("--------------------------------------")
            print("                                      ")
            print("   Here is found back password view   ")
            print("                                      ")
            print("--------------------------------------")

    # 输入卡号等
    def cardInput(self, option=''):
        while True:
            cardId = input("Please input the card number: ")
            pwd = input("Please input the password: ")
            card = self.check.isCPr(self.cards, cardId, pwd)
            if not card:
                print("The card number or password is wrong!")
                if option == "login" or option == "lock":
                    return False
                else:
                    continue
            else:
                return card

    # 登录
    def login(self):
        self.funcShow("Login")
        return self.cardInput("Login")

    # 找回密码
    def foundBackPwd(self):
        self.funcShow("Found Back")
        cardID = input("Please input your card number: ")
        card = self.check.isCardExist(self.cards, cardID)
        if card:
            if not self.check.cardMsgCheck(card, "Found Back"):
                return
            newpwd = self.check.newPwdIpt()
            index = self.cards.index(card)
            self.cards[index].pwd = newpwd
            self.writeCard()
            print("Found back password is successful! Please login again")
            time.sleep(1)
            return True
        else:
            print("The card is not excit")
        return True

    # 开户
    def newAccount(self):
        self.funcShow("New Account")
        idn = self.check.IDNumInput()
        pn = self.check.phoneInput()
        print("It is creating new account new...Please wait a moment...")
        while True:
            cardId = str(random.randrange(10000, 100000))
            if self.check.isCardExist(self.cards, cardId):
                continue
            else:
                break
        cardPwd = input("Create account is success, please input your new password：")
        card = Card(cardId, cardPwd, 0, idn, pn, "False")
        self.appendCard.append(card)
        print("Here is your card information, Please check again")
        print("Card number:{}, Password:{}, Money:{}".format(cardId, cardPwd, 0))
        self.cards = self.readCard.read()
        time.sleep(3)
        active = input("You can save money new and actived the card.y/n")
        if active == "y":
            self.saveMoney(card)
        elif active == "n":
            return
        return True


    # 查询
    def checkMoney(self):
        self.funcShow("Check")
        if self.check.cardLock(card):
            print("Check is false")
        else:
            print("The number is ￥{}".format(card.money))
            time.sleep(2)

    # 存款
    def saveMoney(self, card):
        self.funcShow("Save Money")
        if self.check.cardLock(card):
            print("The card is locked, Please Unlock first")
        else:
            mon = self.check.moneyInput("Save money")
            c = self.cards.index(card)
            print("Loading...")
            time.sleep(2)
            self.writeCard()
            print("It is success to save money. The totle number is {}".format(self.cards[c].money))
            time.sleep(1)

    # 取款
    def getMoney(self, card):
        self.funcShow("Get Money")
        if self.check.cardLock(card):
            print("The card is locked, Please Unlock first")
        else:
            print("The money is ￥{}".format(card.money))
            mon = self.check.moneyInput("Get Money")
            if mon:
                if mon > card.money:
                    print("The number is more than the card money number, please check again: ￥{}".format(card.money))
                    time.sleep(2)
                else:
                    print("Loading...")
                    time.sleep(2)
                    c = self.cards.index(card)
                    self.cards[index].money -= mon
                    self.writeCard()
                    print("It is success to get money. The card money number is ￥{}".format(self.cards[c].money))
            time.sleep(2)

    # 转账
    def transferMoney(self, card):
        self.funcShow("Transfer Money")
        if self.check.cardLock(card):
            print("The card is locked, Please Unlock first")
            return
        while True:
            aite = input("Please input the other card ID: ")
            if aite == card.cardID:
                print("You cannot transfer money to yourself")
                return 
            aiteExsis = self.check.isCardExist(self.cards, aite)
            if aiteExsis == False:
                print("The card ID is not exsist, Please check again")
                return
            else:
                break

            while True:
                print("The money number is ￥{}".format(card.money))
                mon = self.check.moneyInput("Transfer Money")
                if not mon:
                    return
                if mon > card.money:
                    print("The number is more than the card number ￥{}".format(card.money))
                    return
                else:
                    break

            print("Loading...")
            time.sleep(2)
            c = self.cards.index(card)
            self.cards[c].money -= mon
            co = self.cards.index(aiteExsis)
            self.cards[co].money += mon
            self.writeCard()
            print("Transfer money is success. The mony number ￥{}".format(self.cards[c].money))
            time.sleep(2)

    # 销户
    def closeAcount(self, card):
        self.funcShow("Close Account")
        if self.check.cardMsgCheck(card, "Close Account"):
            return
        if card.money > 0:
            gon = input("The card has money, could you want to get it out: yes/no")
            if gon == "yes":
                self.getMoney()
            else:
                return
        if self.check.isSure("Close Account"):
            self.cards.remove(card)
            self.writeCard()
            print("It is success to Close Account!")
            time.sleep(2)
            return True

    # 挂失
    def lockAcount(self):
        self.funcShow("Lock Account")
        cardcheck = self.cardInput("lock")
        if not cardcheck:
            return
        if cardcheck.cardLock == "True":
            print("The card is locked")
            return
        if not self.check.cardMsgCheck("Lock"):
            return
        if self.check.isSure("Lock"):
            c = self.cards.index(cardcheck)
            self.cards[c].cardLock = "True"
            self.writeCard()
            print("It is Success to Lock")
            time.sleep(2)
            return True

    # 解锁
    def unlockAccount(self, card):
        self.funcShow("Unlock Account")
        if card.cardLock == "False":
            print("The card is Unlock")
            return
        if not self.check.cardMsgCheck("Unlock"):
            return
        c = self.cards.index(card)
        self.cards[c].cardLock = "False"
        self.writeCard()
        print("It is Success to Unlock")
        time.sleep(2)
        return True

    # 改密
    def changePwd(self, card):
        self.funcShow("Change Password")
        if self.check.cardLock(card):
            print("The card is locked, Please Unlock first")
            return
        if self.check.cardMsgCheck(card, "Change Password"):
            return
        while True:
            oldPwd = input("Please input your old password: ")
            if self.check.pwdCheckAgain(oldPwd, card.password):
                break
            else:
                print("The password is wrong")
                return
        newPwd = self.check.newPwdIpt()
        c = self.cards.index(card)
        self.cards[c].password = newPwd
        self.writeCard()
        print("It is success to Change Password. Please sign in again")
        time.sleep(2)
        return True


    # 写入文件
    def writeCard(self):
        self.appendCard.append('', w='w')
        for card in self.cards:
            self.appendCard.append(card)

    # 退出
    def exit(self):
        if self.check.isSure("Quit"):
            return True
        else:
            return False
