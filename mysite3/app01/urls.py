from django.contrib import admin
from django.urls import path, include
from app01 import views

urlpatterns = [
    path('index/', views.index),
    path('login/', views.login, name="login"),
    path('ordered/', views.ordered, name="order"),
    path('shopping/', views.shopping, name="shopping"),
    path('test/', views.book_test)
]