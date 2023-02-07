from django.contrib import admin
from .models import Currency, Product, ProductCategory, ProductDetail, ProductUnit

class CurrencyAdmin(admin.ModelAdmin):
    list_display = ['code', 'name']

class ProductDetailAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'id',
        'stock',
        'expiration_date',
        'selling_price',
        'currency',
        'created_at',
        'updated_at',
    )

class ProductUnitAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

admin.site.register(Currency, CurrencyAdmin)
admin.site.register(Product)
admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(ProductDetail, ProductDetailAdmin)
admin.site.register(ProductUnit, ProductUnitAdmin)
