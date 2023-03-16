from django import forms
from .models import Organization

class OrganizationCreateForm(forms.ModelForm):

    class Meta:
        model = Organization
        fields = ['inn', 'bik', 'phone']


class InviteDashboardForm(forms.Form):
    period = forms.ChoiceField(choices=[
        ('day', 'По дням'),
        ('week', 'По неделям'),
        ('month', 'По месячам'),
        ('quarter', "По квартал"),
        ('year', 'По годом'),
    ], label='Период')
    