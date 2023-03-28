# Generated by Django 4.1 on 2023-03-28 07:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientInvite',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='Наименование груза')),
                ('weight', models.FloatField(verbose_name='Потребность (кг)')),
                ('status', models.CharField(choices=[('created', 'Создано'), ('accepted', 'Принята'), ('waiting_pay', 'Ожидает оплаты'), ('payed', 'Оплачено'), ('finished', 'Успешно'), ('canceled', 'Отклонена')], default='created', max_length=255, verbose_name='Статус')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('finish_at', models.DateTimeField(blank=True, null=True, verbose_name='Дата закрытия')),
                ('position', models.PositiveIntegerField(null=True, verbose_name='Позиция')),
            ],
            options={
                'verbose_name': 'Заявка физ. лицо',
                'verbose_name_plural': 'Заявкы физ. лицо',
                'ordering': ['position'],
            },
        ),
        migrations.CreateModel(
            name='ClientOrder',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('desc', models.TextField(verbose_name='Описание')),
                ('status', models.CharField(choices=[('created', 'Создано'), ('accepted', 'Принята'), ('waiting_pay', 'Ожидает оплаты'), ('payed', 'Оплачено'), ('finished', 'Успешно'), ('canceled', 'Отклонена')], default='created', max_length=255, verbose_name='Статус')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('finish_at', models.DateTimeField(blank=True, null=True, verbose_name='Дата закрытия')),
            ],
            options={
                'verbose_name': 'Заказ физ. лицо',
                'verbose_name_plural': 'Заказы физ. лицо',
            },
        ),
        migrations.CreateModel(
            name='OrgInvite',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='Наименование груза')),
                ('weight', models.FloatField(verbose_name='Потребность (кг)')),
                ('status', models.CharField(choices=[('created', 'Создано'), ('accepted', 'Принята'), ('waiting_pay', 'Ожидает оплаты'), ('payed', 'Оплачено'), ('finished', 'Успешно'), ('canceled', 'Отклонена')], default='created', max_length=255, verbose_name='Статус')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('finish_at', models.DateTimeField(blank=True, null=True, verbose_name='Дата закрытия')),
                ('position', models.PositiveIntegerField(null=True, verbose_name='Позиция')),
            ],
            options={
                'verbose_name': 'Заявка юр. лицо',
                'verbose_name_plural': 'Заявкы юр. лицо',
                'ordering': ['position'],
            },
        ),
        migrations.CreateModel(
            name='OrgOrder',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('desc', models.TextField(verbose_name='Описание')),
                ('status', models.CharField(choices=[('created', 'Создано'), ('accepted', 'Принята'), ('waiting_pay', 'Ожидает оплаты'), ('payed', 'Оплачено'), ('finished', 'Успешно'), ('canceled', 'Отклонена')], default='created', max_length=255, verbose_name='Статус')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('finish_at', models.DateTimeField(blank=True, null=True, verbose_name='Дата закрытия')),
            ],
            options={
                'verbose_name': 'Заказ юр. лицо',
                'verbose_name_plural': 'Заказы юр. лицо',
            },
        ),
    ]
