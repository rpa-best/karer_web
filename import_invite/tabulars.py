from adminsortable2.admin import SortableStackedInline

from .models import OrgImportInvite


class OrgInviteTabular(SortableStackedInline):
    model = OrgImportInvite
    sortable_field_name = 'position'
    extra = 0
    exclude = ['finish_at']
    readonly_fields = ['status']

    def has_change_permission(self, request, obj=None) -> bool:
        return False
