from .models import *

 
def default(request):
    categories = Cathegory.objects.all()
    
    return{
        'categories' : categories 
    }