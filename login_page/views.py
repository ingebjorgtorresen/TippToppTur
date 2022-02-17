from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CustomUserCreationForm
from django.urls import reverse
from django.contrib import messages

from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.

def login_page(request):
    return HttpResponse("Dette kommer på siden")


def register(request):
    if request.method == "GET":
        return render(
            request, template_name='login_page/newuser.html',context=
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            User = form.save()
            login(request, User)
            messages.success(request, "Registration successful.")
            return redirect(reverse("minside"))
