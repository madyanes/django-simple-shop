from django.db import models

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
