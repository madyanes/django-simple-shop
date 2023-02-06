import uuid
from decimal import Decimal

from django.core.validators import MinValueValidator
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

    # model relations
    category = models.ForeignKey(to='ProductCategory', on_delete=models.PROTECT, null=True)
    unit = models.ForeignKey(to='ProductUnit', on_delete=models.PROTECT, null=True)

    def get_stock(self) -> int:
        """
        Get a product stock.
        """
        all_products = self.productdetail_set.all()  # don't forget, a product can have multiple product details
        return sum([product.stock for product in all_products])

    def __str__(self) -> str:
        return self.name

class ProductDetail(models.Model):
    """
    The detail of the product.
    Because the purchased products sometime have different expiration date, or they purchased with different prices.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product, on_delete=models.PROTECT, null=True)  # the referenced object (Product) isn't allowed to be deleted
    expiration_date = models.DateField()
    stock = models.IntegerField(validators=[MinValueValidator(1)])
    note = models.TextField(blank=True)
    purchasing_price = models.DecimalField(max_digits=9, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    selling_price = models.DecimalField(max_digits=9, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    created_at = models.DateTimeField(verbose_name='Entry date', auto_now_add=True)  # the date when a good is registered to the system, can't be edited
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        product_name = self.product
        if product_name is None: product_name = '❓'
        return f'{product_name} ({self.id})'  # showing product name and ProductDetail ID on admin form

class ProductCategory(models.Model):
    name = models.CharField(verbose_name='category', max_length=50, unique=True, help_text='ex: snack')
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Product Category'
        verbose_name_plural = 'Product Categories'

class ProductUnit(models.Model):
    name = models.CharField(verbose_name='Unit', max_length=50, unique=True, help_text='ex: pieces')
    code = models.CharField(max_length=10, help_text='ex: pcs')
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Product Unit'
