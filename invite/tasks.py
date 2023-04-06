from celery import shared_task
from .models import OrgInvite, ClientInvite


@shared_task(name='cancel_org_waiting_pay')
def cancel_org_waiting_pay(ids=None):
    print(ids)
    if ids:
        OrgInvite.objects.filter(id__in=ids).update(status="canceled")
    else:
        OrgInvite.objects.filter(status__in=['waiting_pay']).update(status="canceled")


@shared_task(name='cancel_org_payed')
def cancel_org_payed(ids=None):
    if ids:
        OrgInvite.objects.filter(id__in=ids).update(status="canceled")
    else:
        OrgInvite.objects.filter(status__in=['payed']).update(status="canceled")


@shared_task(name='cancel_client_waiting_pay')
def cancel_client_waiting_pay(ids=None):
    if ids:
        ClientInvite.objects.filter(id__in=ids).update(status="canceled")
    else:
        ClientInvite.objects.filter(status__in=['waiting_pay']).update(status="canceled")
    
    

@shared_task(name='cancel_client_payed')
def cancel_client_payed(ids=None):
    if ids:
        ClientInvite.objects.filter(id__in=ids).update(status="canceled")
    else:
        ClientInvite.objects.filter(status__in=['payed']).update(status="canceled")
   
