import uuid
from django.contrib.auth.models import User
from django.db import models
from shop.models import BaseModel
from catalog.models import Currency, ProductDetail

class Invoice(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_detail = models.ManyToManyField(ProductDetail, through='InvoiceItem')
    salesman = models.ForeignKey(to=User, on_delete=models.PROTECT)
    currency = models.ForeignKey(to=Currency, on_delete=models.PROTECT)
    due_date = models.DateTimeField()

    def __str__(self) -> str:
        return f'{self.salesman.username} / {self.created_at}'
