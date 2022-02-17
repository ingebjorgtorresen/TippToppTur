from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login_page, name='login_page'),
    path('login_b/', views.login_b, name='login'),
    path('register/', views.register, name='register'),
]