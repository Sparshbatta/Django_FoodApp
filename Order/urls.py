from django.urls import path
from . import views

urlpatterns=[

    path('<str:my_name>',views.purchase,name="purchase"),
    path('placed/<str:my_name>',views.placed,name="placed"),
    path('order_history/deleteall/',views.delete,name="delete"),
    path('delete/<int:my_id>',views.cancel,name="cancel")

]