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


class BaseOrder(models.Model):
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
    status = models.CharField(max_length=255, choices=STATUS, default='created', verbose_name='Статус')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    finish_at = models.DateTimeField(blank=True, null=True, verbose_name='Дата закрытия')

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return self.name


class OrgOrder(BaseOrder):
    organization = models.ForeignKey(Organization, models.PROTECT, verbose_name='Организация')

    class Meta:
        verbose_name = "Заказ юр. лицо"
        verbose_name_plural = "Заказы юр. лицо"


class ClientOrder(BaseOrder):
    client = models.ForeignKey(Client, models.PROTECT, verbose_name='Физ. лицо')

    class Meta:
        verbose_name = "Заказ физ. лицо"
        verbose_name_plural = "Заказы физ. лицо"


class BaseInvite(models.Model):
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
    weight = models.FloatField(verbose_name='Потребность (кг)')
    status = models.CharField(max_length=255, choices=STATUS, default='created', verbose_name='Статус')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    finish_at = models.DateTimeField(blank=True, null=True, verbose_name='Дата закрытия')
    position = models.PositiveIntegerField(null=True, verbose_name='Позиция')
    
    class Meta:
        abstract = True

    def __str__(self) -> str:
        return self.name


class ClientInvite(BaseInvite):
    order = models.ForeignKey(ClientOrder, models.CASCADE, verbose_name='Заказ')

    class Meta:
        ordering = ['position']
        verbose_name = "Заявка физ. лицо"
        verbose_name_plural = "Заявкы физ. лицо"


class OrgInvite(BaseInvite):
    order = models.ForeignKey(OrgOrder, models.CASCADE, verbose_name='Заказ')

    class Meta:
        ordering = ['position']
        verbose_name = "Заявка юр. лицо"
        verbose_name_plural = "Заявкы юр. лицо"
