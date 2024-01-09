from django.shortcuts import render
from django.db.models import Q
from product.models import Product


# Create your views here.
def search_view(request):
    query = request.GET.get('q', '')  # Get the query from request
    if query:
        # Perform the search across desired fields
        products = Product.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
    else:
        products = Product.objects.none()  # Return an empty query if no search term

    context = {
        'query': query,
        'product': products,
    }
    return render(request, 'search/search_results.html', context)
