from django.shortcuts import render
from rest_framework import mixins, permissions, viewsets
from catalog.exceptions import ShopDeleteProtectedException
from catalog import permissions as shop_permissions
from invoice.models import Cart, CartItem, Invoice, InvoiceItem
from invoice.serializers import CartSerializer, CartItemSerializer, InvoiceSerializer, InvoiceItemSerializer

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
    queryset = InvoiceItem.objects.all()
    serializer_class = InvoiceItemSerializer
    permission_classes = [permissions.IsAdminUser]


class CartViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated, shop_permissions.IsOwner]


class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated, shop_permissions.IsOwner]
