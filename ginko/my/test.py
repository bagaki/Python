'''
验证类：
用户名、密码、卡号、身份证、手机号验证
使用正则表达式进行文本搜索
'''
import re

class Check(object):
    def __init__(self):
       pass
    #用户验证
    def userName(self,admin,password):
        self.admin = admin
        self.password = password
        while True:
            admin = input("请输入用户名：")
            password = input("请输入密码：")
            if admin != self.admin or password != self.password:
                print("用户名或密码输入有误，请重新输入!!!")
                continue
            else:
                return

    #是否确认某操作
    def isSure(self,operate):
        while True:
            res = input("是否确认%s?【yes/no】"%operate)
            if res not in ['yes','no']:
                print("输入有误，请重新输入!!!")
                continue
            elif res == 'yes':
                return True
            else:
                return False

    # 手机号验证
    def phoneInput(self):
        # 简单的手机号验证：开头为1且全部为数字，长度为11位
        while True:
            pnum = input("请输入您的手机号：")
            res = re.match(r"^1\d{10}$",pnum)
            if not res:
                print("手机号输入有误,请重新输入!!!")
                continue
            return pnum
    # 身份证号验证
    def identifyInput(self):
        # 简单的身份证号验证：6位，只有最后一可以为x,其余必须为数字
        while True:
            iden = input("请输入您的身份证号(6位数字)：")
            res = re.match(r"\d{5}\d|x$",iden)
            if not res:
                print("身份证号输入有误,请重新输入!!!")
                continue
            return iden

    # 卡号是否存在
    def isCardIdExist(self,cards,cardId):
        for card in cards:
            if cardId == card.cardId:
                return card
        else:
            return False
    # 卡号和密码是否一致
    def isCardAndPasswordSure(self,cards,cardId,password):
        card = self.isCardIdExist(cards,cardId)
        if card:
            if card.password == password:
                return card
        return False

    # 密码二次确认是否正确
    def isPasswordSure(self, newassword,oldpassword):
        if newassword == oldpassword:
            return True
        else:
           return False
    # 卡号完整信息验证
    def isCardInfoSure(self,card,ope):
        phoneNum = input("请输入手机号:")
        iden = input("请输入身份证号：")
        if card.phoneNum == phoneNum and card.identityId == iden:
            return True
        print("%s失败!!!\n密码、手机号或身份证号与卡中绑定的信息不一致!!!"%ope)
        return False

    # 卡号是否锁定
    def isCardLock(self,card):
        if card.cardLock == "True":
            print("此卡已挂失！")
            return True
        return False
    # 输入金额验证
    def moneyInput(self,ope):
        mon = input("输入%s金额(100的倍数)："%ope)
        # 输入的钱必须是100的倍数
        if re.match(r"[123456789]\d*[0]{2}$", mon):
            return int(mon)
        print("输入有误，%s金额必须是100的倍数!请重新输入!!!"%ope)
        return False

    def newPasswordInput(self):
        while True:
            newpassword = input("请输入新密码：")
            if not re.match(r"\d{6}$",newpassword):
                print("密码必须是6位的纯数字!!!")
                continue
            newpasswordAgain = input("请重复输入新密码：")
            if self.isPasswordSure(newpassword, newpasswordAgain):
              break
            else:
                print("两次输入不一致！")
                continue
        return newpassword