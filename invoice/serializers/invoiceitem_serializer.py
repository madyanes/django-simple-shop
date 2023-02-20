from rest_framework import serializers
from invoice.models import InvoiceItem

class InvoiceItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InvoiceItem
        fields = '__all__'
