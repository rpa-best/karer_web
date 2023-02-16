from django.contrib import admin
from . import models
from . import filters

@admin.register(models.Invite)
class InviteAdmin(admin.ModelAdmin):
    list_display = ['name', 'car', 'create_at', 'finish_at', 'status']
    exclude = ['finish_at', 'status', 'create_at']
    list_filter = (filters.InviteStatusFilter, 'car', 'driver')
    

@admin.register(models.Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['number', 'model', 'vin_number']


@admin.register(models.Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone']
