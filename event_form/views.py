import datetime


from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.utils import timezone
from django.utils.dateparse import parse_date
from django.utils.timezone import *

import brukere.models
from events.models import Event, validate_date_bool
from brukere import *
# Create your views here.

def event_form(request):
    datoidag = datetime.date.today().__str__()
    context = {'datoidag':datoidag}
    return render(request, 'event_form/event_form.html',context)

def new_event(request):
    date = request.POST['date']
    date_today = datetime.date.today()
    date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
    print(date < date_today)
    if(date < date_today):
        return redirect('event_form')

    e = Event(tittel=request.POST['title'],
              dato=date,
              beskrivelse=request.POST['description'],
              arrangør=request.user.get_full_name())
    e.save()
    return redirect("trips")