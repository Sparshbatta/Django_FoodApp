from django.db import models
from cust.models import Client
from Dish.models import MainDish

# Create your models here.


class Order(models.Model):
	order_id=models.AutoField(primary_key=True,unique=True)
	quantity=models.IntegerField(default=1)
	user=models.ForeignKey(Client, on_delete=models.CASCADE)
	cuisine=models.ForeignKey(MainDish, on_delete=models.CASCADE)
	placed_time=models.CharField(default='',max_length=60)
	placed_date=models.CharField(default='',max_length=60)
	delivery_time=models.CharField(default='',max_length=60)
	delivery_date=models.CharField(default='',max_length=60)
	delivery_datetime=models.CharField(default='',max_length=100)
	total_price=models.DecimalField(default=0,decimal_places=3,max_digits=15)



	def __str__(self):
		return "{} - {} - {}".format(self.order_id,self.user.user.username,self.cuisine)