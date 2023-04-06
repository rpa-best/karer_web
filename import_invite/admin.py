from django.contrib import admin, messages
from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _
from adminsortable2.admin import SortableAdminBase
from import_export.admin import ExportActionMixin
from karer_web.mixins import OwnQuerysetMixin
from . import models, tabulars, resources


@admin.register(models.OrgImport)
class OrgOrderAdmin(OwnQuerysetMixin, ExportActionMixin, SortableAdminBase, admin.ModelAdmin):
    resource_class = resources.OrgInviteResource
    list_display = ['id', 'create_at', 'finish_at']
    exclude = ['finish_at', 'create_at']
    list_filter = ['organization']
    inlines = [tabulars.OrgInviteTabular]

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
