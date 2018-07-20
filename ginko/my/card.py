'''
卡：
类名：Card
属性：卡号、密码、余额、身份证、手机
'''


class Card(object):
    def __init__(self, cardId, pwd, money, IDNum, pheNum, cardLock="False"):
        self.cardId = cardId
        self.pwd = pwd
        self.money = money
        self.IDNum = IDNum
        self.pheNum = pheNum
        self.cardLock = cardLock