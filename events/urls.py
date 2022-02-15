from . import views
from django.urls import path

urlpatterns = [
    path('turer/', views.trips, name='trips'),
]