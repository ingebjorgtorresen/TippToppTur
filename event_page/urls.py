from django.urls import path

from . import views

urlpatterns = [
    path('', views.event_page, name='event_page'),
    path('', views.register_event, name='register_event'),
]