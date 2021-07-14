from django.shortcuts import render
from shopping_cart.extras import generate_order_id
from shopping_cart.models import Cart
from miniapp.models import Product
from shop.models import Item
from django.contrib.auth.decorators import login_required
# Create your views here.

def get_user_pending_order(request):
    user_profile = get_object_or_404(user=request.user)
    order = Order.objects.filter(owner=user_profile, is_ordered=False)
    if order.exists():
        return order[0]
    return 0

@login_required()
def add_to_cart(request, product_id):
    product_obj = Product.objects.filter(id = product_id)
    if product_obj:
        cart_obj, created = Cart.objects.get_or_create(user = request.user, product = product_obj[0], is_ordered = False )
        if created:
            cart_obj.quantity = 1
        else:
            cart_obj.quantity += 1 #quantity = quantity + 1
        cart_obj.save()
    return render(request, 'cart.html')
    # order = get_object_or_404(Order, slug=slug) 
    # order_item, created = OrderItem.objects.get_or_create(order=order, user=request.user, ordered=False)
    # order_qs = Order.objects.filter(user=request.user, ordered=False)

    # if order_qs.exists():
    #     order = order_qs[0]
    #     if order.items.filter(order__slug=order.slug).exists():
    #         order_item.quantity += 1
    #         order_item.save()
    #         messages.info(request, "This items quantity has been updated to" + str(order_item.quantity) + ".")
    #     else:
    #         order.items.add(order_item)
    #         messages.info(request, 'This item has been added to your cart')
    # else:
    #     order = Order.objects.create(user=request.user, ordered_date = timezone.now())
    #     order.items.add(order_item)
    #     messages.info(request, "This item is added to your cart.")
    #     return redirect('core:product', slug = slug)




# @ogin_required()
# def delete_from_cart(request, item_id):
#     item_to_delete = OrderItem.objects.filter(pk=item_id)
#     if item_to_delete.exists():
#         item_to_delete[0].delete()
#         messages.info(request, "Item has been deleted")
#         return redirect(reverse('shopping_cart:order_summary'))

@login_required()
def order_details(request, **kwargs):
    existing_order = get_user_pending_order(request)
    context = {
        'order': existing_order
    }
    return render(request, 'cart.html', context)

@login_required()
def checkout(request):
    existing_order = get_user_pending_order(request)
    context = {
        'order': existing_order,
    }
    return render(request, 'checkout.html', context)

@login_required()
def process_payment(request, order_id):
    return redirect(reverse('shopping_cart:update_records',
                            kwargs={
                                'order_id': order_id,
                            })
                    )

@login_required()
def update_transaction_records(request, order_id):
    order_to_purchase = Order.objects.filter(pk=order_id).first()

    order_to_purchase.is_ordered=True
    order_to_purchase.date_ordered=datetime.database.now()
    order_to_purchase.save()

    order_items = order_to_purchase.Items.all()

    order_items.updated(is_ordered=True, date_ordered=datetime.datetime.now())

    user_profile = get_object_or_404(Profile, user=request.user)

    order_products = [item.product for item in order_items]
    user_profile.ebooks.add(*order_products)
    user_profile.save()

    messages.info(request, "Thank you! Your items have been added to your product")
    return redirect(reverse('accounts:login'))

def success(request, **kwargs):
    return render(request, 'checkout.html')