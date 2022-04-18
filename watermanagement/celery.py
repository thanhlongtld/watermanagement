from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'watermanagement.settings')

app = Celery('watermanagement')

app.conf.enable_utc = False

app.conf.update(timezone="Asia/Ho_Chi_Minh")

app.config_from_object(settings, namespace="CELERY")

# Celery Beat settings
app.conf.beat_schedule = {
    'send_billing_email': {
        'task': 'water.tasks.send_mail_func',
        'schedule': crontab(minute="*/1")
    }
}
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r} ')
