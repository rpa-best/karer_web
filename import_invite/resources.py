from import_export.resources import ModelResource, Field
from . import models

class InviteResource(ModelResource):
    id = Field('id', 'ID')
    karer = Field('order__karer', 'Карьер')
    desc = Field('order__desc', 'Описание')
    create_at = Field('create_at', 'Дата создание')
    finish_at = Field('finish_at', 'Дата завершение')
    name = Field('name', 'Название товара')
    car = Field('car', 'Машина')
    driver = Field('driver', 'Водител')
    weight = Field('weight', "Потребность (кг)")


    
class ClientInviteResource(InviteResource):
    client = Field('order__client', 'Физ. лицо')

    class Meta:
        model = models.ClientImportInvite
        exclude = ['status', 'position', 'order']


class OrgInviteResource(InviteResource):
    organization = Field('order__organization', 'Юр. лицо')

    class Meta:
        model = models.OrgImportInvite
        exclude = ['status', 'position', 'order']
