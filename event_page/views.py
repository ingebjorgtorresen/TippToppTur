from django.http import HttpResponse
from django.shortcuts import render
from events.models import Event

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
        }
    except Event.DoesNotExist:
        context = {
            'exists': False,
        }
        return render(request, 'event_page/event_page.html', context)
    return render(request, 'event_page/event_page.html', context)

def register_event(request):
    id = request.GET.get('id', '0')
    print(id)
    print("Test")

    #return HttpResponse(id)