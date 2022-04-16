from django.core.mail import EmailMessage, BadHeaderError
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils.html import strip_tags

from watermanagement import settings
from .models import User, Client


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
