from adminsortable2.admin import SortableAdminBase
from django.contrib import admin, messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import path, reverse
from django.utils.translation import gettext_lazy as _
from import_export.admin import ExportActionMixin
from simple_history.admin import SimpleHistoryAdmin

from core.mixins import OwnQuerysetMixin, ReadOnlyAdminModelMixin

from . import models, resources, tabulars


@admin.register(models.OrgOrder)
class OrgOrderAdmin(OwnQuerysetMixin, ExportActionMixin, SortableAdminBase, admin.ModelAdmin):
    resource_class = resources.OrgInviteResource
    list_display = ['id', 'create_at', 'finish_at']
    exclude = ['finish_at', 'create_at', "user"]
    list_filter = ['organization']
    inlines = [tabulars.OrgInviteTabular]
    list_per_page = 10

    def get_readonly_fields(self, request, obj=None):
        return super().get_readonly_fields(request, obj) if not obj else ['karer', 'desc', 'organization']

    def export_admin_action(self, request, queryset):
        """
        Exports the selected rows using file_format.
        """
        export_format = request.POST.get('file_format')
        queryset = models.OrgInvite.objects.filter(order__in=queryset)

        if not export_format:
            messages.warning(request, _('You must select an export format.'))
        else:
            formats = self.get_export_formats()
            file_format = formats[int(export_format)]()

            export_data = self.get_export_data(file_format, queryset, request=request, encoding=self.to_encoding)
            content_type = file_format.get_content_type()
            response = HttpResponse(export_data, content_type=content_type)
            response['Content-Disposition'] = 'attachment; filename="%s"' % (
                self.get_export_filename(request, queryset, file_format),
            )
            return response

    def get_actions(self, request):
        """
        Adds the export action to the list of available actions.
        """

        actions = super().get_actions(request)
        actions.update(
            export_admin_action=(
                OrgOrderAdmin.export_admin_action,
                "export_admin_action",
                _("Export selected %(verbose_name_plural)s"),
            )
        )
        return actions

    def get_urls(self):
        my_urls = [
            path('<path:object_id>/change/<path:invite_id>/manual-mode/',
                 self.invite_manual_mode,
                 name='%s_%s_manual-mode' % ("invite", "orginvite")),
            path('<path:object_id>/change/<path:invite_id>/recover/',
                 self.invite_recover,
                 name='%s_%s_recover' % ("invite", "orginvite")),
        ]
        return my_urls + super().get_urls()

    def invite_recover(self, request, object_id, invite_id):
        invite = get_object_or_404(models.OrgInvite, id=invite_id)
        invite.status = 'waiting_pay'
        invite.save()
        models.org_invite_schedules(models.OrgInvite, invite, True)
        messages.add_message(request, messages.constants.SUCCESS, "Заявка восстановлено")
        url = reverse("admin:%s_%s_change" % self.get_model_info(), kwargs={"object_id": object_id})
        return HttpResponseRedirect(url)

    def invite_manual_mode(self, request, object_id, invite_id):
        try:
            print(request, invite_id)
            # TODO: post request
            messages.add_message(request, messages.constants.INFO, "Заявка перешла на ручной режим")
        except Exception as _exp:
            messages.add_message(request, messages.constants.ERROR, str(_exp))
        url = reverse("admin:%s_%s_change" % self.get_model_info(), kwargs={"object_id": object_id})
        return HttpResponseRedirect(url)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)


@admin.register(models.ClientOrder)
class ClientOrderAdmin(OwnQuerysetMixin, ExportActionMixin, SortableAdminBase, admin.ModelAdmin):
    resource_classes = [resources.ClientInviteResource]
    list_display = ['id', 'create_at', 'finish_at']
    exclude = ['finish_at', 'create_at', "user"]
    list_filter = ['client']
    inlines = [tabulars.ClientInviteTabular]
    list_per_page = 10

    def get_readonly_fields(self, request, obj=None):
        return super().get_readonly_fields(request, obj) if not obj else ['karer', 'desc', 'client']

    def export_admin_action(self, request, queryset):
        """
        Exports the selected rows using file_format.
        """
        export_format = request.POST.get('file_format')
        queryset = models.ClientInvite.objects.filter(order__in=queryset)

        if not export_format:
            messages.warning(request, _('You must select an export format.'))
        else:
            formats = self.get_export_formats()
            file_format = formats[int(export_format)]()

            export_data = self.get_export_data(file_format, queryset, request=request, encoding=self.to_encoding)
            content_type = file_format.get_content_type()
            response = HttpResponse(export_data, content_type=content_type)
            response['Content-Disposition'] = 'attachment; filename="%s"' % (
                self.get_export_filename(request, queryset, file_format),
            )
            return response

    def get_actions(self, request):
        """
        Adds the export action to the list of available actions.
        """

        actions = super().get_actions(request)
        actions.update(
            export_admin_action=(
                ClientOrderAdmin.export_admin_action,
                "export_admin_action",
                _("Export selected %(verbose_name_plural)s"),
            )
        )
        return actions

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)


@admin.register(models.OrgInvite)
class OrgInviteAdmin(OwnQuerysetMixin, ReadOnlyAdminModelMixin, SimpleHistoryAdmin):
    exclude = ["id", "position"]
    history_list_display = ["status"]
    history_exclude = ('history_reason',)


@admin.register(models.ClientInvite)
class ClientInviteAdmin(OwnQuerysetMixin, ReadOnlyAdminModelMixin, SimpleHistoryAdmin):
    exclude = ["id", "position"]
    history_list_display = ["status"]
    history_exclude = ('history_reason',)
