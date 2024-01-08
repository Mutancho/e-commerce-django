from django.contrib import admin
from django.contrib import admin
from .models import Discount
from django.utils.translation import gettext_lazy as _


# Register your models here.
@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('code', 'valid_from', 'valid_to', 'discount_type', 'discount_value',
                    'discount_apply', 'is_currently_active')
    list_filter = ('active', 'discount_type', 'discount_apply', 'valid_from', 'valid_to')
    search_fields = ('code',)
    actions = ['make_active', 'make_inactive']

    # Custom admin actions
    @admin.action(description=_('Mark selected discounts as active'))
    def make_active(self, request, queryset):
        queryset.update(active=True)

    @admin.action(description=_('Mark selected discounts as inactive'))
    def make_inactive(self, request, queryset):
        queryset.update(active=False)

    # Override get_form to dynamically hide/show fields based on discount_apply choice
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if obj:  # obj is not None, so this is an edit
            if obj.discount_apply == 'all':
                form.base_fields['category'].disabled = True
                form.base_fields['product'].disabled = True
            elif obj.discount_apply == 'category':
                form.base_fields['product'].disabled = True
            elif obj.discount_apply == 'product':
                form.base_fields['category'].disabled = True
        return form

    # Override get_readonly_fields to make certain fields read-only after creation
    def get_readonly_fields(self, request, obj=None):
        if obj:  # Editing an existing object
            return 'code', 'discount_type', 'discount_apply'  # These fields should not be changed
        return ()  # No fields are read-only when creating a new object

    def currently_active(self, obj):
        return obj.is_currently_active()

    currently_active.boolean = True  # This will display it as a status icon
    currently_active.short_description = _("Currently Active")  # For the column header
