from django.urls import path
from . import views

urlpatterns = [
    path("", views.Houses.as_view())
]