from django.urls import path
from . import  views

urlpatterns = [
    path("", views.ToDoSimple.as_view()),
    path("<int:id>", views.ToDoDetail.as_view())
]