from django.urls import path
from . import views

urlpatterns = [
    path("test", views.index, name="test"),

    #     send mail path
    path("newmail", views.newmail, name="new-mail"),

    # test automail
    path("auto", views.test_func, name="test-func"),
    path("schedule", views.schedule_mail, name="schedule-mail")
]
