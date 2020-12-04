from django.shortcuts import render
from django.urls import path
from . import views

urlpatterns=[
    path('user_review/',views.user_review,name="user_review"),
    path('thanksnote/',views.thanksnote,name="thanksnote")
]