from django.urls import path
from app01 import views

urlpatterns = [
    path("index/", views.index),
    path('ajax_receive/', views.ajax_receive),
    path('register/', views.register),
    path('JQ_test/', views.JQ_test),
    path('JQ_receive/', views.JQ_receive),
    path('test/', views.test),
    path('test1/', views.test1),
]
