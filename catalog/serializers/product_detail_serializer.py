from rest_framework import serializers
from catalog.models import ProductDetail

class ProductDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductDetail
        fields = ['id', 'product', 'expiration_date', 'stock', 'note', 'purchasing_price', 'selling_price', 'currency']
