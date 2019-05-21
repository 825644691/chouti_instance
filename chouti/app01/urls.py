from django.urls import path
from app01 import views

urlpatterns = [
    path('register/', views.register, name="register"),
    path('dform_ajax/', views.dform_ajax),
    path('detail/', views.detail),
    path('initial/', views.initial),
]
