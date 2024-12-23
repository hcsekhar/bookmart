from django.urls import path
from setuptools.extern import names

from .import views

urlpatterns = [
    path('', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
]