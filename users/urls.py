# users/urls.py
from django.urls import path

from .views import (register, CustomLoginView, CustomLogoutView, CustomPasswordChangeView, PasswordChangeDoneView,
                    CustomPasswordResetView, CustomPasswordResetDoneView, CustomPasswordResetConfirmView,
                    CustomPasswordResetCompleteView)

app_name = 'users'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),

    # logged user password reset
    path('password_change/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),

    # forgotten password reset
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),

    path('password_reset_sent/', CustomPasswordResetDoneView.as_view(), name='password_reset_sent'),

    path('password_reset_confirm/<uidb64>/<token>/',
         CustomPasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('password_reset_complete/',
         CustomPasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
]
