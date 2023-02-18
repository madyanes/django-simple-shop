import uuid
from decimal import Decimal
from django.core.validators import MinValueValidator
from django.db import models
from shop.models import BaseModel

class ProductDetail(BaseModel):
    """
    The detail of the product.
    Because the purchased products sometime have different expiration date, or they purchased with different prices.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey('Product', on_delete=models.PROTECT, null=True)  # the referenced object (Product) isn't allowed to be deleted
    expiration_date = models.DateField()
    stock = models.IntegerField(validators=[MinValueValidator(1)])
    note = models.TextField(blank=True)
    purchasing_price = models.DecimalField(max_digits=9, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    selling_price = models.DecimalField(max_digits=9, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])

    def __str__(self) -> str:
        product_name = self.product
        if product_name is None: product_name = '❓'
        return f'{product_name} ({self.id})'  # showing product name and ProductDetail ID on admin form
