from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    # product = Product.objects.all().order_by('-id')
    product = Product.objects.filter(featured=True)
    
    context = {
        "products" : product,
    }
    return render(request,'core/index.html', context)

def productlistView(request):
    product = Product.objects.filter()
    
    context = {
        "products" : product,
    }
    return render(request,'core/shop.html',context)
