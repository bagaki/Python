from django.shortcuts import HttpResponse, render, redirect
from myapp import models
# Create your views here.


def classes(request):

    return render(request, 'classes.html')


def add_class(request):
    if request.method == 'GET':
        return render(request, 'add_class.html')
    else:
        print(request.POST)
        v = request.POST.get('title')
        return redirect('/classes/')


def del_class(request):
    nid = request.GET.get('nid')
    return redirect('/classes/')


def edit_class(request):
    if request.method == "GET":
        cid = request.GET.get('cid')
        return render(request, 'edit_class.html')
    else:
        nid = request.GET.get('cid')
        title = request.PSOT.get('title')
        return redirect('/classes/')

###################################################################

def students(request):
    """
    学生列表
    :param request: 
    :return: 
    """
    student_list = 0
    return render(request, 'students.html', {'student_list':student_list})


def add_student(request):
    """

    :param request:
    :return:
    """
    if request.method == 'GET':
        class_list = 0
        return render(request, 'add_student.html', {'class_list':class_list})
    else:
        name = request.POST.get('name')
        class_id = request.POST.get('class_id')
        return redirect('/students/')
    

def edit_student(request):
    if request.method == "GET":
        cid = request.GET.get('cid')
        class_list = 0
        return render(request, 'edit_student.html', {'class_list':class_list})