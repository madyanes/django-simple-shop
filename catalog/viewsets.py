from rest_framework import mixins, viewsets, permissions, status
from rest_framework.response import Response

from catalog.permissions import IsAdminOrReadOnly
from .models import Currency, Product, ProductCategory, ProductDetail, ProductUnit
from .serializers import CurrencySerializer, ProductDetailSerializer, ProductSerializer, ProductCategorySerializer, ProductUnitSerializer

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
    permission_classes = [IsAdminOrReadOnly]

class ProductDetailViewSet(mixins.CreateModelMixin,
                           mixins.RetrieveModelMixin,
                           mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin,
                           mixins.ListModelMixin,
                           viewsets.GenericViewSet):
    queryset = ProductDetail.objects.all()
    serializer_class = ProductDetailSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrReadOnly]

class ProductCategoryViewSet(mixins.CreateModelMixin,
                           mixins.RetrieveModelMixin,
                           mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin,
                           mixins.ListModelMixin,
                           viewsets.GenericViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrReadOnly]

class ProductUnitViewSet(mixins.CreateModelMixin,
                           mixins.RetrieveModelMixin,
                           mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin,
                           mixins.ListModelMixin,
                           viewsets.GenericViewSet):
    queryset = ProductUnit.objects.all()
    serializer_class = ProductUnitSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrReadOnly]

class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrReadOnly]
