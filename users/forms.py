from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    # todo possibly remove password to common optionality so users can create passwords they like
    class Meta(UserCreationForm.Meta):
        model = get_user_model()  # Use your CustomUser model here
        fields = ('email', 'password1', 'password2', 'telephone',
                  'date_of_birth', 'gender',
                  'address', 'area', 'postal_code', 'city',)

    def save(self, commit=True):
        user = super().save(commit=False)
        # Any additional processing or field setting can be done here
        if commit:
            user.save()
        return user
