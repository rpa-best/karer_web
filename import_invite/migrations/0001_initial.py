# Generated by Django 4.1.1 on 2023-03-14 06:15

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('karer_web', '0004_karer_slug_alter_karer_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientImport',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('desc', models.TextField(verbose_name='Описание')),
                ('status', models.CharField(choices=[('created', 'Создано'), ('accepted', 'Принята'), ('waiting_pay', 'Ожидает оплаты'), ('payed', 'Оплачено'), ('finished', 'Успешно'), ('canceled', 'Отклонена')], default='created', max_length=255, verbose_name='Статус')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('finish_at', models.DateTimeField(blank=True, null=True, verbose_name='Дата закрытия')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='karer_web.client', verbose_name='Физ. лицо')),
                ('karer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='karer_web.karer', verbose_name='Объект')),
            ],
            options={
                'verbose_name': 'Импорт физ. лицо',
                'verbose_name_plural': 'Импорты физ. лицо',
            },
        ),
        migrations.CreateModel(
            name='OrgImport',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('desc', models.TextField(verbose_name='Описание')),
                ('status', models.CharField(choices=[('created', 'Создано'), ('accepted', 'Принята'), ('waiting_pay', 'Ожидает оплаты'), ('payed', 'Оплачено'), ('finished', 'Успешно'), ('canceled', 'Отклонена')], default='created', max_length=255, verbose_name='Статус')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('finish_at', models.DateTimeField(blank=True, null=True, verbose_name='Дата закрытия')),
                ('karer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='karer_web.karer', verbose_name='Объект')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='karer_web.organization', verbose_name='Организация')),
            ],
            options={
                'verbose_name': 'Импорт юр. лицо',
                'verbose_name_plural': 'Импорты юр. лицо',
            },
        ),
        migrations.CreateModel(
            name='OrgImportInvite',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='Наименование груза')),
                ('weight', models.FloatField(verbose_name='Потребность (кг)')),
                ('status', models.CharField(choices=[('created', 'Создано'), ('accepted', 'Принята'), ('waiting_pay', 'Ожидает оплаты'), ('payed', 'Оплачено'), ('finished', 'Успешно'), ('canceled', 'Отклонена')], default='created', max_length=255, verbose_name='Статус')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('finish_at', models.DateTimeField(blank=True, null=True, verbose_name='Дата закрытия')),
                ('position', models.PositiveIntegerField(null=True, verbose_name='Позиция')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='karer_web.car', verbose_name='Номер машины')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='karer_web.driver', verbose_name='Водитель')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='import_invite.orgimport', verbose_name='Импорт')),
            ],
            options={
                'verbose_name': 'Заявка юр. лицо',
                'verbose_name_plural': 'Заявкы юр. лицо',
                'ordering': ['position'],
            },
        ),
        migrations.CreateModel(
            name='ClientImportInvite',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='Наименование груза')),
                ('weight', models.FloatField(verbose_name='Потребность (кг)')),
                ('status', models.CharField(choices=[('created', 'Создано'), ('accepted', 'Принята'), ('waiting_pay', 'Ожидает оплаты'), ('payed', 'Оплачено'), ('finished', 'Успешно'), ('canceled', 'Отклонена')], default='created', max_length=255, verbose_name='Статус')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('finish_at', models.DateTimeField(blank=True, null=True, verbose_name='Дата закрытия')),
                ('position', models.PositiveIntegerField(null=True, verbose_name='Позиция')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='karer_web.car', verbose_name='Номер машины')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='karer_web.driver', verbose_name='Водитель')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='import_invite.clientimport', verbose_name='Импорт')),
            ],
            options={
                'verbose_name': 'Заявка физ. лицо',
                'verbose_name_plural': 'Заявкы физ. лицо',
                'ordering': ['position'],
            },
        ),
    ]
