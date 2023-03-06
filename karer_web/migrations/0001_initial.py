# Generated by Django 4.1 on 2023-03-06 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Car",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("number", models.CharField(max_length=100, verbose_name="Номер")),
                ("model", models.CharField(max_length=100, verbose_name="Модель")),
                ("vin_number", models.CharField(max_length=100, verbose_name="Вин")),
            ],
            options={"verbose_name": "Машина", "verbose_name_plural": "Машины",},
        ),
        migrations.CreateModel(
            name="Client",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="ФИО")),
                ("passport", models.CharField(max_length=20, verbose_name="Паспорт")),
                ("phone", models.CharField(max_length=20, verbose_name="Телефон")),
            ],
            options={
                "verbose_name": "Физическое лицо",
                "verbose_name_plural": "Физическое лицо",
            },
        ),
        migrations.CreateModel(
            name="Driver",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="ФИО")),
                (
                    "phone",
                    models.CharField(max_length=255, verbose_name="Номер телефона"),
                ),
            ],
            options={"verbose_name": "Водитель", "verbose_name_plural": "Водители",},
        ),
        migrations.CreateModel(
            name="Karer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="Карьер")),
            ],
            options={"verbose_name": "Карьер", "verbose_name_plural": "Карьеры",},
        ),
        migrations.CreateModel(
            name="Organization",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="Название")),
                ("inn", models.CharField(max_length=20, verbose_name="ИНН")),
                ("bik", models.CharField(max_length=255, verbose_name="ВИК")),
                ("address", models.CharField(max_length=255, verbose_name="Адрес")),
                ("phone", models.CharField(max_length=20, verbose_name="Телефон")),
            ],
            options={
                "verbose_name": "Организация",
                "verbose_name_plural": "Организации",
            },
        ),
    ]