from django.urls import path
from . import views

urlpatterns = [
    path("",views.product_list,name="productlist_page"),
    path("productdetail/",views.product_detail,name="product_page")
]
