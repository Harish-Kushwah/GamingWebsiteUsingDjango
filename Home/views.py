from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.contrib import messages  #this is for using inbuilt messages of django 

from django.contrib.auth import authenticate,login,logout
from hangman import settings
from django.core.mail import send_mail


def home(request):
    return render(request,"index.html")


def signout(request):
    # logout(request)
    messages.success(request,"Logout successfully ")
    return redirect(request,"index.html")


def signin(request):
    if request.method=='POST':
        username=request.POST['username']
        pass1=request.POST['password']

        user=authenticate(username=username,password=pass1)
        if user is not None:
            login(request ,user)
            fname=user.first_name
            return render(request,"index.html" ,{'fname':fname})
            
        else:
            messages.error(request,"Enter valid credentials")
            return redirect('home')
    return render(request,"signin.html")

def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        fname=request.POST['firstname']
        lname=request.POST['lastname']
        email=request.POST['email']
        password=request.POST['password']

        if User.objects.filter(username=username):
            messages.error(request,"Username already exist")
            return redirect('home')
        
        if User.objects.filter(email=email):
            messages.error(request,"Email already exist")
            return redirect('home')
        
        if len(username)>10:
            messages.error(request,"Username must be less than 10 character")
            return redirect('home')

        if not username.isalnum():
            messages.error(request,"Username must be alphanumeric")
            return redirect('home')

        
        myuser=User.objects.create_user(username,email,password)
        myuser.first_name=fname
        myuser.last_name=lname

        myuser.save()

        messages.success(request,"Your account created successfully")


    # welcome email
        subject="Welcome on Hangman "
        message="Hello" + myuser.first_name + "!!\n" +"Welcome on Hangman \n"+"Thank you we have also send you a confirm email \n"

        from_email=settings.EMAIL_HOST_USER
        to_list=[myuser.email]
        send_mail(subject,message,from_email,to_list,fail_silently=True)
        return redirect('signin')

    return render(request,"signup.html")


