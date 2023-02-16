from django.contrib.admin import filters
from . import models

class InviteStatusFilter(filters.SimpleListFilter):
    title = 'Статус'
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return models.Invite.STATUS

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(status=self.value())
        return queryset.filter(status__in=['created', 'accepted', 'waiting_pay'])
