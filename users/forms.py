from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm


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


class CustomPasswordChangeForm(PasswordChangeForm):
    class Meta:
        help_texts = {
            'new_password1': '',
            'new_password2': '',
        }

    def __init__(self, *args, **kwargs):
        super(CustomPasswordChangeForm, self).__init__(*args, **kwargs)
        self.fields['new_password1'].help_text = ''
        self.fields['new_password2'].help_text = ''
