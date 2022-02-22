from django.shortcuts import redirect, render
from django.http import HttpResponse
from events.models import Event
# Create your views here.

def event_form(request):
    return render(request, 'event_form/event_form.html')

def new_event(request):
    e = Event(tittel=request.POST['title'], dato=request.POST['date'], beskrivelse=request.POST['description'])
    e.save()
    return redirect("trips")