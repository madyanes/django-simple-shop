from decimal import Decimal
from django.core.validators import MinValueValidator
from django.db import models
from catalog.models import ProductDetail

class InvoiceItem(models.Model):
    invoice = models.ForeignKey(to='Invoice', on_delete=models.PROTECT)
    product_detail = models.ForeignKey(to=ProductDetail, on_delete=models.PROTECT)
    quantity = models.FloatField(validators=[MinValueValidator(float('0.01'))])
    price = models.DecimalField(max_digits=9, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])

    def __str__(self):
        return f'{self.pk}/{self.product_detail.product.name}'

    class Meta:
        verbose_name = 'Invoice Item'
