from rest_framework import serializers
from catalog.models import ProductCategory

class ProductCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'
