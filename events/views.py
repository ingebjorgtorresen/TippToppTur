from django.shortcuts import render

# Create your views here.
def trips(request):
    return render(request, 'landing_page/trips.html')