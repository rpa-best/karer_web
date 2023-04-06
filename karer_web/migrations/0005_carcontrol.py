# Generated by Django 4.1 on 2023-04-06 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('karer_web', '0004_alter_organization_karer'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarControl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255, verbose_name='Тип собитие')),
                ('mode', models.CharField(max_length=255, verbose_name='Собитие')),
                ('date', models.DateTimeField(verbose_name='Дата и время')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='karer_web.car', to_field='number', verbose_name='Машина')),
            ],
            options={
                'verbose_name': 'Контроль машин',
                'verbose_name_plural': 'Контроль машин',
            },
        ),
    ]
