from django.shortcuts import render
from .models import Event

# Create your views here.
def trips(request):
    return render(request, 'landing_page/trips.html')

def tripstest(request):
    event = Event.objects.all()
    context = {'tittel': event,
    'beskrivelse': event}
    return render(request, 'landing_page/trips.html', context)