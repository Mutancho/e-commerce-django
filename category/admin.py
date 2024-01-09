from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from media.models import Media
from .models import Category


# Register your models here.
class MediaInline(GenericTabularInline):
    model = Media
    fields = ('file', 'alt_text', 'media_type', 'is_main')
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')  # Fields to display in the admin list view
    search_fields = ('name',)  # Fields to be searched in the admin
    inlines = [MediaInline]
