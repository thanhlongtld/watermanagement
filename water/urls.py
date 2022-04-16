from django.urls import path
from . import views

urlpatterns = [
    path("test", views.index, name="test"),

    #     send mail path
    path("newmail", views.newmail, name="new-mail")
]
