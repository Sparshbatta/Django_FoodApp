from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class MainDish(models.Model):
	INDIAN='Indian'
	AMERICAN='American'
	CHINESE='Chinese'
	ITALIAN='Italian'
	TYPE_CHOICES=[(INDIAN,'Indian'),(AMERICAN,'American'),(CHINESE,'Chinese'),(ITALIAN,'Italian')]
	name=models.CharField(max_length=40)
	type=models.CharField(max_length=20,choices=TYPE_CHOICES,default=AMERICAN)
	desc=models.TextField(max_length=1000)
	image=models.FileField(upload_to='dishes/images/')
	price=models.FloatField(default=0.0)

	def __str__(self):
		return "{} - {}".format(self.name,self.type)


# class Cust_Cuisine(models.Model):
# 	user=models.OneToOneField(User,on_delete=models.CASCADE)
# 	cuisine=models.OneToOneField(MainDish,on_delete=models.CASCADE)
	
