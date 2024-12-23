from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from django.contrib import auth
from django.template.context_processors import request


# Create your views here.
def register(request):

    if request.method == "POST":  # form method post which is equals to this POST
        username = request.POST['username']    #naseem
        email = request.POST['email']          #naseemahammad45@gmail.com
        password1 = request.POST['password']   #welocme@1234
        password2 = request.POST['password2']  #welcome@1234

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                print("Username Already Exist Please Try Another Username")
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    print("Email Is Already Take Please Try Another One")
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, email=email, password=password1)
                    user.save()
                    return redirect('login')
        else:
            print("Password Didnt Matched")
            return redirect('register')

    else:
        return render(request,'register.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']   #naseem
        password = request.POST['password']   #welcome@1234

        user = auth.authenticate(username=username, password=password)

        if User is not None:                  # if the condition is true.
            auth.login(request, user)
            print("Login Successfull")
            return redirect('showproducts')

        else:
            print("Invalid Credentials")
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        print("You have been logged out from the Website")
    return render(request, "login.html")