'''
功能：读取文件cardInfo.txt的信息
方法：读、写、删
'''


from card import Card
import json


# read
class ReadCard(Card):
    def __init__(self, cardId='', pwd='', money=0, IDNum='', pheNum='', cardLock=''):
        Card.__init__(self, cardId, pwd, money, IDNum, pheNum, cardLock)

    def dict2Card(self, d):
        return self.__class__(d['cardId'], d['pwd'], d['money'], d['IDNum'], d['pheNum'], d['cardLock'])

    def read(self):
        # card对象转为字典
        with open('userInfo.txt', 'r', encoding='utf-8') as f:
            cards = []
            for re in f.readline():
                cards.append(self.dict2Card(eval(re)))
        return cards


# 写
class AppendCard(Card):
    def __init__(self):
        Card.__init__(self, cardId='', pwd='', money=0, IDNum='', pheNum='', cardLock='')

    def card2Dict(self, card):
        return {'cardId': card.cardId, 'pwd': card.pwd,
                'money': card.money, 'IDNum': card.IDNum,
                'pheNum': card.pheNum, 'cardLock': card.cardLock}

    def append(self, card, w='a'):
        # 默认时追加，如果w='w'就清空文件
        if w == 'w':
            with open('userInfo.txt', 'w', encoding='utf-8') as f:
                f.write('')
        else:
            with open('userInfo.txt', 'a', encoding='utf-8') as f:
                f.write('\n')

# 删
class Del(object):
    def del_(self, cardId):
        readcard = ReadCard()
        cards = readcard.read()
        for card in cards:
            # 删除输入的卡号
            if cardId == card.cardId:
                cards.remove(card)
                break
        else:
            print('This card number is not excit!')
            return False
        # 重新写入文件
        appendCard = AppendCard()
        appendCard.append('', w='w')
        for card in cards:
            appendCard.append(card)
        return True