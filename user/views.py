from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy


# Create your views here.
# Customizing the LoginView (if needed)
class CustomLoginView(auth_views.LoginView):
    template_name = 'users/login.html'  # Specify your custom template
    # Add any other customization here


# Customizing the LogoutView (if needed)
class CustomLogoutView(auth_views.LogoutView):
    # If you want to redirect to a specific page after logout
    next_page = 'name_of_homepage_view'


# Customizing the PasswordChangeView
class CustomPasswordChangeView(auth_views.PasswordChangeView):
    template_name = 'users/password_change_form.html'  # Specify your custom template
    success_url = reverse_lazy('password_change_done')  # URL to redirect after a successful password change


# View for Password Change Done (after successfully changing the password)
class PasswordChangeDoneView(auth_views.PasswordChangeDoneView):
    template_name = 'users/password_change_done.html'  # Specify your custom template
