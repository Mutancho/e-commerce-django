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
    path('reset_password/', CustomPasswordResetView.as_view(), name='reset_password'),

    path('reset_password_sent/', CustomPasswordResetDoneView.as_view(), name='reset_password_sent'),

    path('reset/<uidb64>/<token>/',
         CustomPasswordResetConfirmView.as_view(template_name='users/reset_password_confirm.html'),
         name='reset_password_confirm'),

    path('reset_password_complete/',
         CustomPasswordResetCompleteView.as_view(template_name='users/reset_password_complete.html'),
         name='reset_password_complete'),
]
