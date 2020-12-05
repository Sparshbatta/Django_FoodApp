from django.db import models
from cust.models import Client
# Create your models here.

class ReviewOrder(models.Model):
    Bad='Bad'
    Good='Good'
    Average='Average'
    Worst='Worst'
    Excellent='Excellent'
    Unmatchable='Unmatchable'
    choices=(('Bad',Bad), ('Good',Good),('Average',Average),('Worst',Worst),('Excellent',Excellent),('Unmatchable',Unmatchable))
    client=models.ForeignKey(Client,on_delete=models.CASCADE)
    review=models.TextField(default='',blank=True,max_length=1000)
    rating=models.CharField(choices=choices,default=Good,max_length=15)

    def __str__(self):
        return "{} - {}".format(self.client.user.username,self.rating)