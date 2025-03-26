from django.shortcuts import render,redirect
from django.contrib import messages
from django.conf import settings 
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from shop.models import customer
from django.contrib.auth.decorators import login_required
from shop.models import Product

# Create your views here.
def home(request):
    print(request.user.is_authenticated)
    products = Product.objects.all()
    return render(request,"base_auth/index.html",{
        "productlist":products
    })
def about(request):
    return render(request,"base_auth/about.html")
def login_page(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email,password=password)
        if user is not None:
            print("ttttt")
            login(request,user)
            return redirect("homepage")
        else:
            messages.error(request,'bad credentials')
            print("bad credentials")
            return redirect('loginPage')

    return render(request,'base_auth/login.html')

def signUp(request):
    if request.method == 'POST':
        uname = request.POST['username']
        email = request.POST['email']
        pword1 = request.POST['pword']
        pword2 = request.POST['cpword']
        
        if User.objects.filter(email=email):
            messages.error(request,"Email already exists")
            print("Email already exists")
            return redirect('register_page')
        elif pword1 != pword2:
            messages.error(request,"Passwords do not match")
            print("Passwords do not match")
            return redirect('register_page')

        myuser = User.objects.create_user(email,email,pword1)
        myuser.save()
        messages.success(request,'Successfully regestered ,We have sent you a confirmation mail. Please activate your account by clicking it.')

        customer.objects.create(user = myuser,name= uname,email=email)

        subject = "Welcome to SWAYNA Fashions"
        msg = f"Hi {uname} \nThank you for registering with us! We are thrilled to have you as part of our community. 🎉 \nFeel free to explore our wide range of products and start shopping. If you have any questions or need assistance, don’t hesitate to reach out to our friendly customer support team. \nHappy shopping, and welcome aboard! \nsBest regards, SWAYNA"
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, msg, from_email, to_list, fail_silently=True)
        print(" do not match")
        return redirect("loginPage")

    return render(request,"base_auth/register.html")


def signout(request):
    logout(request)
    messages.success(request,'Logged out successfully')
    return redirect('homepage')
