from .models import Cart, CartItem
from .views import _cart_id



def counter(request):
    cart_count = 0
    if request.path.startswith('/admin'):
       return {}
    else:
        try:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_items = CartItem.objects.all().filter(cart=cart)
            cart_count = sum(item.quantity for item in cart_items)
        except Cart.DoesNotExist:
            cart_count = 0
    return {'cart_count':cart_count}