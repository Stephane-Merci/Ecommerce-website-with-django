from django.shortcuts import render
from .models import *


def index(request):
    # product = Product.objects.all().order_by('-id')
    product = Product.objects.filter(featured=True)
    
    context = {
        "products" : product,
    }
    return render(request,'core/index.html', context)

def shop(request):
    product = Product.objects.filter()
    
    context = {
        "products" : product,
    }
    return render(request,'core/shop.html',context)

def category(request):
    category = Cathegory.objects.all()
    
    context = {
        "categories" : category,
    }
    return render(request,'core/category.html',context)

def category_products_list_view(request, cid):
    category = Cathegory.objects.get(cid=cid)
    products = Product.objects.filter(product_status="published", cathegory=category)
    
    context = {
        "category" : category,
        "products" : products, 
    }
    return render(request,'core/category_products_list.html',context)

def vendor(request):
    vendors = Vendor.objects.all()
    
    context = {
        'vendor' : vendors
    }
    return render(request,'core/vendor.html',context)