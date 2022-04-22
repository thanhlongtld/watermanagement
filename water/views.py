from django.core.mail import EmailMessage, BadHeaderError
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils.html import strip_tags
from django_celery_beat.models import CrontabSchedule, PeriodicTask

from watermanagement import settings
from .models import User, Client
from .tasks import send_mail_func


# Create your views here.


def index(request):
    return render(request, "water/index.html")


def newmail(request):
    clients = Client.objects.all()
    context = {'clients': clients}
    if request.method == 'POST':
        client_mail = request.POST.get("client_mail")
        title = request.POST.get("title")
        message = request.POST.get("message")
        message = strip_tags(message)
        files = request.FILES.getlist('file')

        for file in files:
            print(file.name)
        print(client_mail)
        print(title)
        print(message)

        email = EmailMessage(title, message, settings.EMAIL_HOST_USER, [client_mail])
        for file in files:
            email.attach(file.name, file.read(), file.content_type)
        try:
            email.send()
        except BadHeaderError:
            return HttpResponse('invalid header found')
        return redirect('new-mail')
    return render(request, "water/newmail.html", context)


# auto mail
def test_func(requset):
    send_mail_func.delay()
    return HttpResponse("send_mail")


def schedule_mail(requset):
    schedule, created = CrontabSchedule.objects.get_or_create(hour=10, minute=42)
    task = PeriodicTask.objects.get(name="send_billing_email")
    task.crontab = schedule
    task.save()
    return HttpResponse("scheduled")
