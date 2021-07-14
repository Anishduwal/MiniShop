from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

from miniapp.models import Product
from shop.models import Item

# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField(null = True, blank = True)
    is_ordered = models.BooleanField(default = False)
    ordered_date = models.DateField(auto_now=True) #auto_now store everytime save function is called, auto_now_add stores data one time only

    def __str__(self):
        return self.product.name + ' of ' + self.user.get_full_name()

    