from django import forms
from karer_web.models import Car, Driver, Karer, Organization, Client


class OrgInviteDashboardForm(forms.Form):
    period = forms.ChoiceField(choices=[
        ('day', 'По дням'),
        ('week', 'По неделям'),
        ('month', 'По месячам'),
        ('quarter', "По квартал"),
        ('year', 'По годом'),
    ], label='Период')

    car = forms.MultipleChoiceField(choices=[(c.id, c.number) for c in Car.objects.all()], required=False, label='Машина')
    driver = forms.MultipleChoiceField(choices=[(c.id, c.name) for c in Driver.objects.all()], required=False, label='Водител')
    karer = forms.MultipleChoiceField(choices=[(c.id, c.name) for c in Karer.objects.all()], required=False, label='Карьер')
    organizaton = forms.MultipleChoiceField(choices=[(c.id, c.name) for c in Organization.objects.all()], required=False, label='Организация')


class ClientInviteDashboardForm(forms.Form):
    period = forms.ChoiceField(choices=[
        ('day', 'По дням'),
        ('week', 'По неделям'),
        ('month', 'По месячам'),
        ('quarter', "По квартал"),
        ('year', 'По годом'),
    ], label='Период')

    car = forms.MultipleChoiceField(choices=[(c.id, c.number) for c in Car.objects.all()], required=False, label='Машина')
    driver = forms.MultipleChoiceField(choices=[(c.id, c.name) for c in Driver.objects.all()], required=False, label='Водител')
    karer = forms.MultipleChoiceField(choices=[(c.id, c.name) for c in Karer.objects.all()], required=False, label='Карьер')
    client = forms.MultipleChoiceField(choices=[(c.id, c.name) for c in Client.objects.all()], required=False, label='Физ. лицо')
 