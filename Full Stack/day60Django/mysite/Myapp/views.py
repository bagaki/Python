from django.shortcuts import HttpResponse, render, redirect

# Create your views here.


# 定义一个处理/bagaki/的函数
def bagaki(request):
    return render(request, "bagaki.html")


def tomoya(request):
    return HttpResponse("Hello, tomoya!")


def login(request):
    error_msg = " "
    if request.method == "POST":
        email = request.POST.get("email", None)
        pwd = request.POST.get("pwd", None)
        print(email, pwd)
        if email == "bagaki@test.com" and pwd == "079450":
            return redirect("https://www.bilibili.com")
        else:
            error_msg = "The email or password has wrong!"
    return render(request, "login.html", {"error":error_msg})

def tijiao(request):
    # print(request.POST)
    pass


