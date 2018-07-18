#!/usr/bin/env python
# coding:utf-8


class Card(object):
    def __init__(self, cardId, cardPwd, cardMoney):
        self.cardId = cardId
        self.cardPwd = cardPwd
        self.cardMoney = cardMoney
        self.cardLock = False