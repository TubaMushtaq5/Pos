from django.shortcuts import render
from .models.product import Product
def home(request):
    return render(request, 'mainf/home.html')
    

def about(request):
    return render(request, 'mainf/about.html')

def Dashboard(request):
    return render(request, 'mainf/Dashboard.html')

def User(request):
    return render(request, 'mainf/User.html')

def Inventary(request):
    return render(request, 'mainf/Inventary.html')
def Order(request):
    return render(request, 'mainf/Order.html')
def Settings(request):
    return render(request, 'mainf/settings.html')
def Pos(request):
    prod= Product.get_all_products();
    
    return render(request, 'mainf/Pos.html',{'products':prod})