from django.http import HttpResponse
from django.shortcuts import redirect, render
from events.models import Event
from brukere.models import Turgåere, User_registration
import datetime
from django.utils import timezone


# Create your views here.

def event_page(request):
    id = request.GET.get('id', '0')
    try:
        event = Event.objects.get(pk=id)
        dateToday = timezone.now()
        eventdate = event.dato
        if (eventdate >= dateToday):
            stillAvailable = True
        else:
            stillAvailable = False

        registrert = User_registration.objects.filter(event_pk=id)
        context = {
            'exists': True,
            'title': event.tittel,
            'date': eventdate,
            'arrangør': event.arrangør,
            'arrangør_username': event.arrangør_username,
            'destination': event.destinasjon,
            'description': event.beskrivelse,
            'utstyr': event.utstyr,
            'grad': event.vanskelighetsgrad,
            'terreng': event.terreng,
            'lengde': event.lengde,
            'id': id,
            'påmeldt': request.user.isRegistered(Event.objects.get(pk=id)),
            'registrert': registrert,
            'stillAvailable': stillAvailable,
        }
    except AttributeError:
        context = {'exists': True,
                   'title': event.tittel,
                   'date': event.dato,
                   'arrangør': event.arrangør,
                   'destination': event.destinasjon,
                   'description': event.beskrivelse,
                   }
    except Event.DoesNotExist:
        context = {
            'exists': False,
        }
        return render(request, 'event_page/event_page.html', context)
    return render(request, 'event_page/event_page.html', context)


def register_event(request):
    id = request.GET.get('id', '0')
    event = Event.objects.get(pk=id)
    if not request.user.isRegistered(event):
        request.user.register(event)
    else:
        request.user.unRegister(event)

    link = "../event_page/?id="
    link += id
    return redirect(link)
