from django.shortcuts import render,HttpResponse,redirect
from django import forms
from app01.utils import response,message, check_code as CheckCode, page
import json
from app01 import models, commons, dform
import datetime
import io
from django.db.models import F, Q
import re
import time
import math
import os
import base64


from django.core.cache import cache
from django_redis import get_redis_connection

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
            ctime=datetime.datetime.now(),
            img="statics/upload/image48.png",

        )
        models.SendMsg.objects.filter(email=value["email"]).delete()
        rep.status = True
        req.session["is_login"] = True
        req.session["username"] = value["username"]
        s = models.UserInfo.objects.get(username=value["username"])
        req.session["user_id"] = s.id
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
        req.session["is_login"] = True
        req.session["username"] = value["user"]
        s = models.UserInfo.objects.get(username=value["user"])
        req.session["user_id"] = s.id
        req.session["secondname"] = s.secondname
        # req.session["user_id"] = value["id"]
    else:
        error_msg = obj.errors.as_json()
        rep.error = json.loads(error_msg)
        print(rep.error)
    return HttpResponse(json.dumps(rep.__dict__))


def index(req):
    region = req.GET.get("key", None)
    number = models.Chouti.objects.count()
    # item = json.loads(eval(data))
    current_page = req.GET.get("p", 1)
    current_page = int(current_page)
    favor_most = models.Chouti.objects.all().order_by("-praise_count")[0:7]
    obj = page.PagerHelper(number, current_page, '/app01/index', 10)
    pager = obj.pager_str()
    news_list = models.Chouti.objects.filter(region=region)[obj.page_start:obj.page_end]
    username = req.session.get("username", None)
    keyword = req.POST.get("keyword", None)
    if keyword:
        con = Q()
        q1 = Q()
        q1.connector = "AND"
        q1.children.append(("title__contains", keyword))

        q2 = Q()
        q2.connector = "AND"
        q2.children.append(("content__contains", keyword))
        con.add(q1, "or")
        con.add(q2, "or")
        news_list = models.Chouti.objects.filter(con)[obj.page_start:obj.page_end]
    if username:
        objj = models.UserInfo.objects.get(username=username)
        favor = models.Favor.objects.filter(User_id=objj.id)
        number = []
        for f in favor:
            number.append(f.Chouti_id)
    else:
        objj = ""
    return render(req, "index.html", {"news_list": news_list, "pager_str": pager, "request": req, "number": number,
                                      "favor_most": favor_most, "objjj": objj, "region": region})


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
                message.email(['asd87937149@163.com'], code)
    else:
        obj.summary = form.errors['email'][0]
        obj.status = False
    return HttpResponse(json.dumps(obj.__dict__))


def dofavor(req):
    username = req.session.get("username")
    nid = req.POST.get("news_id")
    obj = models.UserInfo.objects.get(username=username)
    if not models.Favor.objects.filter(Chouti_id=nid, User_id=obj.id).exists():
        models.Favor.objects.create(
            Chouti_id=nid,
            User_id=obj.id,
            is_favor=True,
        )
        data = {"status": True, "code": 2301}

        print(req.session.get("favor_id"))
        models.Chouti.objects.filter(id=nid).update(praise_count=F("praise_count") + 1)

    else:
        models.Favor.objects.filter(Chouti_id=nid, User_id=obj.id).delete()
        data = {"status": True, "code": 2302}
        models.Chouti.objects.filter(id=nid).update(praise_count=F("praise_count") - 1)

    return HttpResponse(json.dumps(data))


def do_comment(req):
    nid = req.POST.get("id")
    print(nid)
    com = models.Comment.objects.filter(news_id=nid)
    comment_list = []
    for o in com:
        comment_list.append({"id": o.id,
                             "user_id": o.user_id,
                             "parent_id": o.parent_comment_id,
                             "content": o.content,
                             })
        """
        {"id": o.id,
         "user_id": o.user_id,
         "parent_id": o.parent_comment_id,
         "content": o.content,
        }
        """
    comment_list_dict = {}
    ret = []
    for row in comment_list:
        row.update({"children": []})
        comment_list_dict[row["id"]] = row
        """
        {1:{"id": o.id,
                             "user_id": o.user_id,
                             "parent_id": o.parent_comment_id,
                             "content": o.content,
                             "children":[]}}
        """

    for item in comment_list:
        parent_row = comment_list_dict.get(item["parent_id"])
        if not parent_row:
            ret.append(item)
        else:
            parent_row["children"].append(item)
    print(ret)
    return HttpResponse(json.dumps(ret))


    # data = list()
    # for da in com:
    #     data.append("<li>" + da.content + "</li>")
    # data = "".join(data)
    # return HttpResponse(data)



class Node:
    @staticmethod
    def recu(ret, row):
        for rt in ret:
            if rt["id"] == row["parent_id"]:
                row["children"] = []
                rt["children"].append(row)
                return
            else:
                Node.recu(rt["children"], row)



    @staticmethod
    def create_tree(comment_list):
        ret = []
        for row in comment_list:
            if not row["parent_id"]:
                row["children"] = []
                ret.append(row)
            else:
                Node.recu(ret, row)

        return ret




def comment1(req):
    nid = req.POST.get("id")
    obj = models.Comment.objects.filter(news_id=nid).select_related("user")
    #计算时间过去了多久
    comment_list = []
    for o in obj:

        comment_list.append({"id": o.id,
                             "user_id": o.user_id,
                             "parent_id": o.parent_comment_id,
                             "content": o.content,
                             "username": o.user.username,
                             "news_id": o.news_id,
                             "time": date_count(o.ctime)})
    """
           {"id": o.id,
            "user_id": o.user_id,
            "parent_id": o.parent_comment_id,
            "content": o.content,
           }
    """
    '''
    [{"id": o.id,
            "user_id": o.user_id,
            "parent_id": o.parent_comment_id,
            "content": o.content,
    },
    {"id": o.id,
            "user_id": o.user_id,
            "parent_id": o.parent_comment_id,
            "content": o.content,
    }]
    '''
    comment_tree = Node.create_tree(comment_list)
    print(comment_tree)
    return HttpResponse(json.dumps(comment_tree))


def date_count(ptime):

    try:
        t = time.strptime(str(ptime).split(".")[0], "%Y-%m-%d %H:%M:%S")
        timeStamp2 = int(time.mktime(t))
    except Exception:
        timeArray = time.localtime(ptime)
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        t2 = time.strptime(otherStyleTime, "%Y-%m-%d %H:%M:%S")
        timeStamp2 = int(time.mktime(t2))
    n = time.strptime(str(datetime.datetime.now()).split(".")[0], "%Y-%m-%d %H:%M:%S")
    timeStamp1 = int(time.mktime(n))
    t = timeStamp1 - timeStamp2-28800
    day = math.floor(t/86400)
    remain = t % 86400
    hour = math.floor(remain/3600)
    remain = remain % 3600
    mins = math.floor(remain/60)
    if day != 0:
        return "%s天%s小时前" % (day, hour)
    else:
        if mins <= 2:
            return "刚刚"
        elif hour == 0:
            return "%s分钟前" % mins
        else:
            return "%s小时%s分钟前" % (hour, mins)




def logout(req):
    req.session.clear()
    return redirect("/app01/index")


def addComment(req):
    parent_id = req.POST.get("p_id", None)
    id = req.POST.get("id")
    data = req.POST.get("data")
    models.Comment.objects.create(
        content=data,
        news_id=id,
        parent_comment_id=parent_id,
        user_id=req.session.get("user_id")
    )
    obj = models.Comment.objects.filter(news_id=id).select_related("user")
    comment_list = []
    for o in obj:

        comment_list.append({"id": o.id,
                             "user_id": o.user_id,
                             "parent_id": o.parent_comment_id,
                             "content": o.content,
                             "username": o.user.username,
                             "news_id": o.news_id,
                             "time": date_count(o.ctime)})

    comment_tree = Node.create_tree(comment_list)
    return HttpResponse(json.dumps(comment_tree))


def test(req):
    obj = models.Chouti.objects.values("praise_count").distinct().order_by(F("praise_count"))
    for o in obj:
        print(o["praise_count"])



    return render(req, "test.html")



def info(req):
    if req.method == "POST":
        username = req.session.get("username")
        secondname = req.POST.get("secondname")
        gender = req.POST.get("gender")
        signature = req.POST.get("signature")
        file_path = os.path.join("statics", "upload", secondname+".jpg")
        '''
        $img = str_replace('data:image/png;base64,', '', $img);
        $img = str_replace(' ', '+', $img);
        '''
        data = req.POST.get("img")
        data = data.replace('data:image/png;base64,', '')
        data = data.replace(' ', '+')
        data = base64.b64decode(data)
        f = open(file_path, "wb")

        f.write(data)
        f.close()
        models.UserInfo.objects.filter(username=username).update(secondname=secondname,
                                                                 gender=gender,
                                                                 signature=signature,
                                                                 img=file_path)
        return HttpResponse("成功")
    if req.method == "GET":
        id = req.session.get("user_id")
        obj = models.UserInfo.objects.get(id=id)

        return render(req, "edit_info.html", {"objjj": obj})


def base(req):
    id = req.session.get("user_id",None)
    if id:
        obj = models.UserInfo.objects.get(id=id)
    return render(req, "base.html", {"objjj": obj})


def addConnect(req):
    data = req.POST.get("text", None)
    if data:
        data = data.split("/")
        return HttpResponse(json.dumps(data[2]))
    else:
        return HttpResponse("false")


def publish(req):
    title = req.POST.get("title")
    content = req.POST.get("content", None)
    publish_type = req.POST.get("type")
    if publish_type == "链接":
        region = req.POST.get("1")
        print(region)
    if publish_type == "文字":
        region = req.POST.get("2")
        print(region)
    is_true = models.Chouti.objects.create(
        title=title,
        content=content,
        region=region,
        username=req.session.get("username"),
        status=False,
    )

    if is_true:
        return HttpResponse("true")
    else:
        return HttpResponse("false")
