import django
from django.shortcuts import render

# Create your views here.
def home(request):
    user = request.user
    user_auth = user.is_authenticated
    context = {'user': user_auth, "name": user.username, "view": True}
    return render(request, 'landing_page/home.html', context)

