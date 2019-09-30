from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages



# Create your views here.

def login(request):
    return render(request, 'login.html')

def register(request):

    if request.method =='POST':
        username=request.POST['username'] 
        email=request.POST['email'] 
        password1=request.POST['password1'] 
        password2=request.POST['password2'] 

        if password1== password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken !')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken !')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                print('User Created !')
                return redirect('/')
        else:
            messages.info(request, 'Password not matched ')
            return redirect('register')
        return redirect('/')


    else:
        return render(request, 'register.html')
