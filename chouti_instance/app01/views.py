from django.shortcuts import render,HttpResponse
from django import forms
from app01.utils import response,message, check_code as CheckCode
import json
from app01 import models, commons, dform
import datetime
import io

# Create your views here.


def check_code(req):
    stream = io.BytesIO()
    img, code = CheckCode.create_validate_code()
    img.save(stream, "JPEG")
    req.session["CheckCode"] = code
    return HttpResponse(stream.getvalue())


def register(req):
    rep = response.BaseResponse()
    obj = dform.UserForm(req.POST)
    if obj.is_valid():
        value = obj.clean()
        is_valid_code = models.SendMsg.objects.filter(email=value["email"], code=value['email_code']).count()
        if not is_valid_code:
            rep.error["email_code"] = [{"message": "验证码不正确"}]
            return HttpResponse(json.dumps(rep.__dict__))
        has_email = models.UserInfo.objects.filter(email=value["email"])
        if has_email:
            rep.error['email'] = [{"message": "邮箱已经存在"}]
            return HttpResponse(json.dumps(rep.__dict__))
        has_exist_username = models.UserInfo.objects.filter(username=value["username"])
        if has_exist_username:
            rep.error["username"] = [{"message": "用户名已经存在"}]
            return HttpResponse(json.dumps(rep.__dict__))
        models.UserInfo.objects.create(
            username=value["username"],
            email=value["email"],
            password=value["password"],
            ctime=datetime.datetime.now()

        )
        models.SendMsg.objects.filter(email=value["email"]).delete()
        rep.status = True
    else:
        error_msg = obj.errors.as_json()
        rep.error = json.loads(error_msg)
        print(rep.error)
    return HttpResponse(json.dumps(rep.__dict__))


def login(req):
    obj = dform.LoginForm(req.POST)
    rep = response.BaseResponse()
    if obj.is_valid():
        value = obj.clean()
        if value["code"].lower() != req.session["CheckCode"].lower():
            rep.error = {'code': [{'message': '验证码错误'}]}
            return HttpResponse(json.dumps(rep.__dict__))
        from django.db.models import Q

        con = Q()
        q1 = Q()
        q1.connector = 'AND'
        q1.children.append(('email', value["user"]))
        q1.children.append(('password', value['pwd']))

        q2 = Q()
        q2.connector = "AND"
        q2.children.append(("username", value['user']))
        q2.children.append(("password", value["pwd"]))

        con.add(q1, "or")
        con.add(q2, "or")
        obj = models.UserInfo.objects.filter(con).first()
        if not obj:
            rep.error = {'user': [{'message': '用户名邮箱或密码错误'}]}
            return HttpResponse(json.dumps(rep.__dict__))
        rep.status = True
    else:
        error_msg = obj.errors.as_json()
        rep.error = json.loads(error_msg)
        print(rep.error)
    return HttpResponse(json.dumps(rep.__dict__))


def index(req):
    return render(req, "index.html")


class SendMsgForm(forms.Form):
    email = forms.EmailField(error_messages={"invalid": "邮箱格式错误"})


def send_msg(req):
    form = SendMsgForm(req.POST)
    obj = response.BaseResponse()
    if form.is_valid():
        _value_dict = form.clean()
        email = _value_dict['email']
        has_exists_email = models.UserInfo.objects.filter(email=email).count()
        if has_exists_email:
            obj.summary = "此邮箱已经被注册"
            return HttpResponse(json.dumps(obj.__dict__))
        current_date = datetime.datetime.now()
        code = commons.random_code()
        count = models.SendMsg.objects.filter(email=email).count()
        if not count:
            models.SendMsg.objects.create(code=code, email=email, stime=current_date, time=1)
            obj.status = True
        else:
            limit_date = current_date - datetime.timedelta(hours=1)
            times = models.SendMsg.objects.filter(email=email, stime__gt=limit_date, time__gt=5).count()
            if times:
                obj.summary = "已经超过次数限制,一小时后重试"
            else:
                reset = models.SendMsg.objects.filter(email=email, stime__lt=limit_date).count()
                if reset:
                    models.SendMsg.objects.filter(email=email).update(stime=current_date, time=1, code=code)
                from django.db.models import F

                models.SendMsg.objects.filter(email=email).update(code=code,
                                                                  time=F("time")+1)
                obj.status = True
        # message.email(['asd87937149@163.com'], code)
    else:
        obj.summary = form.errors['email'][0]
        obj.status = False
    return HttpResponse(json.dumps(obj.__dict__))