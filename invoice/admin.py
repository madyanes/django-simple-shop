from django.contrib import admin

from catalog.models import ProductDetail
from .models import Invoice, InvoiceItem

class InvoiceItemInline(admin.TabularInline):
    model = InvoiceItem
    extra = 3

class InvoiceAdmin(admin.ModelAdmin):
    inlines = [InvoiceItemInline]

    # was trying to filter choice field for Invoice Item to only show the not-binded-yet products with the invoice items
    # but still failed
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        print(f'isi form============={form.base_fields}')
        # form.base_fields['product'].queryset = InvoiceItem.objects.filter(product__isnull=True)
        return form

class InvoiceItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity', 'price', 'invoice']

    # filter products to show only unbinded products with invoice items
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        print(f'isi form============={form.base_fields}')
        form.base_fields['product'].queryset = ProductDetail.objects.filter(invoiceitem__isnull=True)
        return form

admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(InvoiceItem, InvoiceItemAdmin)
