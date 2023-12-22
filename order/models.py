from django.core.validators import MinValueValidator
from django.db import models
from product.models import Product
from users.models import CustomUser


# Create your models here.
class Order(models.Model):
    # todo create a common class for similar attributes between users table
    ORDER_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    telephone = models.CharField(max_length=15, null=False, blank=False)
    shipping_address = models.CharField(max_length=255, null=False, blank=False)
    shipping_city = models.CharField(max_length=50, null=False, blank=False)
    shipping_postal_code = models.CharField(max_length=12, blank=True, null=True)
    shipping_area = models.CharField(max_length=50, blank=True, null=True)
    order_status = models.CharField(max_length=50, default='pending')
    shipping_courier = models.CharField(max_length=50, null=False, blank=False)
    shipping_fee = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], null=False,
                                       blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_paid = models.BooleanField(default=False, null=False)

    def __str__(self):
        return f"Order {self.id} by {self.user.username if self.user else 'Guest'}"

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product.title}"

    def get_cost(self):
        return self.price * self.quantity
