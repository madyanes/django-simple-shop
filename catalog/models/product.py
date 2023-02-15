import uuid
from django.db import models
from shop.models import BaseModel

class Product(BaseModel):
    """
    The products entered to the system should not be deleted.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

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
