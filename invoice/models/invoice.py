import uuid
from django.contrib.auth.models import User
from django.db import models
from catalog.models import Currency, ProductDetail

class Invoice(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_detail = models.ManyToManyField(ProductDetail, through='InvoiceItem')
    salesman = models.ForeignKey(to=User, on_delete=models.PROTECT)
    currency = models.ForeignKey(to=Currency, on_delete=models.PROTECT)
    due_date = models.DateTimeField()
    created_at = models.DateTimeField(verbose_name='Invoice Date', auto_now_add=True)  # the date when a good is registered to the system, can't be edited
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.salesman.username} / {self.created_at}'
