from django.shortcuts import render,HttpResponse
import json
# Create your views here.


def index(req):
    return render(req, "index.html")


def ajax_receive(req):
    if req.method == "POST":
        print("req.POST", req.POST)
    return HttpResponse("ok")


def register(req):
    # return render(req, 'register.html')
    if req.method == "POST":
        username = req.POST.get("username")
        print(username)
        if username == "lxl":
            return HttpResponse("1")
        return HttpResponse("0")
    return render(req, 'register.html')


def JQ_test(req):
    return render(req, "ajax_jquery.html")


def JQ_receive(req):
    #obj = {"name": "lxl"}
    print("hello world")
    func = req.GET.get("callback")
    return HttpResponse("%s('kkk')" % func)

# python => json
# dict =>  object
# list,tuple  => array
# int =>number
# True => true
# False => false
# None  => null