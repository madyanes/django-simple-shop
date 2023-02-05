from django.urls import path

from .views import ProductCreateView, ProductDeleteView, ProductListView, ProductUpdateView

app_name = 'catalog'  # namespace
urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('delete/<uuid:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('update/<uuid:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
]
