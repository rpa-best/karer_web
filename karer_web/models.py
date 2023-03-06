from django.db import models


class Karer(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Карьер'
        verbose_name_plural = "Карьеры"


class Car(models.Model):
    number = models.CharField(max_length=100, verbose_name='Номер')
    model = models.CharField(max_length=100, verbose_name='Модель')
    vin_number = models.CharField(max_length=100, verbose_name='Вин')

    class Meta:
        verbose_name = "Машина"
        verbose_name_plural = "Машины"

    def __str__(self) -> str:
        return self.number


class Driver(models.Model):
    name = models.CharField(max_length=255, verbose_name='ФИО')
    phone = models.CharField(max_length=255, verbose_name='Номер телефона')

    class Meta:
        verbose_name = "Водитель"
        verbose_name_plural = "Водители"

    def __str__(self) -> str:
        return self.name


class Organization(models.Model):
    name = models.CharField("Название", max_length=255)
    inn = models.CharField("ИНН", max_length=20)
    bik = models.CharField("ВИК", max_length=255)
    address = models.CharField("Адрес", max_length=255)
    phone = models.CharField("Телефон", max_length=20)

    class Meta:
        verbose_name = "Организация"
        verbose_name_plural = "Организации"

    def __str__(self) -> str:
        return self.name


class Client(models.Model):
    name = models.CharField("ФИО", max_length=255)
    passport = models.CharField("Паспорт", max_length=20)
    phone = models.CharField("Телефон", max_length=20)

    class Meta:
        verbose_name = "Физическое лицо"
        verbose_name_plural = "Физическое лицо"

    def __str__(self) -> str:
        return self.name
