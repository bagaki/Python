
from view import view
from atm import ATM
from users import Users


def func(view, atm, user):
	view.sysInterface()
	c = input("Please input business:")
	if c == "1":
		return user.checkMoney(atm)
	elif c == "2":
		return user.getMoney(atm)
	elif c == "3":
		return user.saveMoney(atm)
	elif c == "4":
		return user.trandferMoney(atm)
	elif c == "5":
		return user.changePwd(atm)
	elif c == "6":
		return user.unlockAccount(atm)
	elif c == "7":
		return user.closeAccount(atm)
	elif c == "q":
		if user.exitSys(atm):
			return True
	else:
		print("The input is wrong")


def main():
	# 管理员登录为'admin'，密码为'123'
	view = View("admin", "123")
	view.initface()
	atm = ATM()
	view.login()
	user = Users()
	while True:
		view.sysInit()
		c = input("Please input business: ")
		if c == "1":
			user.createAccount(atm)
		elif c == "2":
			if user.log(atm):
				while True:
					if func(view, atm, user) == None:
						continue
					else:
						break
		elif c == "3":
			user.findBackPwd(atm)
		elif c == "4":
			user.lockAccount(atm)
		elif c == "T":
			if user.exitSys(atm):
				# 管理员注销系统
				if view.logout():
					return True
		else:
			print("The input have something wrong")




if __name__ == "__main__":
	main()
