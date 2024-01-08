from django.urls import path
from .views import get_product_price

app_name = 'product'

urlpatterns = [
    path('get-product-price/<int:pk>/', get_product_price, name='get-product-price'),
]
