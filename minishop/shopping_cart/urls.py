from django.conf.urls import url
from django.urls import path, include


# from .views import (
#     add_to_cart,
#     delete_from_cart,
#     order_details,
#     checkout,
#     process_payment,
#     update_transaction_records,
#     success
# )
from .views import add_to_cart
app_name = 'shopping_cart'

urlpatterns = [
    path('add_to_cart/<int:product_id>/', add_to_cart, name = 'add_to_cart_2'),
    # url(r'^add-to-cart/(?P<item_id>[-\w]+)/$', name='add_to_cart'),
    # url(r'^order-summary/$', order_details, name='order_summary'),
    # url(r'^success/$', success, name='purchase_success'),
    # url(r'^item/delete/(?P<item_id>[-\w]+)/$', delete_from_cart, name='delete_from_cart'),
    # url(r'^checkout/$', checkout, name='checkout'),
    # url(r'^payment/(?P<item_id>[-\w]+)/$', process_payment, name='process_payment'),
    # url(r'^update-transaction/(?P<item_id>[-\w]+)/$', update_transaction_records, name='update_records')
]