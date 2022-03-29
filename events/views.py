import datetime
import imp
from django.shortcuts import redirect, render
from django.db.models import F, Count

from brukere.models import UpvotePoints

from .models import Event
from brukere.models import Turgåere



# Create your views here.
def trips(request):
    return render(request, 'landing_page/trips.html')


def tripstest(request):
    user = request.user
    event = Event.objects.all()
    context = {'tittel': event,
               'arrangør': event,
               'dato': event,
               'beskrivelse': event,
               'bilde': event,
               'user': user.is_authenticated,
               'name': user.username,
               'view': True,
               'points': event,
               }
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
    dato = dato1.split(' ')  # ['2111-12-12', '20:22:00+00:00']
    dato2 = dato[1].split(':')
    del dato2[3]
    del dato2[2]
    dato2[0] = str(int(dato2[0]) + 1)
    dato2 = ':'.join(dato2)
    dato[1] = dato2
    dato = 'T'.join(dato)
    context = {'tittel': event.tittel,
               'dato': dato,
               'beskrivelse': event.beskrivelse,
               'pk': event.pk,
               'bilde': event.bilde,
               'points': event.points }
    return render(request, 'edit_event/edit_event_form.html', context)


# return render(request, 'edit_event/edit_event_form.html', context)


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

def totalPoints(request, pk):
    votes = UpvotePoints.objects.all()
    votes = votes.filter(event_pk=pk)
    up = votes.filter(points=1)
    down = votes.filter(points=-1)
    return int(len(up) - len(down))


def canUpvote(request):
    id = request.GET.get('id', '0')
    event = Event.objects.get(pk=id)
    brukertest = Turgåere.objects.filter(username=request.user).get()
    allevotes = brukertest.canVote(event)
    up = allevotes.filter(points=1)

    if len(up) != 0:
        return True


def canDownvote(request):
    id = request.GET.get('id', '0')
    event = Event.objects.get(pk=id)
    brukertest = Turgåere.objects.filter(username=request.user).get()
    allevotes = brukertest.canVote(event)
    down = allevotes.filter(points=-1)

    if len(down) != 0:
        return True


def upvote(request):
    id = request.GET.get('id', '0')
    event = Event.objects.get(pk=id)
    brukertest = Turgåere.objects.filter(username=request.user).get()

    allevotes = brukertest.canVote(event)
    up = allevotes.filter(points=1)
    down = allevotes.filter(points=-1)

    if len(up) == 0 and len(down) == 0:
        # Ingen upvotes eller downvotes
        brukertest.upvote(event)
        event.points += 1
        event.save()

    if len(down) != 0:
        # Allerede downvota, upvoter og sletter gamle downvote
        brukertest.upvote(event)
        # Må opp 2 siden vi er minus 1
        event.points += 2
        event.save()
        down.delete()

    if len(up) != 0:
        #Allered upvota, fjerner upvoten 
        brukertest.upvote(event)
        event.points -= 1
        event.save()
        up.delete()

    return redirect("trips")


def downvote(request):
    id = request.GET.get('id', '0')
    event = Event.objects.get(pk=id)
    brukertest = Turgåere.objects.filter(username=request.user).get()

    allevotes = brukertest.canVote(event)
    up = allevotes.filter(points=1)
    down = allevotes.filter(points=-1)

    if len(up) == 0 and len(down) == 0:
        # Ingen upvotes eller downvotes
        brukertest.downvote(event)
        event.points -= 1
        event.save()

    if len(up) != 0:
        # Allerede downvota, upvoter og sletter gamle downvote
        brukertest.downvote(event)
        # Må opp 2 siden vi er minus 1
        event.points -= 2
        event.save()
        up.delete()
    
    if len(down) != 0:
        #Allered downvota, fjerner downvoten
        brukertest.downvote(event)
        event.points += 1
        event.save()
        down.delete()
    return redirect("trips")
