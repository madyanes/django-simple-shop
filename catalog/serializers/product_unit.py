from rest_framework import serializers
from catalog.models import ProductUnit

class ProductUnitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductUnit
        fields = '__all__'
