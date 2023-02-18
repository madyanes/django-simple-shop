import uuid
from django.contrib.auth.models import User
from django.db import models
from shop.models import BaseModel
from catalog.models import Product

class Invoice(BaseModel):
    #status
    status_choices = [
        ('draft', 'DRAFT'),  # default
        ('ready', 'READY'),
        ('paid', 'PAID'),
        ('cancel', 'CANCEL'),
    ]

    #invoice type
    invoice_type_choices = [
        ('purchase', 'PURCHASE'),
        ('sale', 'SALE'),  # default
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ManyToManyField(Product, through='InvoiceItem')
    salesman = models.ForeignKey(to=User, on_delete=models.PROTECT)
    due_date = models.DateTimeField()
    invoice_type = models.CharField(max_length=10, choices=invoice_type_choices, default=invoice_type_choices[1][0])
    status = models.CharField(max_length=10, choices=status_choices, default=status_choices[0][0])

    def __str__(self) -> str:
        return f'{self.salesman.username} / {self.created_at}'
