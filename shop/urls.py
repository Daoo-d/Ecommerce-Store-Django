from django.urls import path
from . import views

urlpatterns = [
    path("",views.product_list,name="productlist_page"),
    path("product/<int:pk>",views.product_detail,name="product_page"),
    path("order/",views.cart,name="order_page"),
    path("checkout/",views.checkout,name="checkout_page")    
]
