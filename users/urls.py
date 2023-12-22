# users/urls.py
from django.urls import path

from . import views
from .views import (
    register,
    CustomLoginView,
    CustomLogoutView,
    CustomPasswordChangeView,
    PasswordChangeDoneView
)

app_name = 'users'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('password_change/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
]
