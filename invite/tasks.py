import json
import uuid
from datetime import timedelta

from celery import shared_task
from django.utils import timezone
from django_celery_beat.models import CrontabSchedule, PeriodicTask

from core.tasks import send_email

WAITING_CANCEL = 6
WAITING_PAY_NOTIFICATION = 24 - WAITING_CANCEL
PAYED_NOTIFICATION = 24 * 30 - WAITING_PAY_NOTIFICATION
WAITING_PAY_NOTIFICATION_SUBJECT = "Cancel invite"
WAITING_PAY_NOTIFICATION_TEXT = "Cancel invite {instance_id}, Your invite will be cancel after {hours} hours"
PAYED_NOTIFICATION_SUBJECT = "Cancel invite payed"
PAYED_NOTIFICATION_TEXT = "Cancel invite {instance_id}, Your invite will be cancel after {hours} hours"
CANCELED_SUBJECT = "Canceled invite"
CANCELED_TEXT = "Cancel invite {instance_id}"


def _notification_before(model, ids, state):
    if ids:
        qs = model.objects.filter(id__in=ids, status=state).exclude(status__in=['finished', 'canceled'])
    else:
        qs = model.objects.filter(status=state).exclude(status__in=['finished', 'canceled'])
    for instance in qs:
        subject = WAITING_PAY_NOTIFICATION_SUBJECT if instance.status == "waiting_pay" else PAYED_NOTIFICATION_SUBJECT
        message = WAITING_PAY_NOTIFICATION_TEXT if instance.status == "waiting_pay" else WAITING_PAY_NOTIFICATION_TEXT
        send_email.delay(
            instance.order.user.email, subject,
            message.format(instance_id=instance.id, hours=WAITING_CANCEL)
        )
        crontab, _ = CrontabSchedule.objects.get_or_create(hour=f"*/{WAITING_CANCEL}")
        PeriodicTask.objects.create(
            name=str(uuid.uuid4()),
            task="cancel_org_invite",
            kwargs=json.dumps({'ids': [str(instance.id)], "state": state}),
            start_time=timezone.now() + timedelta(hours=WAITING_CANCEL),
            one_off=True,
            crontab=crontab,
            description=message,
        )


def _cancel_invite(model, ids, state):
    if ids:
        qs = model.objects.filter(id__in=ids).exclude(status__in=['finished', 'canceled'])
    else:
        qs = model.objects.exclude(status__in=['finished', 'canceled'])

    for instance in qs:
        if instance.status == state:
            send_email.delay(instance.order.user.email, CANCELED_SUBJECT, CANCELED_TEXT)
            instance.status = 'canceled'
            instance.save()
        else:
            if instance.status == 'payed':
                crontab, _ = CrontabSchedule.objects.get_or_create(hour=f"*/{PAYED_NOTIFICATION}")
                PeriodicTask.objects.create(
                    name=str(uuid.uuid4()),
                    task="notification_before_org",
                    kwargs=json.dumps({'ids': [str(instance.id)], 'state': 'payed'}),
                    start_time=timezone.now() + timedelta(hours=PAYED_NOTIFICATION),
                    one_off=True, crontab=crontab,
                    description=f"Уведамление юр. лица {instance.id} с 'ожидание оплаты' на 'отклонена'",
                )


@shared_task(name="notification_before_org")
def notification_before_org(ids=None, state="waiting_pay"):
    from .models import OrgInvite

    _notification_before(OrgInvite, ids, state)


@shared_task(name="cancel_org_invite")
def cancel_org_invite(ids=None, state='waiting_pay'):
    from .models import OrgInvite

    _cancel_invite(OrgInvite, ids, state)


@shared_task(name="notification_before_client")
def notification_before_client(ids=None, state="waiting_pay"):
    from .models import ClientInvite

    _notification_before(ClientInvite, ids, state)


@shared_task(name="cancel_client_invite")
def cancel_client_invite(ids=None, state='waiting_pay'):
    from .models import ClientInvite

    _cancel_invite(ClientInvite, ids, state)
