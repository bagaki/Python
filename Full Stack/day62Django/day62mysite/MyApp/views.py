from django.shortcuts import render, HttpResponse, redirect
from MyApp import models

# Create your views here.
def publisher_list(request):
    # 去数据库查出所有的出版社，填充到HTML中，给用户返回
    ret = models.Publisher.objects.all()
    return render(request, "publisher_list.html", {"publisher_list": ret})


def add_publisher(request):
    # 用户第一次来，返回一个填写HTML页面
    return render(request, "add_publisher.html")