from django.shortcuts import render, redirect
from .models import Wheel, Nav, Mustbuy, Shop, MainShow
from .models import FoodTypes, Goods
from .models import User, Cart, Order

from .forms.login import LoginForm
from django.http import HttpResponse
from django.http import JsonResponse

import time
import random
from django.conf import settings
import os

from django.contrib.auth import logout
# Create your views here.


def home(request):
	wheelsList = Wheel.objects.all()
	navList = Nav.objects.all()
	mustbuyList = Mustbuy.objects.all()
	shopList = Shop.objects.all()
	shop1 = shopList[0]
	shop2 = shopList[1:3]
	shop3 = shopList[3:7]
	shop4 = shopList[7:11]
	mainList = MainShow.objects.all()

	return render(request, 'axf/home.html', 
		{'title':'Home','wheelsList':wheelsList,'navList':navList, 'mustbuyList':mustbuyList, 
		'shop1':shop1, 'shop2':shop2, 'shop3':shop3, 'shop4':shop4, 'mainList':mainList})


def market(request, categorysid, cid, sortid):
	leftSlider = FoodTypes.objects.all()
	productList = Goods.objects.filter(categorysid = categorysid)
	if cid == '0':
		productList = Goods.objects.filter(categorysid = categorysid)
	else:
		productList = productList.filter(categorysid = categorysid, childcid = cid)

	# 排序
	if sortid == '1':
		productList = productList.order_by('productnum')
	elif sortid == '2':
		productList = productList.order_by('price')
	elif sortid == '3':
		productList = productList.order_by('-price')
	
	group = leftSlider.get(typeid = categorysid)
	childList = []
	childnames = group.childtypenames
	arr1 = childnames.split("#")
	for str in arr1:
		# ALL:0
		arr2 = str.split(":")
		obj = {"childName":arr2[0], "childId":arr2[1]}
		childList.append(obj)

	cartList = []
	token = request.session.get("token")
	if token:
		user =User.objects.get(userToken = token)
		cartList = Cart.objects.filter(userAccount = user.userAccount)
	
	for p in productList:
		for c in cartList:
			if c.productid == p.productid:
				p.num = c.productnum
				continue


	return render(request, 'axf/market.html', {'title':'Market','leftSlider':leftSlider,
		'productList':productList,'childList':childList, 'categorysid':categorysid,
		'cid':cid})


def cart(request):
	cartList = []
	token = request.session.get("token")
	if token != None:
		user = User.objects.get(userToken = token)
		cartList = Cart.objects.filter(userAccount = user.userAccount)
		
	
	return render(request, 'axf/cart.html', {'title':'Cart', 'cartList':cartList})


def mine(request):
	username = request.session.get('username', 'UnSign In')
	return render(request, 'axf/mine.html', {'title':'Mine', 'username': username})

# 登录

def login(request):
	if request.method == "POST":
		f = LoginForm(request.POST)
		if f.is_valid():
			# 信息格式ok,验证密码和账号
			nameid = f.cleaned_data["username"]
			pswd = f.cleaned_data["passwd"]
			try:
				user = User.objects.get(userAccount = nameid)
				if user.userPasswd != passwd:
					return redirect('/login/')
			except User.DoesNotExist as e:
				return redirect('/login/')

			# 登录成功
			token = time.time() + random.randrange(1, 1000)
			user.userToken = str(token)
			user.save()

			request.session['username'] = user.userName
			request.session['token'] = user.userToken
			
			return redirect('/mine/')
		else:
			return render(request, 'axf/login.html', {'title':'Sign in', 'form':f, 'error':f.error})
	else:
		f = LoginForm()
		return render(request, 'axf/login.html', {'title':'Sign in', 'form':f})

	
# 注册
def register(request):
	if request.method == "POST":
		userAccount = request.POST.get('userAccount')
		userPasswd = request.POST.get('userPass')
		userName = request.POST.get('userName')
		userPhone = request.POST.get('userPhone')
		userAddress = request.POST.get('userAddress')
		userRank = 0
		token = time.time() + random.randrange(1, 1000)
		userToken = str(token)
		f = request.FILES['userImg']
		userImg = os.path.join(settings.MDEIA_ROOT, userAccount + '.png')
		with open(userImg, 'wb') as fp:
			for data in f.chunk():
				fp.write(data)
		user = User.createuser(userAccount, userPasswd, userName, userPhone, userAddress, userImg, userRank, userToken)
		user.save() 

		request.session['username'] = userName
		request.session['token'] = userToken
		return redirect('/mine/')
	else:
		return render(request, 'axf/register/html', {'title':'Register'})

#退出登录
def quit(request):
	logout(request)
	return redirect('/mine/')

#
def checkuserid(request):
	userid = request.POST.get("userid")
	try:
		user = User.objects.get(userAccount = userid)
		return JsonResponse({"data":"该用户已被注册","status":"error"})
	except User.DoesNotExist as e:
		return JsonResponse({"data":"可以注册","status":"success"})


# 修改购物车
def changecart(request, flag):
	# 判断用户是否登录
	token = request.session.get("token")
	if token == None:
		# 没登录
		return JsonResponse({"data":-1, "status":"error"})

	productid = request.POST.get('productid')
	product = Goods.objects.get(productid=productid)
	user = User.objects.get(userToken = token)

	if flag == '0':
		if product.storenums == 0:
			return JsonResponse({"data":-2, "status":"error"})

		carts = Cart.objects.filter(userAccount = user.userAccount)
		c = None
		if carts.count() == 0:
			# 直接增加一条订单
			c = Cart.createcart(user.userAccount,productid, 1, 
				product.price, True, product.productimg, 
				product.productlongname, False)
			c.save()
		else:
			try:
				c = carts.get(productid = productid)
				# 修改数量和价格
				c.productnum += 1
				c.productprice = "%.2f" % (float(productprice) * c.productnum)
				c.save()
			except Cart.DoesNotExist as e:
				# 直接增加一条订单
				c = Cart.createcart(user.userAccount,productid, 1, 
			 	product.price, True, product.productimg, 
			 	product.productlongname, False)
				c.save()
		# 库存减一
		product.storenums-= 1
		product.save()		
		return JsonResponse({"data":c.productnum, "price":c.productprice, "status":"success"})
	
	elif flag == '1':
		carts = Cart.objects.filter(userAccount = user.userAccount)
		c = None
		if carts.count() == 0:
			return JsonResponse({"data":-2, "status":"error"})
		else:
			try:
				c = carts.get(productid = productid)
				# 修改数量和价格
				c.productnum -= 1
				c.productprice = "%.2f" % (float(productprice) * c.productnum)
				
				if c.productnum == 0:
					c.delete()
				else:
					c.save()
				
			except Cart.DoesNotExist as e:
				return JsonResponse({"data":-2, "status":"error"})
		# 库存减一
		product.storenums += 1
		product.save()		
		return JsonResponse({"data":c.productnum, "price":c.productprice, "status":"success"})
	
	elif flag == '2':
		carts = Cart.objects.filter(userAccount=user.userAccount)
		c = carts.get(productid=productid)
		c.isChose = not c.isChose
		c.save()
		str = ""
		if c.isChose:
			str = "√"
		return JsonResponse({"data":str, "status":"success"})

	elif flag == '3':
		pass

	return 


def saveorder(request):
	token = request.session.get("token")
	if token == None:
		# 没登录
		return JsonResponse({"data":-1, "status":"error"})
	user = User.objects.get(userToken=token)
	carts = Cart.objects.filter(isChose = True)
	if carts.count() == 0:
		return JsonResponse({"data":-1, "status":"error"})

	oid = time.time() + random.randrange(1, 10000)
	oid = "%d"%oid
	o = Order.createorder(oid, user.userAccount, 0)
	o.save()
	for item in carts:
		item.isDelete = True
		item.orderid = oid
		item.save()
	return JsonResponse({"status":"error"})