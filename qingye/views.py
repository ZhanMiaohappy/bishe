from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse

def index(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'app/home.html')


def yingYi(request):
    engmoduinfo=engmoduInfo.objects.filter(engtypeid_id=1)
    itemList=[]
    for item in engmoduinfo:
        itemDict={}
        itemDict["engmoduname"]=item.engmoduname
        itemDict["teacher"]=item.teacher
        itemDict["coursetime"]=item.coursetime
        itemDict["limitnum"]=item.limitnum
        itemDict["costfee"]=item.costfee
        itemDict["engtypename"]=item.engtypeid.engtypename
        itemList.append(itemDict)
        context={"code":200,"message":"","itemList":itemList}

    return render(request, 'app/yingYi.html', context)


def yingEr(request):
    engmoduinfo = engmoduInfo.objects.filter(engtypeid_id=2)
    itemList = []
    for item in engmoduinfo:
        itemDict = {}
        itemDict["engmoduname"] = item.engmoduname
        itemDict["teacher"] = item.teacher
        itemDict["coursetime"] = item.coursetime
        itemDict["limitnum"] = item.limitnum
        itemDict["costfee"] = item.costfee
        itemDict["engtypename"] = item.engtypeid.engtypename
        itemList.append(itemDict)
        context = {"code": 200, "message": "", "itemList": itemList}
    return render(request, 'app/yingEr.html',context)


def course(request):
    currentUserId=request.session.get('userid')
    everbuyinfo=everbuyInfo.objects.filter(userid_id=currentUserId)
    itemList=[]
    for item in everbuyinfo:
        itemDict={}
        itemDict['buytime']=item.buytime
        itemDict['username']=item.userid.username
        itemDict['engmoduname']=item.engmoduid.engmoduname
        itemDict['engtypename']=item.engmoduid.engtypeid.engtypename
        itemDict["engmoduid"]=item.engmoduid_id
        itemList.append(itemDict)
    context={"code":200, "itemList":itemList}
    return render(request, 'app/course.html', context)

def information(request):
    return render(request, 'app/information.html')


def comprehension1(request, moduleid):
    engrecord=engmoduInfo.objects.get(engmoduid=moduleid)
    context={"code":200,
             "engmoduname":engrecord.engmoduname,
             "teacher":engrecord.teacher,
             "coursetime":engrecord.coursetime,
             "limitnum":engrecord.limitnum,
             "costfee":engrecord.costfee,
             "engtypename":engrecord.engtypeid.engtypename,
             "engmoduid":engrecord.engmoduid
             }
    return render(request, 'app/comprehension1.html' ,context)


# def comprehension2(request):
#     return render(request, 'app/comprehension2.html')
#
#
# def clozeText1(request):
#     return render(request, 'app/clozeText1.html')
#
#
# def clozeText2(request):
#     return render(request, 'app/clozeText2.html')
#
#
# def writing1(request):
#     return render(request, 'app/writing1.html')
#
#
# def writing2(request):
#     return render(request, 'app/writing2.html')
#
#
# def translation1(request):
#     return render(request, 'app/translation1.html')
#
#
# def translation2(request):
#     return render(request, 'app/translation2.html')


def courseList11(request, engmoduid):
    videoinfo=videoInfo.objects.filter(engmoduid_id=engmoduid)
    itemList = []
    for item in videoinfo:
        itemDict={}
        itemDict['videoname'] = item.videoname
        itemDict['videopath'] = item.videopath
        itemDict['duration'] = item.duration
        itemDict['engmoduname'] = item.engmoduid.engmoduname
        itemDict['engtypename'] = item.engmoduid.engtypeid.engtypename
        itemDict['teacher'] = item.engmoduid.teacher
        itemDict['videopath'] = item.videopath
        itemList.append(itemDict)
    context = {"code": 200, "itemList": itemList}
    return render(request, 'app/courseList11.html', context)


# def courseList12(request):
#     return render(request, 'app/courseList12.html')
#
#
# def courseList13(request):
#     return render(request, 'app/courseList13.html')
#
#
# def courseList14(request):
#     return render(request, 'app/courseList14.html')
#
#
# def courseList21(request):
#     return render(request, 'app/courseList21.html')
#
#
# def courseList22(request):
#     return render(request, 'app/courseList22.html')
#
#
# def courseList23(request):
#     return render(request, 'app/courseList23.html')
#
#
# def courseList24(request):
#     return render(request, 'app/courseList24.html')


def register(request):
    request.session.flush()
    return render(request, 'register/register.html',)


def alert(request):
    return render(request, 'register/alert.html')

#登录处理
def login_handle(request):
    dictPost=request.POST
    phoneNum=dictPost.get('phonenum')
    password=dictPost.get('password')
    userinfo=userInfo.objects.filter(phonenum=phoneNum)
    if userinfo:
        if userinfo[0].password == password:
            request.session['userid'] = userinfo[0].userid
            request.session['username'] = userinfo[0].username
            request.session['phonenum'] = userinfo[0].phonenum
            return redirect('/qingye/index/')
        else:
            return redirect('/qingye/register/')
    else:
        return redirect('/qingye/register/')

#注册处理
@csrf_exempt
def register_handle(request):
    try:
        dictPost = request.POST
        username = dictPost['username']
        emailaddr = dictPost['emailaddr']
        phonenum = dictPost['phonenum']
        password = dictPost['password']
        userInfoSave = userInfo(username=username, emailaddr=emailaddr, phonenum=phonenum, password=password,
                                roleid_id=2)
        userInfoSave.save()
        # return render(request,'register/register.html',{"code": 200})
        return JsonResponse({"code":200})
    except Exception as e:
        # return render(request,'register/register.html',{"code":0})
        return JsonResponse({"code": 0})


#购买处理
def buy_handle(request):
    dictPost=request.POST
    password=dictPost.get('password')
    engmoduid=dictPost.get('engmoduid')
    currentUserId=request.session.get('userid')
    userinfo=userInfo.objects.get(userid=currentUserId)
    if password==userinfo.password:
        everbuyinfo=everbuyInfo(engmoduid_id=engmoduid, userid_id=currentUserId)
        everbuyinfo.save()
        return JsonResponse({"code":200})
    else:
        return JsonResponse({"code":0})

#修改处理
@csrf_exempt
def modify_handle(request):
    dictPost = request.POST
    resetPassword=dictPost.get('resetPassword')
    resetName = dictPost.get('resetName')
    userid=request.session.get('userid')
    userInfo.objects.filter(userid=userid).update(username=resetName, password=resetPassword)
    return JsonResponse({"code":200})




