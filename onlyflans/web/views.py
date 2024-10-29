from django.shortcuts import render,redirect
from .models import * 
from django.http import JsonResponse, HttpResponse,HttpResponseRedirect
from .forms import ContactFormForm  
from .models import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():
          form.save()
        return redirect('welcome')  
    else:
       form = ContactFormForm()
    # contact_form= ContactForm.objects.create(**form.cleaned_data)
    
    return render(request, 'contact.html', {'form': form})
    #return HttpResponseRedirect('welcome')

# Create your views here.
def index(request):
    products = Product.objects.all()
    products_public = Product.objects.filter(is_private=False) 
    context = {'products': products_public}
    return render(request, 'index.html',context)

def about(request):
    return render(request, 'about.html',{})

def welcome(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
		#Cracion de carro vacio para empezar
        items = []
    context = {'items':items}
    return render(request, 'welcome.html',context)

def cart(request):
    return render(request, 'cart.html',{})

def checkout(request):
    context = {}
    return render(request, 'checkout.html',context)

def updateItem(request):
    return JsonResponse('Item fue agregado',safe=False)
