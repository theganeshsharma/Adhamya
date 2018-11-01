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
                'newsfeed': NewsFeed.objects.order_by("Priority"),
            }
            return render(request, 'homePage/index.html', context)
        else:
            context={
                'newsfeed':NewsFeed.objects.order_by("Priority"),
            }
            return render(request,'homePage/index.html',context)

    if request.method == "POST":
        return redirect('homePage:index')




#--register--

def registration(request):
    if request.method == "GET":
        return render(request,'homePage/register.html')

    if request.method == "POST":
        ufname=request.POST.get("reg-fname",None)
        ulname=request.POST.get("reg-lname",None)

        uemail = request.POST.get("reg-email",None)
        upass = request.POST.get("reg-pass",None)
        uphone = request.POST.get("reg-uid",None)
        ucat = request.POST.get("reg-category",None)
        new_user = User.objects.create(first_name=ufname,last_name=ulname,username=uID,email=uemail,password=upass)
        new_user.set_password(upass)
        new_mem = Member.objects.get(user=new_user)
        new_mem.MobileNo = uphone
        new_mem.category = ucat

        if ucat=="alumni":
            new_mem.usn =None

        new_mem.save()
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
        user = Member.objects.filter(user__email=usermail).exists()
        if not user:
            return render(request,'homePage/login.html',{'emailnotexist':"No records found for the entered Email"})
        username = user.user.username
        password = request.POST.get("login-password",None)

        guest = authenticate(username=username,password=password)
        if guest is not None:
            if guest.is_active:
                login(request, guest)
                return redirect('homePage:index')

        return render(request, 'homePage/login.html', context={'error': "Invalid Password"})




def news_sub(request):
    if request.method=="POST" or request.method=="GET":
        newsubscriber=request.POST.get("sub-email",None)
        check_email = Subscribers.objects.filter(email_id=newsubscriber).exists()
        if check_email:
            context={
                'exists':"You have already subscribed to Adhamya's Newsletter.",
            }

        else:
            newinst= Subscribers.objects.create(email_id=newsubscriber)
            newinst.save()
            context = {
                'subcriptionsuccess':"Thank you for Subscribing! You'll receive response from our end soon."
            }

        return render(request,'homePage/subscribesuccess.html',context=context)


def dashboard(request):
    #Not handling dashboard with user as parameter to avoid people trying to pass
    #other parameters to unlock other user's dashboard
    if request.method == "GET":
        if request.user.is_authenticated:
            current_user = request.user
            member_instance = Member.objects.get(user=current_user)
            participation_instances = Participation.objects.filter(student=member_instance)
            context={
                'member':member_instance,
                'participations':participation_instances,
            }
            return render(request,'homePage/dashBoard.html',context)

        else:
            return redirect('homePage:login')

    if request.method == "POST":
        return redirect('homePage:dashBoard')


def user_logout(request):
    logout(request)
    return redirect('homePage:index')