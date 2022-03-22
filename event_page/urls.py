from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.event_page, name='event_page'),
    path('register_events', views.register_event, name='register_event')
]