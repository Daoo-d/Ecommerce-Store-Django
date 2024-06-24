from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse,HttpResponse
from .models import Product,Order,OrderItem,customer
import json
from .forms import ShippingForm
from .utils import cookieCart,cartData

# Create your views here.
def product_list(request):
    data = cartData(request)
    cart_items = data["cart_items"]
    order = data["order"]
    items = data["items"]
    products = Product.objects.all()
    return render(request,"shop/productList.html",{
        "productlist":products,
        "cart_items":cart_items
    })

def product_detail(request,pk):
    data = cartData(request)
    cart_items = data["cart_items"]
    order = data["order"]
    items = data["items"]
    product = get_object_or_404(Product,pk=pk)
    return render(request,"shop/productDetail.html",{
        "product":product,
        "cart_items":cart_items
    })

def cart(request):
    data = cartData(request)
    cart_items = data["cart_items"]
    order = data["order"]
    items = data["items"]
    return render(request,"shop/cart.html",{
        "items":items,
        "order":order,
        "cart_items":cart_items
    })

def checkout(request):
    data = cartData(request)
    cart_items = data["cart_items"]
    order = data["order"]
    items = data["items"]

    if request.method == "POST":
        form = ShippingForm(request.POST)
        if request.user.is_authenticated:
            cust = request.user.customer
            order,created = Order.objects.get_or_create(customer=cust,complete=False)
        else:
            name = request.POST.get('name')
            email = request.POST.get('email')       
            cust,created = customer.objects.get_or_create(email=email)   
            cust.name = name
            cust.save() 
            order,created = Order.objects.get_or_create(customer=cust,complete=False)
            for item in items:
                product = Product.objects.get(id=item["product"]["id"])
                orderItem = OrderItem.objects.create(
                    product = product,
                    order = order,
                    quantity = item["quantity"]
                )

        if form.is_valid():
            shiping = form.save(commit=False)
            shiping.customer = cust
            shiping.order = order
            shiping.save()
            order.complete = True
            order.save()
           
            response = HttpResponse("success")
            response.delete_cookie("cart")
            return response
    form = ShippingForm()
    return render(request,"shop/checkout.html",{
        "items":items,
        "order":order,
        "cart_items":cart_items,
        "form":form
    })    

def updateItem(request):
    data = json.loads(request.body)
    productid = data['productid']
    action = data['action']

    print('Action',action)
    print('ProductID',productid)

    customer = request.user.customer
    product = Product.objects.get(id=productid)
    order,created = Order.objects.get_or_create(customer=customer,complete = False)
    orderItem,created = OrderItem.objects.get_or_create(order=order,product=product)

    if action == 'add':
        orderItem.quantity += 1
    elif action == 'remove':
        orderItem.quantity -= 1

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()        
    return JsonResponse("Item was added",safe=False)