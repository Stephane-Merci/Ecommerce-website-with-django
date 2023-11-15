from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from userauths.models import User


def register_view(request):
    
    if request.method == 'POST':                                                                        #Check if you submit the form                                       
        form = UserRegisterForm(request.POST or None)                                                   #then reprint the form and pre-fill it 
        if form.is_valid():                                                                             #Check if the form data is valid 
            new_user = form.save()                                                                      #If yes then save the form data to the database
            username = form.cleaned_data.get('username')                                                #get the user's username
            messages.success(request, f"Hey {username}, Your account has been crated successfully")     #print acount created
            new_user = authenticate(username=form.cleaned_data.get('email'),                            #authenticate the user with his email ans password 
                                    password=form.cleaned_data.get('password1')
                                    )
            login(request, new_user)                                                                    #if new_user is true then loghim into the system and redirect him to the home page
            return redirect('index')
    else:
        form = UserRegisterForm()                                                                       #If it is not a POST, print an empty form
        
    context = {
        'form':form
    }
    return render(request, 'userauths/signup.html', context)
    
    
    
def login_view(request):
    if request.user.is_authenticated:
        messages.warning(request, "You are already logged in")
        return redirect('index')
    
    if request.method == 'POST':
        email = request.POST.get('email')      
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(email=email)
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"You are successfully logged in '{email}'")
                return redirect('index')
            else:
                messages.warning(request, f"User does not exist. Create an accout")
                
        except:
            messages.warning(request, f"User with email '{email}' does not exist")
    
    return render(request, 'userauths/login.html')


def logout_view(request):
    logout(request),
    messages.success(request, f"You are currently logged out")
    return redirect('index')


