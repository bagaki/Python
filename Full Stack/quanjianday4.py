li = ['tomoya','taiichi','mabo','shigeko']

while 1:
	np = input("Please input the new: ")
	if np.strip().upper() == "Q":
		break
	else:
		li.append(np)
	print(li)