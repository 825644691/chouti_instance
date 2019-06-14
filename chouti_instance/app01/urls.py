from django.urls import path
from app01 import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("index/", views.index, name="index"),
    path("send_msg/", views.send_msg),
    path("check_code/", views.check_code),
    path("favor/", views.dofavor),
    path("comment/", views.do_comment),
    path("comment1/", views.comment1),
    path("logout/", views.logout),
    path("addComment/", views.addComment),
    path("test/", views.test),
    path("info/", views.info),
    path("addConnect/", views.addConnect),
    path("publish/", views.publish),


]
