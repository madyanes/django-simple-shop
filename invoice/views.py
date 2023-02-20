from django.shortcuts import render
from rest_framework import permissions, viewsets
from catalog.exceptions import ShopDeleteProtectedException
from invoice.models import Cart, CartItem, Invoice
from invoice.serializers import CartSerializer, CartItemSerializer, InvoiceSerializer

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = [permissions.IsAdminUser]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if bool(instance.invoiceitem_set.count()):
            raise ShopDeleteProtectedException(
                f'This instance ({instance}) has a relation with other instance(s). Impossible to delete.')
        return super().destroy(request, *args, **kwargs)


class InvoiceItemViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = [permissions.IsAdminUser]


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAdminUser]


class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAdminUser]
