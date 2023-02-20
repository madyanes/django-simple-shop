from rest_framework import serializers
from catalog.models import ProductDetail

class ProductDetailSerializer(serializers.HyperlinkedModelSerializer):
    # product = serializers.HyperlinkedIdentityField(view_name='product-detail')

    class Meta:
        model = ProductDetail
        fields = ['url', 'id', 'product', 'expiration_date', 'stock', 'note', 'purchasing_price', 'selling_price']
