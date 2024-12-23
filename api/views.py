from django.shortcuts import render
from products import products
from rest_framework.response import Response
from rest_framework.decorators import api_view
from FoodApp.models import food
from .serializer import ProductSerializer

# Create your views here.
@api_view(['GET'])
def apiOverview(request):

    api_urls = {
        "List": '/product-list',
        "Details View": '/product-detail/<int:id>',
        "Create": '/product-create',
        "Delete": '/product-delete/<int:id>',
        "Update": '/product-update/<int:id>',
    }
    return Response(api_urls)

@api_view(['GET'])
def ShowAll(request):
    products = food.objects.all()
    serializer = ProductSerializer(products, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def ViewProduct(request,pk):
    product = food.objects.get(id=pk)
    serializer = ProductSerializer(product, many=False)

    return Response(serializer.data)

@api_view(['POST'])
def CreateProduct(request):
    print(request.data)
    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def UpdateProduct(request,pk):
    products = food.objects.get(id=pk)
    serializer = ProductSerializer(instance=products, data=request)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['GET'])
def DeleteProduct(request,pk):
    products = food.objects.get(id=pk)

    products.delete()

    return Response("Item Deleted")
