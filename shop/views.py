from django.shortcuts import render,get_object_or_404
from .models import Product

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    return render(request,"shop/productList.html",{
        "productlist":products
    })

def product_detail(request,pk):
    product = get_object_or_404(Product,pk=pk)
    return render(request,"shop/productDetail.html",{
        "product":product
    })