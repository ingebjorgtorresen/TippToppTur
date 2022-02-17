from django.shortcuts import render

# Create your views here.

def event_page(request):
    return render(request, 'event_page/event_page.html')