from django.urls import path

from .views import InvitePlateCheck

urlpatterns = [
    path('check/', InvitePlateCheck.as_view()),
]
