from django.urls import path

from . import views

urlpatterns = [
    path('', views.event_form, name='event_form'),
    path('new_event', views.new_event, name='new_event'),
]