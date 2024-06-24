import json
from .models import *

def cookieCart(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}         
    print("Cart:",cart)           
    items=[]    
    order = {"get_cart_quantity":0,"get_cart_total":0}
        
    for i in cart:
        try:
            product = Product.objects.get(id=i)
            total = (product.price * cart[i]["quantity"]) 
            order["get_cart_total"] += total
            order["get_cart_quantity"]+=cart[i]["quantity"]

            item = {
                "product":{
                    "id":product.id,
                    "name":product.name,
                    "price":product.price,
                    "image":product.image
                },
                "quantity":cart[i]["quantity"],
                "get_total":total
            }
            items.append(item)
        except:
            pass    
    cart_items = order["get_cart_quantity"]
    return {"cart_items":cart_items,"order":order,"items":items}

def cartData(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
        cart_items = order.get_cart_quantity
    else:
        cookieData = cookieCart(request)
        cart_items = cookieData["cart_items"]
        order = cookieData["order"]
        items = cookieData["items"]
    return {"cart_items":cart_items,"order":order,"items":items}    