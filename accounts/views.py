from django.shortcuts import render, redirect
# Create your views here.
from django.contrib.auth.models import User, auth

def register(request):

    if request.method =='POST':
        username=request.POST['username'] 
        email=request.POST['email'] 
        password1=request.POST['password1'] 
        password2=request.POST['password2'] 

        user=User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        return redirect('/')
    
    
    else:
        return render(request, 'register.html')
