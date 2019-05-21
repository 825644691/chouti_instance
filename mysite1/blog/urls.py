
from django.urls import path, re_path, include
from blog import views

urlpatterns = [
    path('cur_time', views.cur_time),
    path('userInfo', views.userInfo),
    re_path(r'^articles/([0-9]{4})/$', views.year_archive),
    path('index', views.index, {"name": "lxl"}),
    path('login', views.login, name="lxl"),
    path('delete', views.delete, name="delete"),
    path('delete1', views.delete1)

]