# Generated by Django 4.1.6 on 2023-02-04 01:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('expired', models.DateField()),
                ('stock', models.IntegerField()),
            ],
        ),
    ]
