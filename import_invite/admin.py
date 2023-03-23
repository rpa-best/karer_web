from django.contrib import admin, messages
from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _
from adminsortable2.admin import SortableAdminBase
from import_export.admin import ExportActionMixin
from . import models, tabulars, resources


@admin.register(models.OrgImport)
class OrgOrderAdmin(ExportActionMixin, SortableAdminBase, admin.ModelAdmin):
    resource_class = resources.OrgInviteResource
    list_display = ['id', 'create_at', 'finish_at', 'status']
    exclude = ['finish_at', 'status', 'create_at']
    list_filter = ['status', 'organization']
    inlines = [tabulars.OrgInviteTabular]

    def formfield_for_dbfield(self, *args, **kwargs):
        formfield = super().formfield_for_dbfield(*args, **kwargs)
        formfield.widget.can_delete_related = False
        formfield.widget.can_change_related = False
        formfield.widget.can_add_related = False
        formfield.widget.can_view_related = False
        return formfield

    def get_readonly_fields(self, request, obj=None):
        return super().get_readonly_fields(request, obj) if not obj else ['karer', 'desc', 'organization']

    def export_admin_action(self, request, queryset):
        """
        Exports the selected rows using file_format.
        """
        export_format = request.POST.get('file_format')
        queryset = models.OrgImportInvite.objects.filter(order__in=queryset)

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


@admin.register(models.ClientImport)
class ClientOrderAdmin(ExportActionMixin, SortableAdminBase, admin.ModelAdmin):
    resource_classes = [resources.ClientInviteResource]
    list_display = ['id', 'create_at', 'finish_at', 'status']
    exclude = ['finish_at', 'status', 'create_at']
    list_filter = ['status', 'client']
    inlines = [tabulars.ClientInviteTabular]

    def formfield_for_dbfield(self, *args, **kwargs):
        formfield = super().formfield_for_dbfield(*args, **kwargs)
        formfield.widget.can_delete_related = False
        formfield.widget.can_change_related = False
        formfield.widget.can_add_related = False
        formfield.widget.can_view_related = False
        return formfield

    def get_readonly_fields(self, request, obj=None):
        return super().get_readonly_fields(request, obj) if not obj else ['karer', 'desc', 'client']
    
    def export_admin_action(self, request, queryset):
        """
        Exports the selected rows using file_format.
        """
        export_format = request.POST.get('file_format')
        queryset = models.ClientImportInvite.objects.filter(order__in=queryset)

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
