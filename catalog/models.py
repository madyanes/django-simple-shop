import uuid

from django.db import models


class Product(models.Model):
    """
    The products entered to the system should not be deleted.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

class ProductDetail(models.Model):
    """
    The detail of the product.
    Because the purchased products sometime have different expiration date, or they purchased with different prices.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)  # set null to prevent deleting the product
    expiration_date = models.DateField()
    stock = models.IntegerField()
    note = models.TextField(blank=True)
    purchasing_price = models.DecimalField(max_digits=9, decimal_places=2)
    selling_price = models.DecimalField(max_digits=9, decimal_places=2)
    created_at = models.DateTimeField(verbose_name='Entry date', auto_now_add=True)  # the date when a good is registered to the system, can't be edited
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.product.name} ({self.id})'  # showing product name and ProductDetail ID on admin form
