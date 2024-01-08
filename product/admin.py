from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from media.models import Media
from .models import Product


# Register your models here.
class MediaInline(GenericTabularInline):
    model = Media
    fields = ('file', 'alt_text', 'media_type', 'is_main')
    extra = 1  # Number of extra empty forms for new media items


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'sell_price', 'quantity', 'is_unlimited', 'weight', 'cost', 'uploaded_at')
    search_fields = ('title', 'barcode')
    list_filter = ('category', 'is_visible')
    inlines = [MediaInline]  # Add this line to include MediaInline
