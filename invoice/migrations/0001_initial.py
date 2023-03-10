# Generated by Django 4.1.6 on 2023-02-18 07:38

from decimal import Decimal
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('due_date', models.DateTimeField()),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalog.currency')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InvoiceItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('quantity', models.FloatField(validators=[django.core.validators.MinValueValidator(0.01)])),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))])),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='invoice.invoice')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalog.product')),
            ],
            options={
                'verbose_name': 'Invoice Item',
            },
        ),
        migrations.AddField(
            model_name='invoice',
            name='product',
            field=models.ManyToManyField(through='invoice.InvoiceItem', to='catalog.product'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='salesman',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
