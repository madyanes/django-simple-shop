from django.contrib import admin
from .models import Product, ProductDetail

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

admin.site.register(Product)
admin.site.register(ProductDetail, ProductDetailAdmin)
