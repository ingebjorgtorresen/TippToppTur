import datetime

from django.http import HttpResponse
from .forms import CustomUserCreationForm
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from brukere.models import Turgåere
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
# Create your views here.
User = get_user_model()
# Create your views here.

def register_serious(request):
    error = request.session.pop("error", None)
    if error is None:
        error = ""
    context = {'error': error}
    return render(request, "login_page/serioususerregister.html", context)

def register_serious_user(request):
    username = request.POST["username"]
    password = request.POST["password"]
    password2 = request.POST["password2"]
    name = request.POST['navn']
    epost = request.POST['mail']

    # Test username
    if len(username) < 3:
        request.session["error"] = "Brukernavnet ditt må være lenger enn 3 bokstaver."
        return redirect("register_serious")

    for a in username:
        if "!@#$%^&*()+?=,<>/".__contains__(a):
            request.session["error"] = "Brukernavnet ditt kan ikke inneholde symboler."
            return redirect("register_serious")

    if " " in username:
        request.session["error"] = "Brukernavnet ditt kan ikke inneholde space."
        return redirect("register_serious")

    noe = Turgåere.objects.filter(username=username)
    if (noe):
        request.session["error"] = "Brukernavn eksisterer allerede!!"
        return redirect("register_serious")

    # Test name
    if name is None or name == " ":
        request.session["error"] = "Må spesifisere navne!!"
        return redirect("register_serious")

    # Test passwords
    if (password is None or len(password) < 8):
        request.session["error"] = "Password is too short!!"
        return redirect("register_serious")

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
        if ("!#$%&'()*+,-./:;<=>?@[\]^_`{|}~".__contains__(a)):
            contains_symbol = True

    if not contains_upper:
        request.session["error"] = "Passordet må inneholde minst en stor bokstav!!"
        return redirect("register_serious")

    if not contains_lower:
        request.session["error"] = "Passordet må inneholde minst en liten bokstav!!"
        return redirect("register_serious")

    if not contains_symbol:
        request.session["error"] = "Passordet må inneholde minst ett symbol!!"
        return redirect("register_serious")

    if not contains_number:
        request.session["error"] = "Passordet må inneholde minst ett tall!!"
        return redirect("register_serious")

    if (password != password2):
        request.session["error"] = "Passordene må matche!!"
        return redirect("register_serious")

    if (len(names) <= 1):
        request.session["error"] = "Du må skrive fullt navn!!"
        return redirect('register')
    else:
        last_name = names[1]
        if len(names) >= 3:
            for x in names[2:]:
                last_name += (" " + x)

    user = Turgåere(username=username, password=make_password(password), email=epost, first_name=names[0],
                    last_name=last_name, seriøsaktør=True,fødselsdato=None)
    user.save()

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect("home")
    else:
        request.session["error"] = "Feil i databasen, kontakt systemansvarlig!!"
        return redirect("register_serious")

def register(request):
    error = request.session.pop("error", None)
    datoidag = (datetime.date.today()-datetime.timedelta(weeks=676)).__str__()
    if error is None:
        error = ""
    context = {'error': error,
               'datoidag' : datoidag,
               }
    return render(request, "login_page/newuser2.html", context)

def register_user(request):
    username = request.POST["username"]
    password = request.POST["password"]
    password2 = request.POST["password2"]
    name = request.POST['navn']
    epost = request.POST['mail']
    fødselsdato = request.POST.get('date', False)

    # Test username
    if len(username) < 3:
        request.session["error"]  =  "Brukernavnet ditt må være lenger enn 3 bokstaver."
        return redirect("register")
   
    for a in username:
        if "!@#$%^&*()+?=,<>/".__contains__(a):
            request.session["error"] = "Brukernavnet ditt kan ikke inneholde symboler."
            return redirect("register")

    if " " in username:
        request.session["error"] = "Brukernavnet ditt kan ikke inneholde space."
        return redirect("register")

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

    if (len(names)<=1):
        request.session["error"] = "Du må skrive fullt navn!!"
        return redirect('register')
    else:
        last_name = names[1]
        if len(names) >= 3:
            for x in names[2:]:
                last_name += (" " + x)

    user = Turgåere(username=username, password=make_password(password), email=epost, first_name=names[0], last_name=last_name, fødselsdato=fødselsdato)
    user.save()
    
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect("home")
    else:
        request.session["error"] = "Feil i databasen, kontakt systemansvarlig!!"
        return redirect("register")

def login_page(request):
    user = request.user
    user_auth = user.is_authenticated
    context = {'user': user_auth, "name": user.username, "view": False}
    return render(request, 'login_page/login_page.html', context)

def login_b(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect("trips")
    else:
        messages.error(request, "Feil brukernavn eller passord!")
        return redirect("login_page")

def logout_b(request):
    logout(request)
    return redirect("home")
