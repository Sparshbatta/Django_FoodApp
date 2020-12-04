from django.shortcuts import render
from django.http import HttpResponse
from cust.models import Client
from django.contrib.auth.models import User
from Dish.models import MainDish


def details(request,my_name):

    data=MainDish.objects.get(name=my_name)
    username=request.user.username
    user=User.objects.get(username=username)
    client=Client.objects.get(user=user)
    if client.prime==True:
        price=data.price*0.9
    else:
        price=data.price
    price="{:.3f}".format(price)
    context={'data':data,'client':client,'price':price}
    return render(request,'details.html',context)



def base(request):
    username=request.user.username
    try:
        user=User.objects.get(username=username)
        data=Client.objects.get(user=user)
        context={'client':data}
        return render(request,'base.html',context)

    except:

        context={}
        return render(request,'base.html',context)
    
def index(request):
    username=request.user.username

    dish_Indian=MainDish.objects.filter(type="Indian")
    dish_American=MainDish.objects.filter(type="American")
    dish_Chinese=MainDish.objects.filter(type="Chinese")
    dish_Italian=MainDish.objects.filter(type="Italian")

    number_Indian=len(dish_Indian)
    if number_Indian%4==0:
        Indian_result=number_Indian//4
    else:
        Indian_result=number_Indian//4+1


    number_American=len(dish_American)
    if number_American%4==0:
        American_result=number_American//4
    else:
        American_result=number_American//4+1

    number_Italian=len(dish_Italian)
    if number_Italian%4==0:
        Italian_result=number_Italian//4
    else:
        Italian_result=number_Italian//4+1

    number_Chinese=len(dish_Chinese)
    if number_Chinese%4==0:
        Chinese_result=number_Chinese//4
    else:
        Chinese_result=number_Chinese//4+1
    try:
        user=User.objects.get(username=username)
        data=Client.objects.get(user=user)
        context={

        'client':data,'dish_Indian':dish_Indian, 'dish_American':dish_American, 'dish_Chinese':dish_Chinese, 
        'dish_Italian':dish_Italian, 'range_Indian':range(0,Indian_result),'range_American':range(0,American_result),
        'range_Chinese':range(0,Chinese_result),'range_Italian':range(0,Italian_result)

        }
        return render(request,'index.html',context)

    except:
        
        context={'dish_Indian':dish_Indian, 'dish_American':dish_American, 'dish_Chinese':dish_Chinese, 
        'dish_Italian':dish_Italian, 'range_Indian':range(0,Indian_result),'range_American':range(0,American_result),
        'range_Chinese':range(0,Chinese_result),'range_Italian':range(0,Italian_result)}
        return render(request,'index.html',context)

    

def aboutus(request):
    username=request.user.username
    try:
        user=User.objects.get(username=username)
        data=Client.objects.get(user=user)
        context={'client':data}
        return render(request,'aboutus.html',context)

    except:
        user=None
        context={'client':user}
        return render(request,'aboutus.html',context)

