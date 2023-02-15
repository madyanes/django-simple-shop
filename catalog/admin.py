from django.contrib import admin
from .models import Currency, Product, ProductCategory, ProductDetail, ProductUnit

@admin.action(description='Change to active')
def make_active(modeladmin, request, queryset):
    queryset.update(is_active=True)

@admin.action(description='Change to inactive')
def make_inactive(modeladmin, request, queryset):
    queryset.update(is_active=False)

class CurrencyAdmin(admin.ModelAdmin):
    list_display = ['code', 'name']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'unit', 'is_active']
    list_filter = ['is_active', 'category', 'unit']
    actions = [make_active, make_inactive]

class ProductDetailAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'id',
        'stock',
        'expiration_date',
        'selling_price',
        'currency',
    )

class ProductUnitAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

admin.site.register(Currency, CurrencyAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(ProductDetail, ProductDetailAdmin)
admin.site.register(ProductUnit, ProductUnitAdmin)
