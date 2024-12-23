from itertools import product
from lib2to3.fixes.fix_input import context

from django.shortcuts import render, redirect
from reportlab.lib.pagesizes import elevenSeventeen

from .forms import ProductFood
from .models import food, Category, Sub_category , Banner

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def ShowAllProducts(request):


    banner = Banner.objects.all()

    sub_category = Sub_category.objects.all()

    category = request.GET.get('category')
    print('category', category)


    # category = request.GET.get('subcategory')
    # print("****8", category)

    if category == None :
        all_products = food.objects.all()
    else:
        all_products = food.objects.filter(category__category_name=category)

    print(all_products,'sjhdjsd')


    categories = Category.objects.all()


    page_num = request.GET.get('page')

    paginator = Paginator(all_products, 4)

    try:
        all_products = paginator.page(page_num)
    except PageNotAnInteger:
        all_products = paginator.page(1)
    except EmptyPage:
        all_products = paginator.page(paginator.num_pages)

    context = {
        'foods1': all_products,
        'categories': categories,
        'banner': banner,
        'sub_category': sub_category
    }
    return render(request, 'showProducts.html', context)
def productDetails(request,pk):

    eachproduct = food.objects.get(id=pk)

    context = {'eachproduct': eachproduct}

    return render(request, 'productDetail.html', context)


def addProduct(request):
    form = ProductFood()
    if request.method == "POST":
        form = ProductFood(request.POST, request.FILES)
        if form.is_valid():
            form.save()

        return redirect('showproducts')

    context = {
        'form' : form
    }

    return render(request,'addProduct.html', context)


def updateProduct(request, pk):
    product = food.objects.get(id=pk)
    form = ProductFood(instance=product)

    if request.method == 'POST':
        form = ProductFood(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect("showproducts")

    context = {
        'form': form
    }

    return render(request,'updateProduct.html', context)

def deleteProduct(request, pk):
    product = food.objects.get(id=pk)
    product.delete()
    return redirect("showproducts")

def searchBar(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            products = food.objects.filter(item_name__icontains=query)
            return render(request, 'searchBar.html', {"products": products})
        else:
            print("no products found")

            return render(request, 'searchBar.html',{})

def products(request, pk):
    subcategory = Sub_category.objects.get(id=pk)
    subcategory_products = food.objects.filter(sub_categories=subcategory)

    context= {
        "sub_category": subcategory_products
    }

    return render(request,'subcategoryProducts.html', context)