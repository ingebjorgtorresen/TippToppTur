from django.shortcuts import render

# Create your views here.

def event_page(request):
    context = {
        'title': "tittel",
        'date': "dato",
        'destination': "destinasjon",
        'description': "beskrivelse",
    }
    return render(request, 'event_page/event_page.html', context)