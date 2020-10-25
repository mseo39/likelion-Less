from django.shortcuts import render, redirect
from django.contrib.auth.forms import User
from django.contrib.auth.views import LoginView
from django.contrib import auth
from main.forms import UserForm
from main.forms import LoginForm

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            return redirect('main')
        
    return render(request, 'signup.html')

def login(request):
    if request.method == "POST":
        username=request.POST.get('username',None)
        password=request.POST.get('password',None)
        user=auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('main')
        else:
            return HttpResponse('Login failed. Try again.')
    else:
        return render(request, 'login.html')

def logout(request):
    if request.method=="POST":
        auth.logout(request)
        return redirect('main')
    return render(request, 'login.html')