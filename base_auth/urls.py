from django.urls import  path
from . import views

urlpatterns = [
    path("",views.home,name="homepage"),
    path("about/",views.about,name="about_page"),
    path("login/",views.login_page,name="loginPage"),
    path("register/",views.signUp,name="register_page"),
    path("log-out/",views.signout,name="signout_page")
]
