from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DeleteView, ListView, UpdateView

from .models import Product

class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'catalog/product_list.html'

class ProductDeleteView(DeleteView):
    model = Product
    context_object_name = 'product'
    template_name = 'catalog/product_delete.html'
    success_url = reverse_lazy('catalog:product_list')

class ProductUpdateView(UpdateView):
    model = Product
    context_object_name = 'product'
    template_name = 'catalog/product_update.html'
    success_url = reverse_lazy('catalog:product_list')

    fields = ['name']  # this attribute is mandatory
