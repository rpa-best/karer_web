from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as _UserAdmin
from django.utils.translation import gettext_lazy as _
from . import models, forms, mixins


admin.site.site_title = 'Объект'
admin.site.site_header = 'Объект'
admin.site.index_title = 'Главная'


@admin.register(models.Karer)
class KarerAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['number', 'model', 'vin_number']
    

@admin.register(models.Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone']


@admin.register(models.Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['inn', 'name']
    list_display_links = ['name']

    def get_readonly_fields(self, request, obj=None):
        return ['name', 'address', 'ogrn', 'kpp'] if obj else []

    def get_form(self, request, obj=None, change=False, **kwargs):
        if not obj:
            return forms.OrganizationCreateForm
        return super().get_form(request, obj, change, **kwargs)


@admin.register(models.Client)
class ClientAdmin(admin.ModelAdmin):
    pass


@admin.register(models.User)
class UserAdmin(_UserAdmin):
    readonly_fields = ['last_login', 'date_joined']
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                    "karer",
               ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
