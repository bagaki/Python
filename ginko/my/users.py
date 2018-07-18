# coding: utf-8


'''
用户
类名：Users
行为：开户、查询、取款、存储、转账、改密、销户、退出
'''

class Users(object):
    def __init__(self, name='', IDNum='', pheNum='', card=None):
        self.name = name
        self.IDNum = IDNum
        self.pheNum = pheNum
        self.card = card

    # 登录
    def log(self, atm):
        card = atm.login()
        if card:
            self.card = card
            return True
        else:
            return False

    # 开户
    def createAccount(self, atm):
        return atm.createAccount()

    # 找回密码
    def findBackPwd(self, atm):
        return atm.findBackPwd()

    # 查询余额
    def checkMoney(self, atm):
        return atm.checkMoney(self.card)

    # 存钱
    def saveMoney(self, atm):
        return atm.saveMoney(self.card)

    # 取钱
    def getMoney(self, atm):
        return atm.getMoney(self.card)

    # 转账
    def trandferMoney(self, atm):
        return atm.transferMoney(self.card)

    # 销户
    def closeAccount(self, atm):
        return atm.closeAcount(self.card)

    # 挂失
    def lockAccount(self, atm):
        return atm.lockAccount()

    # 解锁
    def unlockAccount(self, atm):
        return atm.unlockAccount(self.card)

    # 改密
    def changePwd(self, atm):
        return atm.charngPwd(self.card)


    # 退出
    def exitSys(self, atm):
        return atm.exit()