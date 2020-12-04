from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Client
from django.conf import settings
from Dish.models import MainDish
from Order.models import Order
import os
import datetime
import re
# Create your views here.





def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        password1=request.POST['password']
        password2=request.POST['repassword']
        email=request.POST['email']
        phone=request.POST['phone']
        address=request.POST['address']
        city=request.POST['city']

        try:
            prime = request.POST['prime']
            if prime == "on":
                prime = True
        except:
            prime = False
        state=request.POST['state']
        image=request.FILES['image']

        

        if User.objects.filter(username=username).exists():
            messages.error(request,'Username already taken')
            return redirect('/user/signup/')
        
        elif re.findall(r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$",email)==False:
            messages.error(request,'Invalid Email')
            return redirect('/user/signup')

        elif User.objects.filter(email=email).exists():
            messages.error(request,"Email already taken")
            return redirect('/user/signup/')
        
        elif phone.isnumeric()==False:
            messages.error(request,"Invalid phone number")
            return redirect('/user/signup/')

        elif city.isalnum()==True and city.isalpha()==False:
            messages.error(request,"Invalid city name")
            return redirect('/user/signup/')

        elif password1!=password2:
            messages.error(request,"Password not matched")
            return redirect('/user/signup/')
        else:
            user= User.objects.create_user(username=username,password=password1,email=email)
            new_cust=Client.objects.create(user=user,phone=phone,address=address,city=city,prime=prime,state=state,image=image)
            new_cust.save()
            messages.info(request,"You have been added successfully !!")
            auth.login(request,user)
            return redirect("/")


    else:
        return render(request,'signup.html')


def login(request):
        if request.method=='POST':
           username=request.POST['username']
           password=request.POST['password']
           user=auth.authenticate(username=username,password=password)

           if user is not None:
               auth.login(request,user)
               messages.info(request,"Login Successful!!")
               return redirect("/")
           else:
               messages.info(request,"username or password incorrect")
               return redirect("/user/login/")
        else:
            return render(request,'login.html')


def logout(request):
    auth.logout(request)
    messages.info(request,"Successfully Logged out!!!")
    return render(request,'logout.html')

def account(request):
    username=request.user.username
    user=User.objects.get(username=username)
    client=Client.objects.get(user=user)
    context={'client':client}
    return render(request,'account.html',context)

def history(request):
    username=request.user.username
    user=User.objects.get(username=username)
    client=Client.objects.get(user=user)
    order=Order.objects.filter(user=client)
    context={'client':client,'order':order}
    return render(request, 'history.html',context)


def order_details(request,my_id):
    username=request.user.username
    user=User.objects.get(username=username)
    client=Client.objects.get(user=user)
    time_now=datetime.datetime.now()
    now=time_now.strftime("%m-%d-%Y %H:%M:%S")
    order=Order.objects.get(order_id=my_id, user=client)
    context={'client':client,'order':order,'time_now':now}
    return render(request,'order_details.html',context)

def edit(request):
    if request.method=='POST':
     
        phone=request.POST['phone']
        address=request.POST['address']
        city=request.POST['city']

        try:
            prime = request.POST['prime']
            if prime == "on":
                prime = True
        except:
            prime = False
        state=request.POST['state']
        try:
            image=request.FILES['image']
        except:
            image=None
        

        
        if phone.isnumeric()==False:
            messages.info(request,"Invalid phone number")
            return redirect('/user/edit/')

        elif city.isalnum()==True and city.isalpha()==False:
            messages.info(request,"Invalid city name")
            return redirect('/user/edit/')

        else:
            username=request.user.username
            user=User.objects.get(username=username)
            cust_change=Client.objects.get(user=user)
            cust_change.address=address
            cust_change.city=city
            cust_change.prime=prime
            cust_change.phone=phone
            cust_change.state=state
            if image!= None:
                cust_change.image=image
            cust_change.save()
            messages.info(request,"Changes made successfully!!")
            return redirect("/")
    else:
        username=request.user.username
        user=User.objects.get(username=username)
        client=Client.objects.get(user=user)
        context={'client':client}
        return render(request,'edit.html',context)





