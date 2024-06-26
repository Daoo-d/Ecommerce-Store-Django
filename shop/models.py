from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class ShortUUIDField(models.UUIDField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 10  # Set a shorter max length
        super().__init__(*args, **kwargs)

class customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=100,null=True)
    email = models.EmailField(null=True)

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description =models.TextField(null=True,blank=True)
    price = models.FloatField()
    image = models.ImageField(null=True,blank=True)
    def __str__(self):
        return self.name
    
class Order(models.Model):
    customer = models.ForeignKey(customer,on_delete=models.SET_NULL,blank=True,null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)   
    complete = models.BooleanField(default=False)
    transaction_id = ShortUUIDField(unique=True, default=uuid.uuid4, editable=False)

    def __str__(self) -> str:
        return str(self.id)
    
    @property
    def  get_cart_total(self):
        items = self.orderitem_set.all()
        total = sum([item.get_total for item in items])
        return total
    
    @property
    def  get_cart_quantity(self):
        items = self.orderitem_set.all()
        total = sum([item.quantity for item in items])
        return total
    
class OrderItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,blank=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=0)  

    @property
    def get_total(self):
        total = self.product.price*self.quantity
        return total
      
class PlaceOrder(models.Model):
    customer = models.ForeignKey(customer,on_delete=models.SET_NULL,null=True,blank=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True,blank=True)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=100,null=True)      
    contact = models.CharField(max_length=20)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address