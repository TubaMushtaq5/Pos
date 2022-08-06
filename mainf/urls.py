from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('dashboard/', views.Dashboard, name='blog-Dashboard'),
    path('user/', views.User, name='blog-user'),
    path('pos/', views.Pos, name='blog-pos'),
    path('order/', views.Order, name='blog-order'),
    path('settings/', views.Settings, name='blog-settings'),
    path('inventary/', views.Inventary, name='blog-inventary'),
]