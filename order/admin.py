from django.contrib import admin
from django.contrib import admin
from .models import Order, OrderItem
from django.utils.translation import gettext_lazy as _


# Register your models here.
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    fields = ('product', 'price', 'quantity', 'subtotal')  # Add 'subtotal' here
    readonly_fields = ('subtotal',)  # Make 'subtotal' read-only

    def subtotal(self, instance):
        return instance.get_subtotal() or 0  # Ensure it returns 0 if None

    subtotal.short_description = _("Subtotal")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email',
                    'order_status', 'created_at', 'is_paid', 'display_total_price')
    readonly_fields = ('display_total_price',)
    list_filter = ('order_status', 'is_paid', 'created_at', 'discount')
    search_fields = ('first_name', 'last_name', 'email', 'shipping_city', 'code')
    raw_id_fields = ('user', 'discount')  # Include discount here for easy lookup
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    inlines = [OrderItemInline]  # This line adds the in-line editing feature for OrderItem

    class Media:
        js = ('js/order_admin.js',)

    def display_total_price(self, obj):
        return obj.get_total_cost()

    display_total_price.short_description = _("Total Price")


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'price', 'quantity')
    search_fields = ('order__id', 'product__title')
    raw_id_fields = ('order', 'product')
