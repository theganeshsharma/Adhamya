from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout

from .models import *


#--home Page--
def index(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            user = request.user
            context = {
                'member': Member.objects.filter(user=user),

            }
            return render(request, 'homePage/index.html', context)
        else:
            return render(request,'homePage/index.html')

    if request.method == "POST":
        return redirect('homePage:index')




#--register--

def registration(request):
    if request.method == "GET":
        return render(request,'homePage/register.html')

    if request.method == "POST":
        ufname=request.POST.get("reg-fname",None)
        ulname=request.POST.get("reg-lname",None)
        uID =request.POST.get("reg-uid",None)
        uemail = request.POST.get("reg-email",None)
        upass = request.POST.get("reg-pass",None)
        uphone = request.POST.get("reg-phone",None)
        ucat = request.POST.get("reg-cat",None)
        new_user = User.objects.create(first_name=ufname,last_name=ulname,username=uID,email=uemail,password=upass)
        new_user.set_password(upass)
        new_mem = Member.objects.create(user=new_user,MobileNo=uphone,category=ucat)

        context={
            'member':new_mem,
            'regsuccess':"Successfully Registered! Login using the credentials",
        }

        return render(request,'homePage/login.html',context)




#--login--
def user_login(request):
    if request.method=="GET":
        return render(request, 'homePage/login.html')
    if request.method=="POST":
        usermail = request.POST.get("login-email",None)
        user = Member.objects.get(user__email=usermail)
        username = user.user.username
        password = request.POST.get("login-password",None)

        guest = authenticate(username=username,password=password)
        if guest is not None:
            if guest.is_active:
                login(request, guest)
                return redirect('homePage:index')

        return render(request, 'homePage/login.html', context={'error': "Invalid Credentials"})






