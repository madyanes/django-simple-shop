from rest_framework import serializers
from invoice.models import CartItem


class CartItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'
