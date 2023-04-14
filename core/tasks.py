from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


@shared_task(name='send_email')
def send_email(email, subject, text):
    send_mail(subject, text, settings.EMAIL_HOST_USER, [email])
