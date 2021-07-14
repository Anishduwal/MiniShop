from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='images/')
    desc = models.TextField()
    price = models.PositiveIntegerField()
    offer = models.BooleanField(default=False)
    discount = models.PositiveIntegerField(null=True, blank=True)
    discounted_price = models.PositiveIntegerField(editable = False, null = True)
    is_new = models.BooleanField(default=False)
    
    #default table name in database will be appname_table class name
    class Meta:
        db_table = 'product'
        #bydefault it will automatically append 's' on classname
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.offer:
            if not self.discount:
                raise ValueError('Discount must be set')
            self.discounted_price = self.price - ((self.discount / 100) * self.price)
        return super(Product, self).save(*args, **kwargs)