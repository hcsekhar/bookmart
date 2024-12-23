from django.urls import path
from setuptools.extern import names

from .import views

urlpatterns = [
    path('showproducts/', views.show_products, name='showproductss'),
    path('create-pdf', views.pdf_report, name='create-pdf'),
]

