from django.urls import path

from .views import ProductDeleteView, ProductListView

app_name = 'catalog'  # namespace
urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('delete/<uuid:pk>/', ProductDeleteView.as_view(), name='product_delete'),
]
