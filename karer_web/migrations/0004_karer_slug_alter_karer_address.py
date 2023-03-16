# Generated by Django 4.1.1 on 2023-03-14 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karer_web', '0003_karer_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='karer',
            name='slug',
            field=models.SlugField(default='', max_length=255, verbose_name='Уникальная название'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='karer',
            name='address',
            field=models.TextField(blank=True, null=True, verbose_name='Адрес'),
        ),
    ]