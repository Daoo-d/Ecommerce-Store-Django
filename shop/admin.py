from django.contrib import admin
from .models import customer,Product,Order,OrderItem,PlaceOrder

# Register your models here.
admin.site.register(customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(PlaceOrder)
