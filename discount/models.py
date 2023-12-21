import datetime
from django.db import models


# Create your models here.
class Discount(models.Model):
    DISCOUNT_TYPE_CHOICES = [
        ('percentage', 'Percentage'),
        ('fixed', 'Fixed Amount')
    ]

    DISCOUNT_APPLY_CHOICES = [
        ('all', 'All Products'),
        ('category', 'By Category'),
        ('product', 'Specific Product')
    ]

    code = models.CharField(max_length=50, unique=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount_type = models.CharField(max_length=10, choices=DISCOUNT_TYPE_CHOICES)
    discount_value = models.DecimalField(max_digits=10, decimal_places=2)
    discount_apply = models.CharField(max_length=10, choices=DISCOUNT_APPLY_CHOICES)
    active = models.BooleanField(default=True)
    category = models.ForeignKey('category.Category', null=True, blank=True, on_delete=models.SET_NULL)
    product = models.ForeignKey('product.Product', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.code

    def is_currently_active(self):
        return self.active and self.valid_from <= datetime.datetime.now() <= self.valid_to

    def apply_discount(self, amount):
        if self.discount_type == 'percentage':
            return amount * (1 - (self.discount_value / 100))
        elif self.discount_type == 'fixed':
            return max(amount - self.discount_value, 0)
