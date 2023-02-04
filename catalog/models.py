import uuid

from django.db import models


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    expired = models.DateField()
    stock = models.IntegerField()

    def __str__(self) -> str:
        return self.name
