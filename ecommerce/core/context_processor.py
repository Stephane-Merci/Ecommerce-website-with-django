from .models import *

 
def default(request):
    categories = Cathegory.objects.all()
    # address = Address.objects.get(user=request.user)
    
    return{
        'categories' : categories, 
        # 'address' : address
    }