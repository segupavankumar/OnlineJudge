from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
import requests



def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect')
            return render(request, 'login.html')
    return render(request,'login.html')
    # login function

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request,'registration.html', {'form': form})

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    data = requests.get('http://127.0.0.1:8000/api/v1/problems?format=json').json()
    return render(request,'home.html',{'data':data})

@login_required(login_url='login')
def problem_view(request,id):
    data = requests.get(f'http://127.0.0.1:8000/api/v1/problems/{id}?format=json').json()
    return render(request,'problem_view.html',{'data':data})