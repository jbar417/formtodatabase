from django.urls import path
from . import views

urlpatterns = [
    path("", views.functionview1.as_view()),
    path("submitted", views.functionsubmitted),
]