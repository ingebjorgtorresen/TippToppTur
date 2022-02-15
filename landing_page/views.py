import django
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'landing_page/home.html')

def trips(request):
    return render(request, 'landing_page/trips.html')