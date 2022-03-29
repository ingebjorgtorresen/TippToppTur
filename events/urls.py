from . import views
from django.urls import path

urlpatterns = [
    path('turer/', views.tripstest, name='trips'),
    path('turer/search_results', views.search_results, name='search_results'),
    path('delete_event', views.deleteEvent, name='deleteEvent'),
    path('edit_event', views.editEvent, name='editEvent'),
    path('update_event', views.updateEvent, name='updateEvent')
]