from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('home', views.home, name="home"),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('blog', views.blog, name='blog'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('blog-single', views.blog_single, name='blog-single'),
    path('product-single', views.product_single, name='product-single'),
]