from django.shortcuts import render, HttpResponse,redirect
import datetime
from blog.models import User
# Create your views here.


def cur_time(request):

    times = datetime.datetime.now()

    return render(request, "cur_time.html", {"abc": times})


def userInfo(req):
    if req.method == "POST":
        # username = req.POST.get("username", None)
        # gender = req.POST.get("gender", None)
        # email = req.POST.get("email", None)
        # print(req.POST["username"])
        #user = {"username": username, "gender": gender, "email": email}
        #user_list.append(user)
        #ORM插入数据
        #方法1
        # User.objects.create(
        #     username=username,
        #     gender=gender,
        #     email=email
        # )
        # 方法2（推荐）
        User.objects.create(
            **dict(req.POST.items())
        )
        #方法3
        # user = User(username=username, gender=gender,email=email)
        # user.save()

        #return render(req, "userInfo.html", {"user_list": user_list})
        #return redirect("/blog/userInfo", {"user_list": user_list})
    # ORM查找(方法1)
    user_list = User.objects.all()
    # ORM查找(方法2)
    # User.objects.get(**kwargs)返回与条件匹配的一个对象
    # ORM查找(方法3)
    # User.objects.filter(**kwargs)返回与条件匹配的所有对象
    # 例User.objects.filter(id=2)[0].values("price")
    return render(req, "userInfo.html", {"user_list": user_list})


def year_archive(req, y):
    return HttpResponse(y+"years")


def index(req,name):
    return HttpResponse(name)


def login(req):
    if req.method == "POST":
        username = req.POST.get("username")
        pwd = req.POST.get("pwd")
        if username == "lxl" and pwd == "123":
            return HttpResponse("登陆成功")
    lxl = "handsome"
    return render(req, 'login.html', locals())
    #locals 调用本地变量lxl，在html直接用{{lxl}}取出handsome


def delete(req):
    username = req.GET.get("username")
    print(username)
    #ORM按索引删除数据
    User.objects.filter(username=username).delete()
    return redirect("/blog/userInfo")


def delete1(req):
    if req.method == "POST":
        #print(dict(req.POST.items()))
        username = req.POST.get("username")
        User.objects.filter(username=username).delete()
        return HttpResponse("成功")
    return HttpResponse("失败")



#redirct()页面转跳

'''
ORM修改数据(方法1)
user = User.objects.get(id=5)获取一个对象
user.name ="lxl"
user.save()#save方法会重新赋值，就算没有改变也会重新赋值，所以效率会很低
ORM修改数据(方法2推荐)
User.objects.filter(id=2).update(name="lxl")#update要的是querySet的对象
'''
