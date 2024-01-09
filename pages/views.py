from django.shortcuts import render, get_object_or_404
from category.models import Category
from product.models import Product
from django.core.paginator import Paginator, EmptyPage
from django.http import HttpResponse


# Create your views here.


def home_view(request):
    return render(request, 'pages/home.html')


def about_view(request):
    return render(request, 'pages/about.html')


def contact_view(request):
    return render(request, 'pages/contact.html')


def health_and_beauty_view(request):
    return render(request, 'pages/health_and_beauty.html')


def perfume_view(request):
    category = get_object_or_404(Category, name__iexact='perfumes')
    products = Product.objects.filter(category=category, is_visible=True)
    return render(request, 'pages/perfumes.html', {'products': products, 'category': category})


def load_more_products(request):
    page = request.GET.get('page', 1)
    products = Product.objects.all()
    # todo ensure pagination works for product display
    paginator = Paginator(products, 10)

    try:
        products = paginator.page(page)
    except EmptyPage:
        return HttpResponse('')

    # Render the product cards using a partial template
    return render(request, 'pages/product_page_partial.html', {'products': products})
