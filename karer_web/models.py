from django.core.validators import MaxLengthValidator
from django.db import models
from .validators import INNCheckValidator


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
    name = models.CharField("Название", max_length=255, blank=True)
    inn = models.CharField("ИНН", max_length=20, unique=True,
                           validators=[
                               MaxLengthValidator(10, 'Неправильный ИНН'),
                           ])
    bik = models.CharField("ВИК", max_length=255, blank=True)
    address = models.CharField("Адрес", max_length=255, blank=True)
    phone = models.CharField("Телефон", max_length=20, blank=True)
    ogrn = models.CharField("ОГРН", max_length=20, blank=True)
    kpp = models.CharField("КПП", max_length=20, blank=True)

    class Meta:
        verbose_name = "Организация"
        verbose_name_plural = "Организации"

    def __str__(self) -> str:
        return self.name

    def clean(self):
        validator = INNCheckValidator()
        org = validator(self.inn)
        self.address = org['a']
        self.name = org['c']
        self.ogrn = org['o']
        self.kpp = org['p']
        return super(Organization, self).clean()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.full_clean()
        return super(Organization, self).save(force_insert, force_update, using, update_fields)


class Client(models.Model):
    name = models.CharField("ФИО", max_length=255)
    passport = models.CharField("Паспорт", max_length=20)
    phone = models.CharField("Телефон", max_length=20)

    class Meta:
        verbose_name = "Физическое лицо"
        verbose_name_plural = "Физическое лицо"

    def __str__(self) -> str:
        return self.name
