from django.shortcuts import render
from .models import * 

# Create your views here.
def index(request):
    products = Product.objects.all()
    products_private =Product.objects.filter(is_private =True)

    context = {'products':products}
    return render(request, 'index.html',context)

def about(request):
    return render(request, 'about.html',{})

def welcome(request):
    return render(request, 'welcome.html',{})

def cart(request):
    return render(request, 'cart.html',{})

def checkout(request):
    return render(request, 'checkout.html',{})