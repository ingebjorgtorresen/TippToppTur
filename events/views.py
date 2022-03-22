import datetime
from django.shortcuts import redirect, render
from django.db.models import F, Count
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
    søkenavn = request.GET['navn']
    sorter = request.GET['sorter']
    vanskelighetsgrad = request.GET['vanskelighetsgrad']
    utstyr = request.GET['utstyr']
    event = Event.objects.all()
    if søkenavn != '':
        event = event.filter(tittel__contains = søkenavn)
    if vanskelighetsgrad != 'Alle':
        event = event.filter(vanskelighetsgrad = vanskelighetsgrad)
    if utstyr != 'Alle':
        if utstyr == 'on':
            event = event.exclude(utstyr = '')
        elif utstyr == 'off':
            event = event.filter(utstyr = '')
    if sorter == 'dfa':
        event = event.order_by('dato')
    elif sorter == 'dsa':
        event = event.order_by('-dato')
    elif sorter == 'llk':
        event = event.order_by(F('lengde').desc(nulls_last=True))
    elif sorter == 'lkl':
        event = event.order_by(F('lengde').asc(nulls_last=True))
    else:
        event = event.annotate(count = Count('user_registration'))
        if sorter == 'phl':
            event = event.order_by('-count')
        elif sorter == 'plh':
            event = event.order_by('count')

    context = {'tittel': event,
    'arrangør' : event,
    'dato' : event,
    'beskrivelse': event,
    'bilde' : event,
    'user': user.is_authenticated,
    'name': user.username,
    'view': True}
    return render(request, 'landing_page/trips.html', context)