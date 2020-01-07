from django.shortcuts import render,redirect
from django.contrib.auth import authenticate ,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    return render(request, 'app/home.html',{})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request, user)
            messages.success(request,('you successfully Logged In.'))
            return redirect('home')
        else:
            messages.success(request,('Username or Password is incorrect.'))
            return redirect('login')

    else:
        return render(request, 'app/login.html',{})

def logout_user(request):
    messages.success(request,('you successfully Logged out.'))
    logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['password1']:
            try:
                user = User.objects.get(username = request.POST['username'])
                messages.success(request,('Username is already taken.'))
                return redirect('register')
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],request.POST['password'])
                login(request,user)
                messages.success(request,('you successfully register'))
                return redirect('home')
    else: 
        return render(request,'app/register.html')
