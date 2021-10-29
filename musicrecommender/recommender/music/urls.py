from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('m1/', views.m1, name='m1'),
]
