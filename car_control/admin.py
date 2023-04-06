from django.contrib import admin
from karer_web.mixins import ReadOnlyAdminModelMixin
from .models import CarControl


@admin.register(CarControl)
class CarControl(ReadOnlyAdminModelMixin, admin.ModelAdmin):
    pass
