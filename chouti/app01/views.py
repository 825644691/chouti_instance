from django.shortcuts import render, HttpResponse
from django import forms
import json

import pickle

# Create your views here.


class LoginForm(forms.Form):
    user = forms.CharField(min_length=6,error_messages={"required": "用户名不能为空",
                                                        "min_length": "用户名长度不能小于6"})
    email = forms.EmailField(error_messages={"required": "邮箱不能为空", "invalid": "邮箱格式错误"})


def register(req):
    obj = LoginForm()
    if req.method == "POST":
        obj = LoginForm(req.POST)
        if obj.is_valid():
            value_dict = obj.clean()
            print(value_dict)
            # create(**value_dict)
        else:
            # error_dict = obj.errors
            # print(error_dict['user'][0])
            # print(error_dict['email'][0])
            pass
        return render(req, "register.html", {"obj": obj})
    return render(req, "register.html", {"obj": obj})


def dform_ajax(req):
    if req.method == "GET":
        return render(req, "dform_ajax.html")
    ret = {'status': True, 'error': None, 'data': None}
    obj = LoginForm(req.POST)
    if obj.is_valid():
        print(obj.clean())
    else:
        ret["status"] = False
        ret["error"] = obj.errors.as_json()
    return HttpResponse(json.dumps(ret))


# class JsonCustomEncoder(json.JSONEncoder):
#     def default(self, field):
#         if isinstance(field, object):
#             return {field.__getattribute__('')}
#         else:
#             return json.JSONEncoder.default(self,field)


def detail(req):
    from app01 import dform
    if req.method == "POST":
        obj = dform.DetailForm(req.POST, req.FILES)
        if obj.is_valid():
            print(obj.clean())
        else:
            print(obj.errors.as_json())
    if req.method == "GET":
        obj = dform.DetailForm()
    return render(req, "detail.html", {"obj": obj})


from app01 import models
from app01 import dform


def initial(req):
    nid = req.GET.get("nid")
    m = models.Place.objects.filter(id=nid).first()
    dic = {'username':"root","user_type": m.id}
    obj = dform.InitialForm(dic)
    return render(req, "initial.html", {"obj": obj})


