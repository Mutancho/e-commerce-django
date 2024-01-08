from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views, login
from django.urls import reverse_lazy, reverse
from .forms import CustomUserCreationForm
from .tasks import send_welcome_email
from django.contrib.auth.views import (PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView,
                                       PasswordResetCompleteView)


# Register view


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            send_welcome_email(user.email)
            return redirect(reverse('users:login'))
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})


# Customizing the LoginView
class CustomLoginView(auth_views.LoginView):
    template_name = 'users/login.html'  # Specify your custom template

    def get_success_url(self):
        return reverse('home')


# Customizing the LogoutView
class CustomLogoutView(auth_views.LogoutView):
    next_page = reverse_lazy('home')

# Customizing the PasswordChangeView
class CustomPasswordChangeView(auth_views.PasswordChangeView):
    template_name = 'users/password_change_form.html'  # Specify your custom template
    success_url = reverse_lazy('password_change_done')  # URL to redirect after a successful password change


# View for Password Change Done
class PasswordChangeDoneView(auth_views.PasswordChangeDoneView):
    template_name = 'users/password_change_done.html'


class CustomPasswordResetView(PasswordResetView):
    """View used for submitting the email address for password reset."""
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    success_url = reverse_lazy('users:password_reset_sent')


class CustomPasswordResetDoneView(PasswordResetDoneView):
    """View shown after the user submits their email for password reset."""
    template_name = 'users/password_reset_sent.html'


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    """View used for the actual password reset."""
    template_name = 'users/password_reset_confirm.html'
    success_url = reverse_lazy('users:password_reset_complete')


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    """View used to display password successfully reset."""
    template_name = 'users/password_reset_complete.html'

# todo add another view for Password reset unsuccessful eg when link is already userd.
