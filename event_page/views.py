from django.shortcuts import render
from events.models import Event

# Create your views here.

def event_page(request):
    try:
        event = Event.objects.get(pk=1)
        context = {
            'title': event.tittel,
            'date': event.dato,
            'destination': "Kommer senere",
            'description': event.beskrivelse,
        }
    except Event.DoesNotExist:
        return render(request, 'event_page/event_page.html', context)
    return render(request, 'event_page/event_page.html', context)