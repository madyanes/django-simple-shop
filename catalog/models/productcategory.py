from django.db import models
from shop.models import BaseModel

class ProductCategory(BaseModel):
    name = models.CharField(verbose_name='category', max_length=50, unique=True, help_text='ex: snack')
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Product Category'
        verbose_name_plural = 'Product Categories'
