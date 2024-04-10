from django.contrib import admin
from django.urls import path,include
from. import views

urlpatterns = [
    path('', views.home,name='home'),
    path('propos', views.propos,name='propos'),
    path('signup', views.signup,name='propos'),
     
]
