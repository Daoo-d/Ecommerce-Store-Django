from django.shortcuts import render

# Create your views here.
def product_list(request):
    return render(request,"shop/productList.html")

def product_detail(request):
    return render(request,"shop/productDetail.html")