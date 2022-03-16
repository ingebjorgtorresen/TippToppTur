from datetime import date, datetime

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
    datotime = datetime.now()
    error = request.session.pop("error", None)
    if error is None:
        error = ""

    context = {'datoidag': datotime,
               'error': error,
               }
    return render(request, 'event_form/event_form.html', context)


def new_event(request):
    datoen1 = request.POST['date']
    datoen = datoen1.split('T')
    # ['2022-03-01', '15:38']
    datoenher = datetime.strptime(datoen[0], '%Y-%m-%d').date()
    # 2022-03-01 -Date objekt
    date_today = date.today()
    # 2022-03-15
    timenow = (datetime.strptime(datoen[1], '%H:%M')).time()
    # 15:38:00
    timetoday = (datetime.now().time()).strftime('%H:%M:%S')
    timetoday = datetime.strptime(timetoday, '%H:%M:%S')
    timetoday = timetoday.time()
    # 09:03:34

    if not (datoenher > date_today):
        request.session["error"] = "Du må velge dato frem i tid!"
        return redirect('event_form')

        # Frem i tid
    if datoenher == date_today:
        if timetoday > timenow:
            request.session["error"] = "Du må velge dato frem i tid!"
            return redirect('event_form')

    e = Event(tittel=request.POST['title'],
              dato=datoen1,
              beskrivelse=request.POST['description'],
              arrangør=request.user.get_full_name())
    e.save()
    return redirect("trips")
