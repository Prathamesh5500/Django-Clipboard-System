# urls.py
from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.SignupPage, name='signup'),
    path('login/', views.LoginPage, name='login'),
    path('home/', views.HomePage, name='home'),
    path('logout/', views.LogoutPage, name='logout'),
    path('display_public_data/', views.display_public_data, name='display_public_data'),
]
