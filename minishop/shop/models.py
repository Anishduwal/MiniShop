from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='images')
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
