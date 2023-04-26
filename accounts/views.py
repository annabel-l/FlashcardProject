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
        user = User.objects.create_user(username, email, password)
        user.set_password(password)
        if user != None: 
            newUser = authenticate(request, username = username, password = password)
            return redirect("/login")
    return render( request, "account.html", {"form":form})

def loginCheck(request):
    form = LoginForm(request.POST or None)
    if form.is_valid(): 
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username = username, password = password)
        if user != None:
            login(request, user)
            request.session['userId'] = user.id
            request.session['sort']=None
            return redirect("/")
    return render( request, "account.html", {"form":form})

def logoutCheck(request):
    logout(request)
    request.session['userId'] = None
    return redirect("/")
        