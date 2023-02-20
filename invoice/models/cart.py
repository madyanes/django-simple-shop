from django.contrib.auth.models import User
from django.db import models
from shop.models import BaseModel
from catalog.models import Product


class Cart(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='CartItem')

    def __str__(self):
        return f'Cart for {self.user.username}'
