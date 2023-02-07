from django.contrib import admin

from .models import Invoice, InvoiceItem

class InvoiceItemInline(admin.TabularInline):
    model = InvoiceItem
    extra = 3

class InvoiceAdmin(admin.ModelAdmin):
    inlines = [InvoiceItemInline]

admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(InvoiceItem)
