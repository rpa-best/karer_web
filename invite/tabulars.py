from django.contrib import admin
from adminsortable2.admin import SortableStackedInline
from .models import OrgInvite, ClientInvite


class OrgInviteTabular(SortableStackedInline):
    model = OrgInvite
    sortable_field_name = 'position'
    extra = 0
    exclude = ['finish_at']
    readonly_fields = ['status']


class ClientInviteTabular(SortableStackedInline):
    model = ClientInvite
    sortable_field_name = 'position'
    extra = 0
    exclude = ['finish_at']
    readonly_fields = ['status']