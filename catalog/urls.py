from django.urls import include, path

from rest_framework import routers

from .views import ProductCreateView, ProductDeleteView, ProductListView, ProductUpdateView
from .viewsets import ProductViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)

app_name = 'catalog'  # namespace
urlpatterns = [
    path('api/', include(router.urls)),
    path('', ProductListView.as_view(), name='product_list'),
    path('delete/<uuid:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('update/<uuid:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
]
