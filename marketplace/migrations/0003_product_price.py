# Generated by Django 4.1 on 2023-04-06 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0002_product_karer'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.FloatField(null=True, verbose_name='Цена'),
        ),
    ]