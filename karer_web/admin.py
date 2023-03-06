from django.contrib import admin
from . import models


admin.site.site_title = 'Карьер'
admin.site.site_header = 'Карьер'
admin.site.index_title = 'Главная'

@admin.register(models.Karer)
class KarerAdmin(admin.ModelAdmin):
    pass


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
