from django.shortcuts import render
from product.models import Product


# Create your views here.
def cart_detail(request):
    cart = request.session.get('cart', {})
    product_ids = cart.keys()
    # Get product objects and add quantity to them
    products = [
        {'product': Product.objects.get(pk=id), 'quantity': qty}
        for id, qty in cart.items()
    ]
    return render(request, 'cart/cart.html', {'cart': products})
