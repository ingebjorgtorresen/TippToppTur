from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def event_form(request):
    return render(request, 'event_form.html')