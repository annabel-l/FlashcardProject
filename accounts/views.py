from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from cards.views import *

# Create your views here.
from .forms import LoginForm, RegisterForm

User = get_user_model()

def registerCheck(request):
    form = RegisterForm(request.POST or None)
    
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        email = None
        try:
            user = User.objects.create_user(username, email, password)
            user.set_password(password)
        except: user = None
        if user != None: 
            login(request, user)
            return redirect("login/")
    return render( request, "account.html", {"form":form})

def loginCheck(request):
    form = LoginForm(request.POST or None)
    if form.is_valid(): 
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username = username, password = password) #checks if valid user and password, returns None if invalid password
        #if user == None:
        #    return render(request, "forms.html", {"form":form, "invalid_user":True})
        if user != None:
            login(request, user) #logs in user, redirects them home, otherwise goes to auto login page
            return redirect("/")
    return render( request, "account.html", {"form":form})

def logoutCheck(request):
    logout(request)
    return redirect("/")
        