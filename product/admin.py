from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from django.core.exceptions import ValidationError
from media.models import Media
from .models import Product


# Register your models here.
# todo capture error when there is no image uploaded to a project
# todo fix unlimited quantity currently it still requires some quantity
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

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        main_image_count = 0
        has_image = False

        for instance in instances:
            if isinstance(instance, Media) and instance.media_type == 'image':
                has_image = True
                if instance.is_main:
                    main_image_count += 1

            instance.save()

        # Check for at least one image
        if not has_image:
            raise ValidationError('At least one image is required.')

        # Check for exactly one main image
        if main_image_count != 1:
            raise ValidationError('Exactly one image must be set as the main image.')

        formset.save_m2m()
