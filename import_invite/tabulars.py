from django.contrib import admin
from adminsortable2.admin import SortableStackedInline
from .models import OrgImportInvite, ClientImportInvite


class OrgInviteTabular(SortableStackedInline):
    model = OrgImportInvite
    sortable_field_name = 'position'
    extra = 0
    exclude = ['finish_at']
    readonly_fields = ['status']


class ClientInviteTabular(SortableStackedInline):
    model = ClientImportInvite
    sortable_field_name = 'position'
    extra = 0
    exclude = ['finish_at']
    readonly_fields = ['status']