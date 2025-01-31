from django.urls import path
from . import views

urlpatterns = [
    path("main/", views.mainpage, name="mainpage"),
    path("tutorial/", views.tutorialpage, name="tutorial"),
]