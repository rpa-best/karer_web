# Generated by Django 4.1.1 on 2023-02-28 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invite', '0002_organization_remove_invite_organization_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='invite',
            options={'ordering': ['position'], 'verbose_name': 'Заявка', 'verbose_name_plural': 'Заявкы'},
        ),
        migrations.AddField(
            model_name='invite',
            name='position',
            field=models.PositiveIntegerField(null=True, verbose_name='Позиция'),
        ),
    ]
