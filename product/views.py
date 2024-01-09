from django.http import JsonResponse
from .models import Product


# Create your views here.
def get_product_price(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        return JsonResponse({'price': str(product.sell_price)})
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status=404)



