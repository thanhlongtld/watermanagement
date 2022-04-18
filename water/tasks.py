from celery import shared_task
from django.core.mail import send_mail

from watermanagement import settings


@shared_task(bind=True)
def test_func(self):
    for i in range(10):
        print(i)
    return "DONE"


@shared_task(bind=True)
def send_mail_func(self):
    send_mail("Test 18.4","Test Test",settings.EMAIL_HOST_USER,['dungtn312@gmail.com'],True)
    return "DONE mail"
