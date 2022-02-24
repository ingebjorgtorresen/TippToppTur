from django.shortcuts import redirect, render
from django.http import HttpResponse

import brukere.models
from events.models import Event
from brukere import *
# Create your views here.

def event_form(request):
    return render(request, 'event_form/event_form.html')

def new_event(request):
    e = Event(tittel=request.POST['title'], dato=request.POST['date'], beskrivelse=request.POST['description'],arrangør=request.user.get_full_name())
    e.save()
    return redirect("trips")