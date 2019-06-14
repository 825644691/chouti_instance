from django.shortcuts import render, HttpResponse, redirect
import datetime
from app01 import models
from django.db.models import Avg, Min, Sum, Max, F, Q
# Create your views here.
from django.db.models import Count



def index(req):
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

    s1 = [1, 2, 3, 4, 5]
    s2 = Person("lxl", 18)
    s3 = datetime.datetime.now()
    s4 = []
    s5 = "<a href ='#'>啊阿斯达克</a>"
    return render(req, "index.html", locals())


def login(req):
    if req.method == "POST":
        username = req.POST.get("username")
        pwd = req.POST.get("pwd")
        if username == "lxl" and pwd == "123":
            # return redirect("app01/index.html")
            return HttpResponse("denglu chenggong")
    return render(req, "login.html")


def ordered(req):
    return render(req, "ordered.html")


def shopping(req):
    return render(req, "shopping.html")


def book_test(req):
    # return HttpResponse("ok")
    # 自动建关联表的插入数据方法
    # author1 = models.Author.objects.get(id=3)
    # author2 = models.Author.objects.get(id=4)
    # book = models.Book.objects.filter(id=3)[0]
    # #author = models.ManyToManyField("Author")
    # book.author.add(author1, author2)
    # return HttpResponse("ok")

    # 手动建表
    # models.Book2Author.objects.create(
    #     book_id=2,
    #     author_id=3,
    # )
    #多对多表 在删除数据的时候(级连删除)，在关联表中有的都会删除

    #obj = models.Book.objects.filter(id=3)
    #for,if第一次执行for循环会执行sql操作，并把数据放进缓存
    #if的使用用obj.exists()只返回True or False
    # for o in obj:
    #     #     print(o.title)
    #     # obj.update(title="longzu")
    #     # for o in obj:
    #     #     print(o.title)
    #     # if obj.iterator()#把所有结果做成一个迭代器，用多少拿多少
    #     #
    #     # return HttpResponse("ok")
    # 正向查询(根据数据的外键去主键所对应的表去取)
    # obj = models.Book.objects.filter(title="longzu")[0]
    # print(obj.publisher.city)
    # publisher是外键

    # 反向查询
    # 通过主键去取外键的数据
    # 通过obj.外键表_set
    # obj = models.Publish.objects.filter(name="广州出版社")[0]
    # obj.book_set.values("title")



    #多对多模式查询是否可以通过manytomany.CharField来正反查询属性
    #查找id>2,id<2,id=2:
    # models.Book.objects.filter(id__gt=2)
    # models.Book.objects.filter(id__it=2)
    # models.Book.objects.filter(id__in=2)
    # #模糊查询 例：title__contains="p",不分大小写
    # models.Book.objects.filter(title__contains="l")
    # #范围查询
    # models.Book.objects.filter(id__range=[1, 2])

    #关联表查询
    # obj = models.Publish.objects.filter(book__title__contains="long").values("name")[0]#获取Publish自己表内容
    # obj = models.Publish.objects.filter(book__title__contains="long").values("book__id")[0]#获取Publish的关联表Book的内容
    # print(obj)
    # return HttpResponse("OK")

    # 聚合查询：
    # 平均值(Avg),最小值(Min),总(Sum)
    # models.Book.objects.all().aggregate(Avg("price"))


    # 分组查询
    # 例：根据authors_name分组求其的总价格
    # Book.objects.values("author_name").annotate(Sum("price"))

    # F查询，专门对某一列数据做处理
    # 例：给全部书的价格都加上20元
    # models.Book.objects.all().updata(price=F("price")+20)


    # Q查询,(filter(Q(1)|Q(2)))或
    # obj = models.Book.objects.filter(Q(id=3) | Q(title="longzu"))


    # __startswith=("") endswith("") 以什么开头，以什么结尾

    # 关联表查询(不同表的内容联合查询)
    # objs = models.Book.objects.all().select_related("publisher")
    # for obj in objs:
    #     print(obj.publisher.name)
    obj = models.Book.objects.aggregate(n=Count("id"))
    print(obj)

    return HttpResponse("ok")

    # objs = models.Author.objects.values("name", "book__title")
    # for obj in objs:
    #     print(obj["name"], obj["book__title"])
    # return HttpResponse("ok")
