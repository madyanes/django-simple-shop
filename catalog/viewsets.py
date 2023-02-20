from rest_framework import exceptions, mixins, viewsets, permissions, status
from rest_framework.response import Response

from catalog.exceptions import ShopDeleteProtectedException
from catalog.permissions import IsAdminOrReadOnly
from .models import Product, ProductCategory, ProductDetail, ProductUnit
from .serializers import ProductDetailSerializer, ProductSerializer, ProductCategorySerializer, ProductUnitSerializer

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

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if bool(instance.productdetail_set.count()):
            raise ShopDeleteProtectedException(f'This instance ({instance}) has a relation with other instance(s). Impossible to delete.')
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProductDetailViewSet(mixins.CreateModelMixin,
                           mixins.RetrieveModelMixin,
                           mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin,
                           mixins.ListModelMixin,
                           viewsets.GenericViewSet):
    queryset = ProductDetail.objects.all()
    serializer_class = ProductDetailSerializer
    permission_classes = [permissions.IsAdminUser]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if bool(instance.invoiceitem_set.count()):
            raise ShopDeleteProtectedException(f'This instance ({instance}) has a relation with other instance(s). Impossible to delete.')
        return super().destroy(request, *args, **kwargs)

class ProductCategoryViewSet(mixins.CreateModelMixin,
                           mixins.RetrieveModelMixin,
                           mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin,
                           mixins.ListModelMixin,
                           viewsets.GenericViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    permission_classes = [permissions.IsAdminUser]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if bool(instance.product_set.count()):
            raise ShopDeleteProtectedException(f'This instance ({instance}) has a relation with other instance(s). Impossible to delete.')
        return super().destroy(request, *args, **kwargs)

class ProductUnitViewSet(mixins.CreateModelMixin,
                           mixins.RetrieveModelMixin,
                           mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin,
                           mixins.ListModelMixin,
                           viewsets.GenericViewSet):
    queryset = ProductUnit.objects.all()
    serializer_class = ProductUnitSerializer
    permission_classes = [permissions.IsAdminUser]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if bool(instance.product_set.count()):
            raise ShopDeleteProtectedException(f'This instance ({instance}) has a relation with other instance(s). Impossible to delete.')
        return super().destroy(request, *args, **kwargs)
