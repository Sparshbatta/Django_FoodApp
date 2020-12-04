
from django.urls import path
from . import views

urlpatterns = [

    path('login/',views.login,name="login"),
    path('signup/',views.signup,name="signup"),
    path('logout/',views.logout,name="logout"),
    path('account/',views.account,name="account"),
    path('history/',views.history,name="history"),
    path('order_details/<int:my_id>/',views.order_details,name="order_details"),
    path('edit/',views.edit,name="edit")


]
