from django.contrib import admin
from .models import Product

# Register your models here.
class ProductApp(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'discount', 'discounted_price', 'is_new')
    
    
admin.site.register(Product, ProductApp)