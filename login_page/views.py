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
    return render(request, "login_page/newuser2.html")

def register_user(request):
    username = request.POST["username"]
    password = request.POST["password"]
    password2 = request.POST["password2"]
    navn = request.POST['navn']
    epost = request.POST['mail']

    if len(username) > 3:
        request.session["error"]  =  "Brukernavnet ditt må være lenger enn 3 bokstaver."
        return redirect("register")
   

    for a in username:
        if "!@#$%^&*()+?=,<>/".__contains__(a):
            request.session["error"] = "Brukernavnet ditt kan ikke inneholde disse symboler."
            return redirect("register")

    if " " in username:
        request.session["error"] = "Brukernavnet ditt kan ikke inneholde disse symboler."
        return redirect("register")

    noe = Turgåere.objects.filter(username=username)
    if (noe):
        return redirect("register")
    
    if (password != password2):
        return redirect("register")



    user = Turgåere(username=username, password=make_password(password))
    user.save()

    #new_user = Turgåere.objects.get_or_create(username=username,is_staff = False)
    #new_user.set_password(password)
    #new_user.save()
    
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect("home")
    else:
        return redirect("register")
    
