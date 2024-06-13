from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"base_auth/index.html")
def about(request):
    return render(request,"base_auth/about.html")