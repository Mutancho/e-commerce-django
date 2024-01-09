from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('perfumes/', views.perfume_view, name='perfumes'),
    path('beauty/', views.health_and_beauty_view, name='health_and_beauty'),
    path('load-more-products/', views.load_more_products, name='load_more_products'),
]
