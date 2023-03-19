from django.urls import path,include
from django.contrib import admin
from . import views

urlpatterns = [
    path("index",views.index,name="index"),
    path("<int:flight_id>",views.flight,name="flight"),
    path("<int:flight_id>/book",views.book,name="book"),
    path("<int:flight_id>/unbook",views.unbook_flight,name="unbook"),
]