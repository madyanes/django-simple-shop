from rest_framework import serializers

from catalog.models import Product

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    # product_detail = 'ProductDetailSerializer()'
    class Meta:
        model = Product
        fields = ['url', 'id', 'name', 'is_active', 'created_at', 'updated_at']
