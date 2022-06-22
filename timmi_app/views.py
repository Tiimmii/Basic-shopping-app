from math import prod
from posixpath import split
from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Products
from django.contrib.auth.models import User, auth
from django.contrib import messages



def products(request):
    products = Products.objects.all()
    return render(request, 'index.html', {"goods": products})

def search(request):
    if request.method=='POST':
        search=request.POST['search']
        objects=Products.objects.filter(name__contains=search)
        return render(request, 'search.html', {'search':search, 'object':objects})
    else:
        return render(request, 'search.html',{})
def signup(request):
    if request.method=='POST':
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        password2=request.POST['password2']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']

    
        if len(email)>0:
            if len(username)>0:
                if len(password)>0:
                    if password==password2:
                        if User.objects.filter(email=email).exists():
                            messages.info(request, 'Email already exists')
                            return redirect('signup')
                        elif User.objects.filter(username=username).exists():
                            messages.info(request, 'username already exists')
                            return redirect('signup')
                        else:
                            user = User.objects.create_user(username=username, password=password, email=email)
                            user.save();
                            return redirect('login')
                    else:
                            messages.info(request, 'passwords do not match')
                            return redirect('signup')
                else:
                    messages.info(request, 'password field required')
                    return redirect('signup')
            else:
                messages.info(request, 'username field required')
                return redirect('signup')
            
        else:
            messages.info(request, 'email field required')
            return redirect('signup')
    else:
        return render(request, 'signup.html', {})

def login(request):
    if request.method=='POST':
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']

        if len(email)>0:
            if len(username)>0:
                if len(password)>0:
                    user = auth.authenticate(username=username, password=password)

                    if user is None:
                        messages.info(request,'User not found')
                        return redirect('login')
                    else:
                        auth.login(request, user)
                        return redirect('products')
                else:
                    messages.info(request, 'password field required')
                    return redirect('login')
            else:
                messages.info(request, 'username field required')
                return redirect('login')
        else:
            messages.info(request, 'email field required')
            return redirect('login')
    else:
        return render(request, 'login.html',{})



    