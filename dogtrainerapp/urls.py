from django.contrib import admin
from django.urls import path
from dogtrainerapp import views

urlpatterns = [
    path("", views.index, name='index'),
    path("contact", views.contact, name='contact'),
    path("about", views.about, name='about'),
]
