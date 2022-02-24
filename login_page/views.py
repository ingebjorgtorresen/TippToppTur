from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
# Create your views here.

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
        return redirect("login_page")

def register(request):
    return HttpResponse("Hello")

def logout_b(request):
    logout(request)
    return redirect("home")
