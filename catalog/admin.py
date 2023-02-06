from django.contrib import admin
from .models import Product, ProductCategory, ProductDetail, ProductUnit

class ProductDetailAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'id',
        'stock',
        'expiration_date',
        'selling_price',
        'created_at',
        'updated_at',
    )

class ProductUnitAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

admin.site.register(Product)
admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(ProductDetail, ProductDetailAdmin)
admin.site.register(ProductUnit, ProductUnitAdmin)
