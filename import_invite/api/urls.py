from django.urls import path
from .views import InvitePlateCheck

urlpatterns = [
    path('check/<str:plate>/', InvitePlateCheck.as_view()),
]