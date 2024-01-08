from django.db import models
from category.models import Category
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from django.contrib.contenttypes.fields import GenericRelation
from media.models import Media


# Create your models here.
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=False, related_name='product')
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(blank=True)
    sell_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], null=False,
                                     blank=False)
    cost = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], null=False,
                               blank=False)
    quantity = models.IntegerField(validators=[MinValueValidator(0)], null=False, blank=False)
    is_unlimited = models.BooleanField(default=False)
    weight = models.DecimalField(max_digits=10, decimal_places=3, validators=[MinValueValidator(0)], null=False,
                                 blank=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    barcode = models.CharField(max_length=100, unique=True)
    is_visible = models.BooleanField(default=True)
    units_sold = models.IntegerField(default=0, validators=[MinValueValidator(0)], null=False, blank=False)
    media = GenericRelation(Media)

    def clean(self):
        self._validate_price_less_than_cost()
        self._validate_quantity_if_not_unlimited()

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def _validate_price_less_than_cost(self):
        if self.cost and self.sell_price:
            if self.cost >= self.sell_price:
                raise ValidationError('Cost must be less than the price.')

    def _validate_quantity_if_not_unlimited(self):
        if not self.is_unlimited and self.quantity is None:
            raise ValidationError('Quantity must be provided for limited product.')

    def __str__(self):
        return self.title
