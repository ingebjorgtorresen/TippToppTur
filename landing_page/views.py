import django
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    user = request.user
    user_auth = user.is_authenticated
    context = {'user': user_auth, "name": user.username}
    return render(request, 'landing_page/home.html', context)

def trips(request):
    user = request.user
    user_auth = user.is_authenticated
    context = {'user': user_auth, "name": user.username}
    return render(request, 'landing_page/trips.html', context)