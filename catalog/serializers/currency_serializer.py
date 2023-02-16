from rest_framework import serializers
from catalog.models import Currency

class CurrencySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Currency
        fields = '__all__'
