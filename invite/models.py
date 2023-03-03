from django.db import models


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

    class Meta:
        verbose_name = "Организация"
        verbose_name_plural = "Организации"

    def __str__(self) -> str:
        return self.name


class Order(models.Model):
    STATUS = (
        ('created', 'Создано'),
        ('accepted', 'Принята'),
        ('waiting_pay', 'Ожидает оплаты'),
        ('payed', 'Оплачено'),
        ('finished', 'Успешно'),
        ('canceled', 'Отклонена')
    )
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name='Наименование груза')
    organization = models.ForeignKey(Organization, models.PROTECT, verbose_name='Организация')
    status = models.CharField(max_length=255, choices=STATUS, default='created', verbose_name='Статус')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    finish_at = models.DateTimeField(blank=True, null=True, verbose_name='Дата закрытия')

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self) -> str:
        return self.name


class Invite(models.Model):
    STATUS = (
        ('created', 'Создано'),
        ('accepted', 'Принята'),
        ('waiting_pay', 'Ожидает оплаты'),
        ('payed', 'Оплачено'),
        ('finished', 'Успешно'),
        ('canceled', 'Отклонена')
    )
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name='Наименование груза')
    car = models.ForeignKey(Car, models.PROTECT, verbose_name='Номер машины')
    driver = models.ForeignKey(Driver, models.PROTECT, verbose_name='Водитель')
    order = models.ForeignKey(Order, models.CASCADE, verbose_name='Заказ')
    weight = models.FloatField(verbose_name='Потребность (кг)')
    status = models.CharField(max_length=255, choices=STATUS, default='created', verbose_name='Статус')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    finish_at = models.DateTimeField(blank=True, null=True, verbose_name='Дата закрытия')
    position = models.PositiveIntegerField(null=True, verbose_name='Позиция')
    
    class Meta:
        ordering = ['position']
        verbose_name = "Заявка"
        verbose_name_plural = "Заявкы"

    def __str__(self) -> str:
        return self.name
