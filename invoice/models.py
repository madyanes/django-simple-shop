import uuid
from decimal import Decimal

from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models

from catalog.models import Currency, ProductDetail

class Invoice(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    salesman = models.ForeignKey(to=User, on_delete=models.PROTECT)
    currency = models.ForeignKey(to=Currency, on_delete=models.PROTECT)
    due_date = models.DateTimeField()
    created_at = models.DateTimeField(verbose_name='Invoice Date', auto_now_add=True)  # the date when a good is registered to the system, can't be edited
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.salesman.username} / {self.created_at}'

class InvoiceItem(models.Model):
    invoice = models.ForeignKey(to=Invoice, on_delete=models.PROTECT)
    product = models.OneToOneField(to=ProductDetail, on_delete=models.PROTECT, primary_key=True)
    quantity = models.FloatField(validators=[MinValueValidator(float('0.01'))])
    price = models.DecimalField(max_digits=9, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])

    def __str__(self):
        return f'{self.pk}/{self.product.product.name}'

    class Meta:
        verbose_name = 'Invoice Item'
