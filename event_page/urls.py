from django.urls import path

from . import views

urlpatterns = [
    path('', views.event_page, name='event_page'),
    path('/id<int:num>/', views.event_page, name='event_page'),
]