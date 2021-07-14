from django.shortcuts import render
from django.http import HttpResponse
from . models import Item

# Create your views here.
def shop(request):
    items = Item.objects.all()
    return render(request, 'shop.html', {'items': items})
