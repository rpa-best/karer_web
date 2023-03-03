from django.contrib import admin
from adminsortable2.admin import SortableTabularInline
from .models import Invite


class InviteTabular(SortableTabularInline):
    model = Invite
    sortable_field_name = 'position'
    extra = 0
    exclude = ['finish_at']
    readonly_fields = ['status']
