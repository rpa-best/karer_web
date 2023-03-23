from django.contrib import admin
from adminsortable2.admin import SortableStackedInline
from .models import OrgImportInvite, ClientImportInvite


class OrgInviteTabular(SortableStackedInline):
    model = OrgImportInvite
    sortable_field_name = 'position'
    extra = 0
    exclude = ['finish_at']
    readonly_fields = ['status']

    def has_change_permission(self, request, obj = None) -> bool:
        return False
    
    def formfield_for_dbfield(self, *args, **kwargs):
        formfield = super().formfield_for_dbfield(*args, **kwargs)
        formfield.widget.can_delete_related = False
        formfield.widget.can_change_related = False
        formfield.widget.can_add_related = False
        formfield.widget.can_view_related = False
        return formfield


class ClientInviteTabular(SortableStackedInline):
    model = ClientImportInvite
    sortable_field_name = 'position'
    extra = 0
    exclude = ['finish_at']
    readonly_fields = ['status']

    def has_change_permission(self, request, obj = None) -> bool:
        return False
    
    def formfield_for_dbfield(self, *args, **kwargs):
        formfield = super().formfield_for_dbfield(*args, **kwargs)
        formfield.widget.can_delete_related = False
        formfield.widget.can_change_related = False
        formfield.widget.can_add_related = False
        formfield.widget.can_view_related = False
        return formfield
