import tkinter

from atm import ATM

def func(self):
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

win = tkinter.Tk()
win.title("bagaki")
win.geometry("400x400+200+20")

# 创建按钮
button = tkinter.Button(win, text="button", command=func,
                        width=10, height=5)
button.pack()

button1 = tkinter.Button(win, text="button", command=func)
button1.pack()

button2 = tkinter.Button(win, text="Quit", command=win.quit)
button2.pack()


win.mainloop()