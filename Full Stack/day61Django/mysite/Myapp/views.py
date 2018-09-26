from django.shortcuts import HttpResponse, render, redirect
from Myapp import models

# Create your views here.


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


def user_list(request):
    # 利用ORM这个工具去查询数据库，不用自己去查
    ret = models.UserInfo.objects.all()
    print(ret[0].id, ret[0].name)
    return render(request, "user_list.html", {"user_list":ret})
    # return HttpResponse("kakak")


def add_user(request):
    if request.method == "POST":
        new_name = request.POST.get("username", None)
        models.UserInfo.objects.create(name=new_name)
        return redirect("/user_list/")
    return render(request, "add_user.html")