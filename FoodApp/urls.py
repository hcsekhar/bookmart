import views
from django.urls import path
from setuptools.extern import names

from .import views

urlpatterns = [
    path('', views.ShowAllProducts, name='showproducts'),
    path('FoodApp/<int:pk>', views.productDetails, name='productDetail'),
    path('addProduct/', views.addProduct, name='addProduct'),
    path('updateProduct/<int:pk>/', views.updateProduct, name="updateProduct"),
    path('deleteProduct/<int:pk>/', views.deleteProduct, name="deleteProduct"),
    path('search/', views.searchBar, name='search'),
    path('subcategoryProducts/<int:pk>/', views.products, name="subcategoryProducts"),

]
