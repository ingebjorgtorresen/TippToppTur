from django.urls import path

from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('register/', views.register, name='register'),
    path('register_new_user', views.register_user, name='register_user'),
]