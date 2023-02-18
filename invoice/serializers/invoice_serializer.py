from rest_framework import serializers
from invoice.models import Invoice

class InvoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'
