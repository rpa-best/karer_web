import uuid
from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from import_invite.models import OrgImportInvite, ClientImportInvite

class BaseOrder(models.Model):
    STATUS = (
        ('created', 'Создано'),
        ('accepted', 'Принята'),
        ('waiting_pay', 'Ожидает оплаты'),
        ('payed', 'Оплачено'),
        ('finished', 'Успешно'),
        ('canceled', 'Отклонена')
    )
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    karer = models.ForeignKey('karer_web.Karer', models.PROTECT)
    desc = models.TextField(verbose_name='Описание')
    status = models.CharField(max_length=255, choices=STATUS, default='created', verbose_name='Статус')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    finish_at = models.DateTimeField(blank=True, null=True, verbose_name='Дата закрытия')

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return str(self.id)


class OrgOrder(BaseOrder):
    organization = models.ForeignKey("karer_web.Organization", models.PROTECT, verbose_name='Организация')

    class Meta:
        verbose_name = "Заказ юр. лицо"
        verbose_name_plural = "Заказы юр. лицо"


class ClientOrder(BaseOrder):
    client = models.ForeignKey("karer_web.Client", models.PROTECT, verbose_name='Физ. лицо')

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
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    product = models.ForeignKey("marketplace.Product", models.PROTECT, verbose_name='Продукт', null=True)
    car = models.ForeignKey("karer_web.Car", models.PROTECT, verbose_name='Номер машины')
    driver = models.ForeignKey("karer_web.Driver", models.PROTECT, verbose_name='Водитель')
    weight = models.FloatField(verbose_name='Потребность (кг)', validators=[MinValueValidator(1)])
    status = models.CharField(max_length=255, choices=STATUS, default='created', verbose_name='Статус')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    finish_at = models.DateTimeField(blank=True, null=True, verbose_name='Дата закрытия')
    position = models.PositiveIntegerField(null=True, verbose_name='Позиция')
    
    class Meta:
        abstract = True

    def __str__(self) -> str:
        return str(self.product)
    
    def clean(self) -> None:
        imports = OrgImportInvite.objects.filter(product_id=self.product_id, order__karer_id=self.order.karer_id).aggregate(sum=models.Sum('weight'))['sum'] or 0 + \
            (ClientImportInvite.objects.filter(product_id=self.product_id, order__karer_id=self.order.karer_id).aggregate(sum=models.Sum('weight'))['sum'] or 0)
        exports = OrgInvite.objects.filter(product_id=self.product_id, order__karer_id=self.order.karer_id).aggregate(sum=models.Sum('weight'))['sum'] or 0 + \
            (ClientInvite.objects.filter(product_id=self.product_id, order__karer_id=self.order.karer_id).aggregate(sum=models.Sum('weight'))['sum'] or 0)
        delta = imports - exports
        if delta < self.weight:
            raise ValidationError(f"Продукт не достатучном колечестве, имеется {delta} {self.product.unit}")
        return super().clean()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None) -> None:
        self.full_clean()
        return super().save(force_insert, force_update, using, update_fields)
    
    @classmethod
    def check_plate(cls, plate, karer_slug):
        return cls.objects.filter(car__number=plate, order__karer__slug=karer_slug, status__in=['payed', 'waiting_pay', 'accepted', 'created']).exists()


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
