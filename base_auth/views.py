from django.shortcuts import render
from shop.models import Product

# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request,"base_auth/index.html",{
        "productlist":products
    })
def about(request):
    return render(request,"base_auth/about.html")