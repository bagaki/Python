'''
验证：
用户名、密码、卡号、身份证、手机
'''


import re
import tkinter


win = tkinter.Tk()
win.title("bagaki")
win.geometry("400x400+200+20")

class Check(object):
    def __init__(self):
        pass

    # 用户验证
    def userName(self, admin, password):
        self.admin = admin
        self.pwd = password
        while True:
            user = input("Please input user name: ")
            pwd = input("Please input user password: ")
            if user != self.admin or pwd != self.pwd:
                print("The user name or password is wrong! Please input again!")
                continue
            else:
                return

    # 是否确认某操作
    def isSure(self, operate):
        while True:
            ms = input("Please make sure {}Yes/No]".format(operate))
            if ms not in ['yes', 'no']:
                print("输入有误，请重新输入!!!")
                continue
            elif ms == 'yes':
                return True
            else:
                return False

    # 手机验证
    def phoneInput(self):
        # 简单的手机验证：开头为1且全部为数字，长度为11位
        while True:
            pn = input("Please input your phone number: ")
            res = re.match(r"^1\d{10}", pn)
            if not res:
                print("The phone is wrong! Please input again!")
                continue
            return pn

    # 身份证验证
    def IDNumInput(self):
        # 简单的身份证验证：长度为16位
        while True:
            idn = input("Please input your ID number: ")
            res = re.match(r"^1\d{5}", idn)
            if not res:
                print("The ID number is wrong! Please input again!")
                continue
            return idn

    # 卡号是否存在
    def isCardExist(self, cards, cardId):
        for card in cards:
            if cardId == card.cardId:
                return card
        else:
            return False

    # 卡号和密码是否一致
    def isCPr(self, cards, cardId, pwd):
        card = self.isCardExist(cards, cardId)
        if card:
            if card.pwd == pwd:
                return card
        return False

    # 密码二次确认
    def pwdCheckAgain(self,newPwd, oldPwd):
        if newPwd == oldPwd:
            return True
        else:
            return False

    # 卡号完整信息验证
    def cardMsgCheck(self, card, ope):
        pheNum = input("Please input your phone number: ")
        idn = input("Please input your ID number:")
        if card.pheNum == pheNum and card.idn == idn:
            return True
        print("{} is false!!\n The phone number or ID number is not the same!".format(ope))
        return False

    # 卡号是否锁定
    def cardLock(self, card):
        if card.cardLock == "True":
            print("This card was locked")
            return True

    # 输入金额验证
    def moneyInput(self, ope):
        mon = input("input {} money (at least $100)".format(ope))
        # 输入的钱必须时100的倍数
        if re.match(r"[1-9]\d*[0]{2}", mon):
            return int(mon)
        print("The input is wrong! The input money number should be at least $100!\n Please input again!")
        return False

    # 改密码
    def newPwdIpt(self):
        while True:
            npwd = input("Please input your new password: ")
            if not re.match(r"\d{6}", npwd):
                print("The password should be 6 number!")
                continue
            npwdagain = input("Please input your new password again: ")
            if self.pwdCheckAgain(npwd, npwdagain):
                break
            else:
                print("The password is not the same")
                continue
        return npwd




# button1 = tkinter.Button(win, text="button", command=Check.isSure).place(x=50, y=300)
# # button1.pack()
#
# button2 = tkinter.Button(win, text="Quit", command=win.quit)
# button2.pack()
#
# win.mainloop()