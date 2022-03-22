import datetime
from django.shortcuts import redirect, render
from .models import Event

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
    dato1 = str(event.dato)
    dato = dato1.split(' ') #['2111-12-12', '20:22:00+00:00']
    dato2 = dato[1].split(':')
    del dato2[3]
    del dato2[2]
    dato2[0] = str(int(dato2[0])+1)
    dato2 = ':'.join(dato2)
    dato[1] = dato2
    dato = 'T'.join(dato)
    print(dato)
    context = {'tittel': event.tittel,
    'dato' : dato, 
    'beskrivelse': event.beskrivelse,
    'pk': event.pk}
    return render(request, 'edit_event/edit_event_form.html', context)

def updateEvent(request):
    date = request.POST['date']
    e = Event.objects.get(pk=request.POST['primarykey'])
    e.updateEvent(request.POST['title'], date, request.POST['description'])
    return redirect("trips")

def search_results(request):
    user = request.user
    event = Event.objects.all()
    context = {'tittel': event,
    'arrangør' : event,
    'dato' : event,
    'beskrivelse': event,
    'bilde' : event,
    'user': user.is_authenticated,
    'name': user.username,
    'view': True,
    'søkenavn': request.GET['navn'],
    'sorter': request.GET['sorter'],
    'vanskelighetsgrad': request.GET['vanskelighetsgrad'],
    'utstyr': request.GET['utstyr']}
    return render(request, 'landing_page/trips.html', context)