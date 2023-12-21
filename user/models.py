from django.contrib.auth.models import AbstractUser
from django.db import models


# Custom User Model
class CustomUser(AbstractUser):
    # Additional fields from built in
    telephone = models.CharField(max_length=15, null=False, blank=False)
    date_of_birth = models.DateField(null=True, blank=True)
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    address = models.CharField(max_length=255, null=False, blank=False)
    area = models.CharField(max_length=255, blank=True)
    postal_code = models.CharField(max_length=12, blank=True)
    city = models.CharField(max_length=50, null=False, blank=False)
    email_verified = models.BooleanField(default=False, null=False, blank=False)
    registration_date = models.DateTimeField(auto_now_add=True)

    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        self.email = self.email.lower()  # Ensure the email is saved in lowercase
        super().save(*args, **kwargs)
