from .models import Cart, CartItem
from .views import _cart_id


def counter(request):
    if request.path.startswith('/admin'):
        return {}

    cart_count = 0

    if request.user.is_authenticated:
        # Logged-in user: count items by user, no need for session cart
        cart_items = CartItem.objects.filter(user=request.user)
        cart_count = sum(item.quantity for item in cart_items)
    else:
        # Anonymous user: use session-based cart
        try:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_items = CartItem.objects.filter(cart=cart)
            cart_count = sum(item.quantity for item in cart_items)
        except Cart.DoesNotExist:
            cart_count = 0

    return {'cart_count': cart_count}
