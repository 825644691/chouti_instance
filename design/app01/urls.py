from django.urls import path,re_path
from app01.views import LR

urlpatterns = [
    path("register/", LR.register, name="register"),
    path("login/", LR.login, name="login"),
    path("index/", LR.index, name="index"),
    path("mf_test/", LR.mf_test),
    re_path("edit/(\d+)/", LR.edit),


]
