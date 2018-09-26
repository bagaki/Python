username = input("Please input your name:")
pwd = input("Please input your password:")


with open("userinfo", "r", encoding="utf-8")as f:
    for line in f:
        # print(line.strip())
        u,p = line.strip().split("|")
        if u == username and p == pwd:
            print("success")
            break
    else:
        print("get out")
        