from . import views
from django.urls import path

urlpatterns = [
    path('turer/', views.tripstest, name='trips'),
]