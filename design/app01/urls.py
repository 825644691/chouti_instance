from django.urls import path
from app01 import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("index/", views.index, name="index"),
]
