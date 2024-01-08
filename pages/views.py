from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def home_view(request):
    return render(request, 'pages/home.html')


def about_view(request):
    return render(request, 'pages/about.html')


def contact_view(request):
    return render(request, 'pages/contact.html')


def health_and_beauty_view(request):
    return render(request, 'pages/health_and_beauty.html')


def perfume_view(request):
    return render(request, 'pages/perfumes.html')
