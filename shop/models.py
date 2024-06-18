from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=100,null=True)
    email = models.EmailField(null=True)

    def __str__(self) -> str:
        return self.name

# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     description =models.TextField()
#     price = models.FloatField()
#     # image
#     def __str__(self):
#         return self.name
    
# class order()    