from django.urls import reverse
from django.utils.html import format_html
from django.contrib import admin
from adminsortable2.admin import SortableStackedInline
from .models import OrgInvite, ClientInvite


class OrgInviteTabular(SortableStackedInline):
    model = OrgInvite
    sortable_field_name = 'position'
    extra = 0
    exclude = ['finish_at']
    readonly_fields = ['status', 'open_link']

    def has_change_permission(self, request, obj = None) -> bool:
        return False

    @admin.display(description='Подробно')
    def open_link(self, obj: OrgInvite):
        url = f"{reverse(f'admin:{self.model._meta.app_label}_{self.model._meta.model_name}_change', kwargs={'object_id': obj.id})}?language=uz-cl"
        return format_html(f"<a href='{url}'>Открыт</a>")


class ClientInviteTabular(SortableStackedInline):
    model = ClientInvite
    sortable_field_name = 'position'
    extra = 0
    exclude = ['finish_at']
    readonly_fields = ['status', 'open_link']

    def has_change_permission(self, request, obj = None) -> bool:
        return False

    @admin.display(description='Подробно')
    def open_link(self, obj: OrgInvite):
        url = f"{reverse(f'admin:{self.model._meta.app_label}_{self.model._meta.model_name}_change', kwargs={'object_id': obj.id})}?language=uz-cl"
        return format_html(f"<a href='{url}'>Открыт</a>")
