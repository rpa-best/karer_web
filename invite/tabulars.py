from django.contrib import admin
from adminsortable2.admin import SortableStackedInline
from .models import OrgInvite, ClientInvite


class OrgInviteTabular(SortableStackedInline):
    model = OrgInvite
    sortable_field_name = 'position'
    extra = 0
    exclude = ['finish_at']
    readonly_fields = ['status']

    def has_change_permission(self, request, obj = None) -> bool:
        return False


class ClientInviteTabular(SortableStackedInline):
    model = ClientInvite
    sortable_field_name = 'position'
    extra = 0
    exclude = ['finish_at']
    readonly_fields = ['status']

    def has_change_permission(self, request, obj = None) -> bool:
        return False
