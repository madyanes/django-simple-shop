from django.db import models
from shop.models import BaseModel

class Currency(BaseModel):
    name = models.CharField(max_length=20, help_text='Indonesian Rupiah')
    code = models.CharField(max_length=3, help_text='IDR')

    def __str__(self):
        return self.code

    class Meta:
        verbose_name_plural = 'Currencies'
