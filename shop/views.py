from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse,HttpResponse
from .models import Product,Order,OrderItem
import json
from .forms import ShippingForm

# Create your views here.
def product_list(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
        cart_items = order.get_cart_quantity
    else:
        items=[]    
        order = {"get_cart_quantity":0,"get_cart_total":0}
        cart_items = 0
    products = Product.objects.all()
    return render(request,"shop/productList.html",{
        "productlist":products,
        "cart_items":cart_items
    })

def product_detail(request,pk):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
        cart_items = order.get_cart_quantity
    else:
        items=[]    
        order = {"get_cart_quantity":0,"get_cart_total":0}
        cart_items = 0
    product = get_object_or_404(Product,pk=pk)
    return render(request,"shop/productDetail.html",{
        "product":product,
        "cart_items":cart_items
    })

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
        cart_items = order.get_cart_quantity
    else:
        try:
            cart = json.loads(request.COOKIES['cart'])
        except:
            cart = {}         
        print("Cart:",cart)           
        items=[]    
        order = {"get_cart_quantity":0,"get_cart_total":0}
        cart_items = order["get_cart_quantity"]
        for i in cart:
            cart_items += cart[i]["quantity"]
    return render(request,"shop/cart.html",{
        "items":items,
        "order":order,
        "cart_items":cart_items
    })

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
        cart_items = order.get_cart_quantity
    else:
        items=[]  
        order = {"get_cart_quantity":0,"get_cart_total":0}
        cart_items = 0
    if request.method == "POST":
        form = ShippingForm(request.POST)
        if form.is_valid():
            shiping = form.save(commit=False)
            shiping.customer = customer
            shiping.order = order
            shiping.save()
            order.complete = True
            order.save()
            return HttpResponse("success")
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