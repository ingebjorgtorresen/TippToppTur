from codecs import register_error
from django.contrib.auth import login, authenticate
from django.forms import PasswordInput
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CustomUserCreationForm
from django.urls import reverse
from django.contrib import messages

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from brukere.models import Turgåere
User = get_user_model()
# Create your views here.

def login_page(request):
    return HttpResponse("Dette kommer på siden")


def register(request):
    error = request.session.pop("error", None)
    if error is None:
        error = ""
    context = {'error': error}
    return render(request, "login_page/newuser2.html", context)

def register_user(request):
    username = request.POST["username"]
    password = request.POST["password"]
    password2 = request.POST["password2"]
    name = request.POST['navn']
    epost = request.POST['mail']

    noe = Turgåere.objects.filter(username=username)
    if (noe):
        request.session["error"] = "Brukernavn eksisterer allerede!!"
        return redirect("register")

    # Test name
    if name is None or name == " ":
        request.session["error"] = "Må spesifisere navne!!"
        return redirect("register")

    names = name.split(" ")
    if len(name) <= 1:
        request.session["error"] = "Må spesifisere fornavn og etternavn!!"
        return redirect("register")

    for name in names:
        if len(name) < 1:
            request.session["error"] = "Ugyldig format!!"
            return redirect("register")

    # Test passwords
    if (password is None or len(password) < 8):
        request.session["error"] = "Password is too short!!"
        return redirect("register")

    contains_lower = False
    contains_upper = False
    contains_number = False
    contains_symbol = False
    for a in password:
        if (a.islower()):
            contains_lower = True
        if (a.isupper()):
            contains_upper = True
        if (a.isnumeric()):
            contains_number = True
        if ( "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~".__contains__(a)):
            contains_symbol = True
    
    if not contains_upper:
        request.session["error"] = "Passordet må inneholde minst en stor bokstav!!"
        return redirect("register")

    if not contains_lower:
        request.session["error"] = "Passordet må inneholde minst en liten bokstav!!"
        return redirect("register")
    
    if not contains_symbol:
        request.session["error"] = "Passordet må inneholde minst ett symbol!!"
        return redirect("register")

    if not contains_number:
        request.session["error"] = "Passordet må inneholde minst ett tall!!"
        return redirect("register")

    if (password != password2):
        request.session["error"] = "Passordene må matche!!"
        return redirect("register")
    
    user = Turgåere(username=username, password=make_password(password))
    user.save()
    
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect("home")
    else:
        request.session["error"] = "Feil i databasen, kontakt systemansvarlig!!"
        return redirect("register")
    
