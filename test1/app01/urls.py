from django.urls import path,re_path
from app01 import views


urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('validate_regi/', views.validate_regi),
    path('index/', views.index),
    path('logout/', views.logout, name="logout"),
    path('classes/', views.handle_classes),
    path('student/', views.handle_student),
    path('teacher/', views.handle_teacher),
    path('delete/', views.delete),
    path('add_teacher/', views.add_teacher),
    path('tag_delete/', views.tag_delete),
    re_path(r'^edit_teacher-(\d+)/$', views.edit_teacher),
    re_path(r'^edit_teacher-(\d+)/?p=(\d+)$', views.edit_teacher),
    path('upload/',views.upload),
    path('test/', views.test)


]
