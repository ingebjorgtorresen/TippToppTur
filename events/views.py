from django.shortcuts import redirect, render
from .models import Event
from django.utils.timezone import *

# Create your views here.
def trips(request):
    return render(request, 'landing_page/trips.html')

def tripstest(request):
    user = request.user
    event = Event.objects.all()
    context = {'tittel': event,
    'arrangør' : event,
    'dato' : event,
    'beskrivelse': event,
    'bilde' : event,
    'user': user.is_authenticated,
    'name': user.username,
    'view': True}
    return render(request, 'landing_page/trips.html', context)

def deleteEvent(request):
    id = request.GET.get('id', '0')
    event = Event.objects.get(pk=id)
    event.deleteEvent()
    return redirect("trips")

def editEvent(request):
    id = request.GET.get('id', '0')
    event = Event.objects.get(pk=id)
    context = {'tittel': event.tittel,
    'dato' : datetime.strftime(event.dato, "%Y-%m-%d"),
    'beskrivelse': event.beskrivelse}
    print(context)
    return render(request, 'edit_event/edit_event_form.html', context)

def updateEvent(request):
    #TODO fiks denne metoden
    date = request.POST['date']
    print(request.POST['id'])
    e = Event.objects.get(pk=request.POST['id'])
    e.updateEvent(request.POST['title'], date, request.POST['description'])
    return None