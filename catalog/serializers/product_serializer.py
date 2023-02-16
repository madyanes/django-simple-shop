from rest_framework import serializers

from catalog.models import Product
# from catalog.serializers import ProductCategorySerializer

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
