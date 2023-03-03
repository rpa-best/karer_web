from django.contrib import admin
from adminsortable2.admin import SortableAdminBase
from . import models, filters, tabulars


@admin.register(models.Organization)
class Organization(admin.ModelAdmin):
    pass


@admin.register(models.Order)
class OrderAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ['name', 'create_at', 'finish_at', 'status']
    exclude = ['finish_at', 'status', 'create_at']
    list_filter = (filters.InviteStatusFilter,)
    inlines = [tabulars.InviteTabular]


@admin.register(models.Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['number', 'model', 'vin_number']


@admin.register(models.Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone']
