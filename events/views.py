import datetime
import imp
from django.shortcuts import redirect, render

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
    'arrangør' : event,
    'dato' : event,
    'beskrivelse': event,
    'bilde' : event,
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
    'pk': event.pk,
    'points': event.points
               }
    return render(request, 'edit_event/edit_event_form.html', context)

def updateEvent(request):
    date = request.POST['date']
    e = Event.objects.get(pk=request.POST['primarykey'])
    e.updateEvent(request.POST['title'], date, request.POST['description'])
    return redirect("trips")

def upvote(request):
    id = request.GET.get('id', '0')
    event = Event.objects.get(pk=id)
    bruker = request.user
    if bruker.hasUpvote(event):
        print("Upvote")
        bruker.upvote(event)
        event.points +=1
        event.save()


    
    return redirect("trips")


def downvote(request):
    id = request.GET.get('id', '0')
    event = Event.objects.get(pk=id)
    bruker = request.user
    print("Downvote -1")

    if bruker.hasDownvote(event):
        print("Downvote")
        bruker.downvote(event)
        event.points -= 1
        event.save()



    return redirect("trips")
#
 #def hasUpvote(self, event):
#        upvote = UpvotePoints.objects.filter(user_pk = self, event_pk = event)
##        #points =
  #      return False
