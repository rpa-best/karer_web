from django.contrib import admin
from adminsortable2.admin import SortableAdminBase
from . import models, tabulars


@admin.register(models.OrgOrder)
class OrgOrderAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ['id', 'create_at', 'finish_at', 'status']
    exclude = ['finish_at', 'status', 'create_at']
    list_filter = ['status', 'organization']
    inlines = [tabulars.OrgInviteTabular]


@admin.register(models.ClientOrder)
class ClientOrderAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ['id', 'create_at', 'finish_at', 'status']
    exclude = ['finish_at', 'status', 'create_at']
    list_filter = ['status', 'client']
    inlines = [tabulars.ClientInviteTabular]
