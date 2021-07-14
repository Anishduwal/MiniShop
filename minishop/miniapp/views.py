from django.shortcuts import render
from django.http import HttpResponse
from . models import Product
# Create your views here.

def home(request):
    prods = Product.objects.all()
    return render(request,'index.html', {'prods': prods})

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')


def blog_single(request):
    return render(request, 'blog-single.html')

def product_single(request):
    return render(request, 'product-single.html')