from django.http import HttpResponse
from django.shortcuts import redirect, render
from events.models import Event
from brukere.models import Turgåere, User_registration

# Create your views here.

def event_page(request):
    id = request.GET.get('id', '0')
    try:
        event = Event.objects.get(pk=id)
        context = {
            'exists': True,
            'title': event.tittel,
            'date': event.dato,
            'arrangør': event.arrangør,
            'destination': "Kommer senere",
            'description': event.beskrivelse,
            'id' : id,
            'påmeldt': request.user.isRegistered(Event.objects.get(pk=id)),
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
        print("aaaaa")
        request.user.register(event)
    else:
        print("adwad")
        request.user.unRegister(event)
    
    link = "../event_page/?id="
    link += id
    return redirect(link)
        