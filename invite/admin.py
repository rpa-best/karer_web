from django.contrib import admin
from adminsortable2.admin import SortableAdminBase
from . import models, tabulars


@admin.register(models.Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['number', 'model', 'vin_number']


@admin.register(models.Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone']


@admin.register(models.Organization)
class OrganizationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Client)
class ClientAdmin(admin.ModelAdmin):
    pass


@admin.register(models.OrgOrder)
class OrgOrderAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ['name', 'create_at', 'finish_at', 'status']
    exclude = ['finish_at', 'status', 'create_at']
    list_filter = ['status', 'organization']
    inlines = [tabulars.OrgInviteTabular]


@admin.register(models.ClientOrder)
class ClientOrderAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ['name', 'create_at', 'finish_at', 'status']
    exclude = ['finish_at', 'status', 'create_at']
    list_filter = ['status', 'client']
    inlines = [tabulars.ClientInviteTabular]
