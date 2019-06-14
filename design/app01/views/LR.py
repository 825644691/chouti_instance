from django.shortcuts import render,redirect
from app01 import dform
from app01 import models
from django import forms

# Create your views here.


def auth(func):
    def inner(req, *args, **kwargs):
        is_login = req.session.get("is_login")
        if is_login:
            return func(req, *args, **kwargs)
        else:
            return redirect("login")
    return inner


def register(req):
    obj = dform.UserForm()
    if req.method == "POST":
        obj = dform.UserForm(req.POST)
        if obj.is_valid():
            print(obj.clean())
            username = req.POST.get("username")
            m = models.User()
            m.full_clean()
            if models.User.objects.filter(username=username).count() == 0:
                models.User.objects.create(**dict(req.POST.items()))
                redirect("login")
            else:
                message = "用户名已经存在"
                return render(req, "register.html", {"message": message, "obj": obj})

        else:
            print(obj.errors.as_json())

    return render(req, "register.html", {"obj": obj})


def login(req):
    obj = dform.UserForm()
    if req.method == "POST":
        obj = dform.UserForm(req.POST)
        if obj.is_valid():
            print(obj.clean())
            username = req.POST.get("username")
            password = req.POST.get("password")
            if models.User.objects.filter(username=username, password=password).exists():
                print("ok")
                req.session["is_login"] = True
                req.session["username"] = username
                return redirect("index")
            else:
                message = "用户名不存在"
                return render(req, "login.html", {"message": message, "obj": obj})

        else:
            print(obj.errors.as_json())

    return render(req, "login.html", {"obj": obj})


@auth
def index(req):
    username = req.session.get("username")
    m = models.User.objects.filter(username=username).first()
    dic = {"username": m.username, "email": m.email}
    obj = dform.UserForm(dic)
    return render(req, "index.html", {"username": username, "obj":obj})


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = models.User #必须先指定一个表
        fields = "__all__" #标是所有字段
    username = forms.CharField(min_length=6)




def mf_test(req):
    obj = UserInfoForm()
    if req.method == "POST":
        obj = UserInfoForm(req.POST)
        if obj.is_valid():
            obj.save()
    return render(req, "test.html", {"obj": obj})


def edit(req, nid):
    print("1")
    if req.method == "GET":

        data = models.User.objects.get(id=nid)
        obj = UserInfoForm(instance=data)
        return render(req, "edit.html", {"obj": obj, "nid": nid})
    if req.method == "POST":
        data = models.User.objects.get(id=nid)
        obj = UserInfoForm(req.POST, instance=data)
        if obj.is_valid():
            obj.save()
    return render(req, "edit.html", {"obj": obj})
