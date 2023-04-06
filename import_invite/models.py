import uuid
from django.db import models


class BaseImport(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    karer = models.ForeignKey('karer_web.Karer', models.PROTECT, verbose_name='Объект')
    desc = models.TextField(verbose_name='Описание')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    finish_at = models.DateTimeField(blank=True, null=True, verbose_name='Дата закрытия')

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return str(self.id)


class OrgImport(BaseImport):
    organization = models.ForeignKey("karer_web.Organization", models.PROTECT, verbose_name='Организация')

    class Meta:
        verbose_name = "Импорт юр. лицо"
        verbose_name_plural = "Импорты юр. лицо"


class BaseImportInvite(models.Model):
    STATUS = (
        ('waiting_pay', 'Ожидает оплаты'),
        ('payed', 'Оплачено'),
        ('finished', 'Успешно'),
        ('canceled', 'Отклонена')
    )
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    product = models.ForeignKey("marketplace.Product", models.PROTECT, verbose_name='Продукт', null=True)
    car = models.ForeignKey("karer_web.Car", models.PROTECT, verbose_name='Номер машины')
    driver = models.ForeignKey("karer_web.Driver", models.PROTECT, verbose_name='Водитель')
    weight = models.FloatField(verbose_name='Потребность (кг)')
    status = models.CharField(max_length=255, choices=STATUS, default='created', verbose_name='Статус')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    finish_at = models.DateTimeField(blank=True, null=True, verbose_name='Дата закрытия')
    position = models.PositiveIntegerField(null=True, verbose_name='Позиция')
    
    class Meta:
        abstract = True

    def __str__(self) -> str:
        return str(self.product)
    
    @classmethod
    def check_plate(cls, plate, karer_slug):
        return cls.objects.filter(car__number=plate, order__karer__slug=karer_slug, status__in=['payed', 'waiting_pay', 'accepted', 'created']).exists()


class OrgImportInvite(BaseImportInvite):
    order = models.ForeignKey(OrgImport, models.CASCADE, verbose_name='Импорт')

    class Meta:
        ordering = ['position']
        verbose_name = "Заявка юр. лицо"
        verbose_name_plural = "Заявкы юр. лицо"
