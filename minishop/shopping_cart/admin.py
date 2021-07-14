from django.contrib import admin
from shopping_cart.models import Cart
# Register your models here.
class CartApp(admin.ModelAdmin):
    list_display = ('id', 'quantity', 'is_ordered', 'ordered_date')\


admin.site.register(Cart, CartApp)
