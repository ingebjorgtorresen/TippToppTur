from django.urls import path

from . import views

urlpatterns = [
    #path('', views.register, name='register'),
    path('register/', views.register, name='register'),
    path('register_new_user', views.register_user, name='register_user'),
    path('login/', views.login_page, name='login_page'),
    path('login_b/', views.login_b, name='login'),
    path('logout/', views.logout_b, name='logout'),
    path('register_serious/', views.register_serious, name='register_serious'),
    path('register_serious_user/', views.register_serious_user, name='register_serious_user'),
]