from django.shortcuts import render, redirect, HttpResponse
from app01 import models
import json
from utils.page import PagerHelper
import os

# Create your views here.


def register(req):
    if req.method == "POST":
        models.User.objects.create(
            **dict(req.POST.items())
        )
        return redirect("login")
    return render(req, "register.html")


def validate_regi(req):
    username = req.POST.get("na")
    if models.User.objects.filter(username=username).exists():
        return HttpResponse("1")
    return HttpResponse("0")


def login(req):
    message = ""
    if req.method == "POST":
        username = req.POST.get("username")
        pwd = req.POST.get("password")
        if models.Student.objects.filter(username=username).exists():
            if models.Student.objects.filter(username=username, password=pwd).exists():
                rep = redirect("/app01/index")
                # rep.set_cookie('username', username, max_age=300000)
                rep.set_signed_cookie('username', username, max_age=300000)
                req.session["username"] = username
                req.session["is_login"] = True
                return rep
            else:
                message = "密码错误"
        else:
            message = "用户名不存在"
            # if pwd == password:
            #     return redirect("/app01/index")
    return render(req, "login.html", {"message": message})


def index(req):
    # username = req.COOKIES.get("username")
    is_login = req.session.get("is_login")
    if is_login:
        # username = req.get_signed_cookie("username")
        username = req.session.get("username")
        if username:
            print(req.COOKIES)
            return render(req, "index.html", {"username": username})
    else:
        return redirect("login")


def logout(req):
    req.session.clear()
    return redirect("/app01/index")


# 装饰器
# def auth(func):
#     def inner(req,*args,**kwargs):
#         return func(req,*args,**kwargs)
#     return inner


def auth(func):
    def inner(req, *args, **kwargs):
        is_login = req.session.get("is_login")
        if is_login:
            return func(req, *args, **kwargs)
        else:
            return redirect("login")
    return inner


@auth
def handle_classes(req):
    if req.method == "POST":
        response_dict = {}
        caption = req.POST.get("caption", None)
        if caption and models.Classes.objects.filter(caption=caption).count() == 0:
            response_dict['status'] = True
            obj = models.Classes.objects.create(
                **dict(req.POST.items())
            )
            response_dict["data"] = {"id": obj.id, "caption": obj.caption}
        elif not caption:
            response_dict['status'] = False
            response_dict['error'] = "不能为空"

        else:
            response_dict['status'] = False
            response_dict['error'] = "已经存在"
        return HttpResponse(json.dumps(response_dict))
    current_page = req.GET.get("p", 1)
    current_page = int(current_page)
    total_count = models.Classes.objects.all().count()
    obj = PagerHelper(total_count, current_page, '/app01/classes', 3)
    pager = obj.pager_str()
    cls_list = models.Classes.objects.all()[obj.page_start:obj.page_end]

    username = req.session.get("username")
    return render(req, "classes.html", {"username": username, "classes": cls_list, "str_pager": pager})


@auth
def handle_teacher(req):
    total_account = models.Teacher.objects.count()
    current_page = req.GET.get("p", 1)
    current_page = int(current_page)
    page = PagerHelper(total_account, current_page, "/app01/teacher", 3)
    pager = page.pager_str()
    objs = models.Teacher.objects.filter(id__in=models.Teacher.objects.all()[page.page_start:page.page_end]).values(
        "id", "name", "classes__id", "classes__caption")
    result = {}
    for t in objs:

        if t["id"] in result:
            result[t["id"]]['cls_list'].append({'id': t["classes__id"], 'caption': t["classes__caption"]})
        else:
            if t['classes__id']:
                temp = [{'id': t["classes__id"], 'caption': t["classes__caption"]}]
            else:
                temp = []
            result[t["id"]] = {
                'nid': t['id'],
                'name': t['name'],
                'cls_list': temp
            }
    # for obj in objs:
    #     print(obj.name, obj.classes_set.values("caption"))
    username = req.session.get("username")
    return render(req, "teacher.html", {"username": username, "teacher_list": result,"pager":pager})


@auth
def handle_student(req):
    username = req.session.get("username")
    return render(req, "student.html", {"username": username})


def delete(req):
    if req.method == "POST":
        vid = req.POST.get("id", None)
        print("vid", vid)
        models.Classes.objects.filter(id=vid).delete()
        return HttpResponse("okok")
    return HttpResponse("ok")


def add_teacher(req):
    if req.method == "POST":
        name = req.POST.get("name")
        cls = req.POST.getlist("cls")
        print(cls)
        obj = models.Teacher.objects.create(name=name)
        obj.classes_set.add(*cls)
        return redirect("/app01/teacher")
    username = req.session.get("username")
    cls_list = models.Classes.objects.all()
    return render(req, "add_teacher.html", {"username": username, "cls_list": cls_list})


def tag_delete(req):
    if req.method == "POST":
        id = req.POST.get("id")
        name = req.POST.get("tag", None)
        obj1 = models.Classes.objects.filter(caption=name).values("id")[0]
        obj = models.Teacher.objects.get(id=id)
        obj.classes_set.filter(**obj1).delete()
        return HttpResponse("okok")
    return HttpResponse("ok")


def edit_teacher(req, nid):
    page = req.GET.get("p",1)
    print(page)
    if req.method == "POST":
        name = req.POST.get("name")
        cls_li = req.POST.getlist("class")
        obj = models.Teacher.objects.get(id=nid)
        obj.name = name
        obj.save()
        obj.classes_set.set(cls_li)
        return redirect('/app01/teacher/?p=%s' % page)
    obj = models.Teacher.objects.get(id=nid)
    tea_list = obj.classes_set.all().values_list("id")
    if tea_list:
        id_list = list(zip(*tea_list))[0]
    else:
        id_list = ()
    cls_list = models.Classes.objects.exclude(id__in=id_list)
    clss_list = models.Classes.objects.filter(id__in=id_list)
    username = req.session.get("username")
    return render(req, "edit_teacher.html", {"username": username,
                                             "obj": obj,
                                             "cls_list": cls_list,
                                             "id_list": clss_list})


def upload(req):
    if req.method == "POST":
        user = req.POST.get("user")
        fafafa = req.POST.get("fafafa")
        obj = req.FILES.get("fafafa")
        print(obj.name, obj.size)
        file_path = os.path.join('statics', 'upload', obj.name)
        f = open(file_path, 'wb')
        for chunk in obj.chunks():
            f.write(chunk)
        f.close()
        models.File.objects.create(name=obj.name,path=file_path)
    photo_list = models.File.objects.all()
    return render(req, "upload.html",{'photo_list': photo_list})


def upload1(req):

    user = req.POST.get("user")
    obj = req.FILES.get("fafafa")
    file_path = os.path.join("statics","upload",obj.name)
    f = open(file_path, "wb")
    for chunk in obj.chunks():
        f.write(chunk)
    f.close()
    models.File.objects.create(name=obj.name, path=file_path)
    return HttpResponse(json.dumps(file_path))