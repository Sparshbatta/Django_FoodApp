from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Client(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone=models.CharField(max_length=14)
    address=models.CharField(max_length=200)
    city=models.CharField(max_length=40)
    prime=models.BooleanField(default=False)
    state=models.CharField(max_length=40)
    image=models.FileField(upload_to="clients/images/")
    def __str__(self):
        return "{}".format(self.user.username)