from django.urls import path

from . import views

urlpatterns = [
    path('', views.login_page, name='login_page'),
    path('newuser', views.register, name='newuser'),
]