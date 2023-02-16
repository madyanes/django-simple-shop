from rest_framework import mixins, viewsets, permissions

from catalog.permissions import IsAdminOrReadOnly
from .models import Currency, Product, ProductDetail
from .serializers import CurrencySerializer, ProductDetailSerializer, ProductSerializer

class ProductViewSet(mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.ListModelMixin,
                     viewsets.GenericViewSet):
    """
    The shopkeeper is allowed to CREATE, RETRIEVE, UPDATE, DELETE, LIST the product.
    Others are allowed to RETRIEVE, LIST the product.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrReadOnly]

class ProductDetailViewSet(viewsets.ModelViewSet):
    queryset = ProductDetail.objects.all()
    serializer_class = ProductDetailSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrReadOnly]

class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrReadOnly]
