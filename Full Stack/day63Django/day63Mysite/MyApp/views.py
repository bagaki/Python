# coding=utf-8
from django.shortcuts import render, HttpResponse, redirect
from MyApp import models

# Create your views here.
# 出版社
def publisher_list(request):
    # 去数据库查出所有的出版社，填充到HTML中，给用户返回
    ret = models.Publisher.objects.all().order_by("id")
    return render(request, "publisher_list.html", {"publisher_list": ret})


def add_publisher(request):
    error_msg = ""
    if request.method == "POST":
        new_name = request.POST.get("publisher_name")
        if new_name:
            # 通过ORM去数据库里新建一条数据
            models.Publisher.objects.create(name=new_name)
            # 引导用户访问出版社列表页，查看是否添加成功
            return redirect("/publisher_list/")
        else:
            error_msg = "The Publisher name cannot null"
    # 用户第一次来，返回一个填写HTML页面
    return render(request, "add_publisher.html", {"error": error_msg})


def del_publisher(request):
    # 取到指定删除的数据
    # 1.从GET请求的参数里面拿到将要删除的数据的ID值
    del_id = request.GET.get("id", None)
    # 如果能取到id值
    if del_id:
        # 去数据库删除当前id值得数据
        # 根据id值查找到数据
        del_obj = models.Publisher.objects.get(id=del_id)
        # 删除
        del_obj.delete()
        # 返回删除后的页面，跳转到出版社的列表页，查看删除是否成功
        return redirect("/publisher_list/")
    else:
        return HttpResponse("The data is not exsist")


def edit_publisher(request):
    # 用户修改完出版社的名字，点击提交安安，给我发来新的出版社名字
    if request.method == "POST":
        # 取新出版社名字
        edit_id = request.POST.get("id")
        new_name = request.POST.get("publisher_name")
        # 更新出版社
        # 根据id去打编辑的是哪个出版社
        edit_publisher = models.Publisher.objects.get(id=edit_id)
        edit_publisher.name = new_name
        edit_publisher.save()
        # 跳转出版社列表页
        return redirect("/publisher_list/")

    # 从GET请求的URL中取到id参数
    edit_id = request.GET.get("id")
    if edit_id:
        # 获取到当前编辑的出版社对象
        publisher_obj = models.Publisher.objects.get(id=edit_id)
        return render(request, "edit_publisher.html", {"publisher": publisher_obj})
    else:
        return HttpResponse("The Publisher is not exsist")

# 书
def book_list(request):
    all_book = models.Book.objects.all()
    return render(request, "book_list.html", {"all_book": all_book})


def add_book(request):
    if request.method == "POST":
        new_title = request.POST.get("book_title")
        new_publisher_id = request.POST.get("publisher")
        models.Book.objects.create(title=new_title, publish_id=new_publisher_id)
        return redirect("/book_list/")

    ret = models.Publisher.objects.all()
    return render(request, "add_book.html", {"publisher_list": ret})


def delete_book(request):
    delete_id = request.GET.get("id")
    models.Book.objects.get(id=delete_id).delete()
    return redirect("/book_list/")


def edit_book(request):
    if request.method == "POST":
        edit_id = request.POST.get("id")
        new_title = request.POST.get("book_title")
        new_publisher_id = request.POST.get("publisher")
        edit_book_obj = models.Book.objects.get(id=edit_id)
        edit_book_obj.title = new_title
        edit_book_obj.publish_id = new_publisher_id
        edit_book_obj.save()
        return redirect("/book_list/")

    edit_id = request.GET.get("id")
    edit_book_obj = models.Book.objects.get(id=edit_id)
    ret = models.Publisher.objects.all()
    return render(request,
                  "edit_book.html",
                  {"publisher_list": ret, "book_obj": edit_book_obj}
    )


def author_list(request):
    all_author = models.Author.objects.all()
    return render(request, "author_list.html", {"author_list": all_author})


def add_author(request):
    if request.method == "POST":
        new_author_name = request.POST.get("author_name")
        books = request.POST.getlist("books")
        new_author_obj = models.Author.objects.create(name=new_author_name)
        new_author_obj.book.set(books)

        return redirect("/author_list/")

    ret = models.Book.objects.all()
    return render(request, "add_author.html", {"book_list": ret})


def delete_author(request):
    del_author_id = request.GET.get("id")
    models.Author.objects.get(id=del_author_id).delete()
    return redirect("/author_list/")


def edit_author(request):
    if request.method == "POST":
        edit_author_id = request.POST.get("author_id")
        new_author_name = request.POST.get("author_name")
        new_books = request.POST.getlist("books")
        edit_author_obj = models.Author.objects.get(id=edit_author_id)
        edit_author_obj.name = new_author_name
        edit_author_obj.book.set(new_books)
        edit_author_obj.save()
        return  redirect("/author_list/")

    edit_id = request.GET.get("id")
    edit_author_obj = models.Author.objects.get(id=edit_id)
    ret = models.Book.objects.all()
    return render(request, "edit_author.html", {"book_list":ret, "author": edit_author_obj})