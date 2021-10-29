from django.urls import path
from . import views
from .views import ml

urlpatterns = [
    path('', views.home, name='home'),
    path('m1/', views.m1, name='m1'),
    path('library/', views.viewsongs, name='lib'),
    path('ml/', ml.as_view(), name='ml'),
]
