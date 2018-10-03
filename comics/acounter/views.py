from django.shortcuts import render, redirect, HttpResponse
from .models import Users,Comics, MainPage
from .models import BookKeep, Search, History
from django.http import JsonResponse


import os
import time
import random
from django.conf import settings
from .Tag.login import LoginForm


# Create your views here.
def test(request):
    return render(request, 'test/index.html')


def myself(request):
    username = Users.objects.all()
    return render(request, 'myself/myself.html', {'title': 'Myself', 'username': username})


def register(request):
    if request.method == "POST":
        userAccount = request.POST.get('userAccount')
        userPasswd = request.POST.get('userPasswd')
        userName = request.POST.get('userName')
        userAddress = request.POST.get('userAddress')
        f = request.FILES['userImg']
        userImg = os.path.join(settings.MDEIA_ROOT, userAccount + '.png')
        with open(userImg, 'wb') as fp:
            for data in f.chunk():
                fp.write(data)
        token = time.time() + random.randrange(1, 1000)
        userToken = str(token)
        user = Users.createuser(userAccount, userPasswd, userName, userAddress, userToken, userImg)
        user.save()

        request.session['username'] = userName
        request.sesion['token'] = userToken
        return redirect('/myself/')
    else:
        return render(request, 'myself/register.html', {'title': 'Register'})


def login(request):
    if request.method == 'POST':
        f = LoginForm(request.POST)
        if f.is_valid():
            nameid = f.cleaned_data['username']
            passwd = f.cleaned_data['passwd']
            try:
                user = Users.objects.get(userAccount = nameid)
                if user.userPasswd != passwd:
                    return redirect('/login/')
            except Users.DoesNotExist as e:
                return redirect('/login/')

            token = time.time() + random.randrange(1, 1000)
            user.userToken = str(token)
            user.save()

            request.session['username'] = user.userName
            request.session['token'] = user.userToken

            return redirect('/myself/')

        else:
            return render(request, 'myself/login.html', {'title': 'Sign In', 'form': f, 'error': f.errors})
    else:
        f = LoginForm()
        return render(request, 'myself/login.html', {'title': 'Sign In', 'form': f})


def checkuserid(request):
    userid = request.POST.get('userid')
    try:
        user = Users.objects.get(userAccount = userid)
        return JsonResponse({'data': 'The Account was registed', 'stattus': 'error'})
    except Users.DoesNotExist as e:
        return JsonResponse({'data': 'Register is OK', 'status': 'success'})


def quit(request):
    logout(request)
    return redirect('/myself/')