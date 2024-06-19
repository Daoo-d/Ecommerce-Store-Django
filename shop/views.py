from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from .models import Product,Order,OrderItem
import json

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
        cart_items = order.get_cart_quantity
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
        cart_items = order.get_cart_quantity
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
        items=[]    
        order = {"get_cart_quantity":0,"get_cart_total":0}
        cart_items = order.get_cart_quantity
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
        cart_items = order.get_cart_quantity
    return render(request,"shop/checkout.html",{
        "items":items,
        "order":order,
        "cart_items":cart_items
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