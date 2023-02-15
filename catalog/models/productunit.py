from django.db import models

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
