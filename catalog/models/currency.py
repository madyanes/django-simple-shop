from django.db import models

class Currency(models.Model):
    name = models.CharField(max_length=20, help_text='Indonesian Rupiah')
    code = models.CharField(max_length=3, help_text='IDR')

    def __str__(self):
        return self.code

    class Meta:
        verbose_name_plural = 'Currencies'
