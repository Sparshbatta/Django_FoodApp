from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from cust.models import Client
from .models import ReviewOrder
from django.contrib import messages
# Create your views here.

def user_review(request):
    username=request.user.username
    user=User.objects.get(username=username)
    client=Client.objects.get(user=user)
    context={'client':client}
    return render(request,"review.html",context)

def thanksnote(request):
    username=request.user.username
    user=User.objects.get(username=username)
    client=Client.objects.get(user=user)
    review_data=request.POST['review']
    rating=request.POST.get('stars')
    ReviewOrder.objects.create(client=client,review=review_data,rating=rating)
    context={'client':client}
    messages.info(request,'Your Review has been successfully submitted !!')
    return redirect('/')
