from . import views
from django.urls import path

urlpatterns = [
    path('turer/', views.tripstest, name='trips'),
    path('delete_event', views.deleteEvent, name='deleteEvent'),
    path('edit_event', views.editEvent, name='editEvent'),
    path('update_event', views.updateEvent, name='updateEvent'),
    path('turer/upvote/', views.upvote, name='upvote'),
    path('turer/downvote/', views.downvote, name='downvote'),
]