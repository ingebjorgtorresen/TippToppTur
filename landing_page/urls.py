from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('turer/', views.trips, name='trips'),
    path('minside/', views.myPage, name='mypage'),
]