# Generated by Django 4.1.6 on 2023-02-20 07:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0002_remove_productdetail_currency_delete_currency'),
        ('invoice', '0003_invoice_invoice_type_invoice_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoice.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.product')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(through='invoice.CartItem', to='catalog.product'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
