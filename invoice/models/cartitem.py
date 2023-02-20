from django.db import models
from shop.models import BaseModel
from catalog.models import Product
from .cart import Cart


class CartItem(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
