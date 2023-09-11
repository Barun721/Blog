from django.shortcuts import render
from accounts.forms import user_login2,UserCreateForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.shortcuts import redirect


# Create your views here.
  #render to display the form

def index(request):
    return render(request,"index.html",)

def registration(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            print("Registration successfull")
    else:
        form = UserCreateForm()
    return render(request,"register.html",{"form":form})

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username,password = password)
        if user:
            if user.is_active:                  
                login(request,user)
                return redirect('accounts:index')
            else:
                return HttpResponse("User is not active")
        else:
            return HttpResponse('Please check your cred.')    
    return render(request,"user_login.html",{})

def user_logout(request):
    logout(request)
    return redirect('accounts:index')