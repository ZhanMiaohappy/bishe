from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from .models import *
from django.urls import reverse

def index(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'app/home.html')


def yingYi(request):
    return render(request, 'app/yingYi.html')


def yingEr(request):
    return render(request, 'app/yingEr.html')


def course(request):
    return render(request, 'app/course.html')

def information(request):
    return render(request, 'app/information.html')


def comprehension1(request):
    return render(request, 'app/comprehension1.html')


def comprehension2(request):
    return render(request, 'app/comprehension2.html')


def clozeText1(request):
    return render(request, 'app/clozeText1.html')


def clozeText2(request):
    return render(request, 'app/clozeText2.html')


def writing1(request):
    return render(request, 'app/writing1.html')


def writing2(request):
    return render(request, 'app/writing2.html')


def translation1(request):
    return render(request, 'app/translation1.html')


def translation2(request):
    return render(request, 'app/translation2.html')


def courseList11(request):
    return render(request, 'app/courseList11.html')


def courseList12(request):
    return render(request, 'app/courseList12.html')


def courseList13(request):
    return render(request, 'app/courseList13.html')


def courseList14(request):
    return render(request, 'app/courseList14.html')


def courseList21(request):
    return render(request, 'app/courseList21.html')


def courseList22(request):
    return render(request, 'app/courseList22.html')


def courseList23(request):
    return render(request, 'app/courseList23.html')


def courseList24(request):
    return render(request, 'app/courseList24.html')


def register(request):
    request.session.flush()
    return render(request, 'register/register.html')


def alert(request):
    return render(request, 'register/alert.html')

#登录处理
def login_handle(request):
    dictPost=request.POST
    phoneNum=dictPost.get('phonenum')
    password=dictPost.get('password')
    userinfo=userInfo.objects.filter(phonenum=phoneNum)
    if userinfo:
        if userinfo[0].password==password:
            request.session['userid']=userinfo[0].userid
            request.session['username']=userinfo[0].username
            return redirect('/qingye/index/')
        else:
            return redirect('/qingye/register/')
    else:
        return redirect('/qingye/register/')

#注册处理
def register_handle(request):
    try:
        dicPost = request.POST
        username = dicPost['username']
        emailaddr = dicPost['emailaddr']
        phonenum = dicPost['phonenum']
        password = dicPost['password']
        userInfoSave = userInfo(username=username, emailaddr=emailaddr, phonenum=phonenum, password=password,
                                roleid_id=2)
        userInfoSave.save()
        return render(request,'register/register.html',{"code": 200})
    except Exception as e:
        return render(request,'register/register.html',{"code":0})
