from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate

from .models import Product, Business


def register(request):
    if request.method == 'GET':
        return render(request, 'products/register.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('dashboard')
            except IntegrityError:
                return render(request, 'products/register.html', {'form': UserCreationForm(), 'error': 'This username has already been taken. Please choose another one!'})

        else:
            return render(request, 'products/register.html', {'form': UserCreationForm(), 'error': 'Passwords did not match'})

def dashboard(request):
    return render(request, 'products/dashboard.html')

def technology(request):
    products = Product.objects.all()
    return render(request, 'products/tech_product_list.html', {'products': products})

def business(request):
    business_product = Business.objects.all()
    return render(request, 'products/business_product.html', {'business_product': business_product})


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'products/login.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'products/login.html', {'form': AuthenticationForm(), 'error': 'Username and password did not match'})
        else:
            login(request, user)
            return redirect('dashboard')

def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('register')
