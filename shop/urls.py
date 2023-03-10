"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from rest_framework import routers

from catalog.viewsets import ProductViewSet, ProductDetailViewSet, ProductCategoryViewSet, ProductUnitViewSet
from invoice.views import CartViewSet, CartItemViewSet, InvoiceViewSet, InvoiceItemViewSet
from .views import UserViewSet

# Django Admin Interface (custom)
admin.site.site_header = 'Simple Shop Administration'
admin.site.index_title = 'Site Administration'
admin.site.site_title = 'Simple Shop Administration'

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'products', ProductViewSet, basename='product')
router.register(r'product-categories', ProductCategoryViewSet, basename='productcategory')
router.register(r'product-units', ProductUnitViewSet, basename='productunit')
router.register(r'product-details', ProductDetailViewSet, basename='productdetail')
router.register(r'invoice', InvoiceViewSet, basename='invoice')
router.register(r'invoice-items', InvoiceItemViewSet, basename='invoice-item')
router.register(r'cart', CartViewSet, basename='cart')
router.register(r'cart-item', CartItemViewSet, basename='cartitem')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
]
