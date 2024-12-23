from django.urls import path
from setuptools.extern import names

from . import views

urlpatterns = [
    path('apiOverview', views.apiOverview, name="apiOverview"),
    path("product-list/", views.ShowAll, name= "product-list"),
    path("product-view/<int:pk>/", views.ViewProduct, name="product-view"),
    path("product-create/", views.CreateProduct, name="create-product"),
    path("product-update/<int:pk>/", views.UpdateProduct, name="update-product"),
    path("product-delete/<int:pk>/", views.DeleteProduct, name="delete-product"),
]