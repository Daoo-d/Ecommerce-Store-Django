"""
URL configuration for swayna project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from shop import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("swayna/",include("base_auth.urls")),
    path("swayna/shop/",include("shop.urls")),
    path("swayna/blog/",include("blog.urls")),
    path('update_item/',views.updateItem,name="update_item")
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
