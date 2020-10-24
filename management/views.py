from django.shortcuts import render, redirect
from django.contrib.auth.forms import User
from django.contrib.auth.views import LoginView
from main.forms import UserForm
from main.forms import LoginForm

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            return redirect('base')
        
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        form = LoginForm(request,POST)
        username=request.POST['username']
        password=request.POST['password']
        if user is not None:
            login(request, user)
            return redirect('base')
        else:
            return HttpResponse('Login failed. Try again.')
    else:
        form = LoginForm()
        return render(request, 'login.html')