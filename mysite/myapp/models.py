from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
    #define the fields
    def __str__(self):
        return self.name
    seller_name=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    description=models.CharField(max_length=250)
    image=models.ImageField(blank=True,upload_to='images')