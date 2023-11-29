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
        'vendors' : vendors
    }
    return render(request,'core/vendor.html',context)

def vendor_details(request, vid):
    vendor = Vendor.objects.get(vid=vid)
    products = Product.objects.filter(vendor=vendor, product_status="published")
    
    context = {
        'vendor' : vendor,
        'products' : products
    }
    return render(request,'core/vendor_detail.html',context)

def product_details(request, pid):
    product = Product.objects.get(pid=pid, product_status="published")
    p_images = product.product_images.all()
    
    context = {
        'product': product,
        'p_images': p_images
    }
    
    return render(request, 'core/product_details.html',context)