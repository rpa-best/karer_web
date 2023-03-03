from django.contrib import admin
from adminsortable2.admin import SortableTabularInline
from .models import OrgInvite, ClientInvite


class OrgInviteTabular(SortableTabularInline):
    model = OrgInvite
    sortable_field_name = 'position'
    extra = 0
    exclude = ['finish_at']
    readonly_fields = ['status']


class ClientInviteTabular(SortableTabularInline):
    model = ClientInvite
    sortable_field_name = 'position'
    extra = 0
    exclude = ['finish_at']
    readonly_fields = ['status']