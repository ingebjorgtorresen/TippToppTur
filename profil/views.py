from django.shortcuts import redirect, render

# Create your views here.
def profil(request):
    user = request.user
    user_auth = user.is_authenticated
    context = {'user': user_auth, "name": user.username, "view": True}
    return render(request, 'profil/profil.html', context)

def editprofile(request):
    user = request.user
    user_auth = user.is_authenticated
    birthday = str(request.user.fødselsdato)
    context = {'user': user_auth, "name": user.username, "fullname": f'{user.first_name} {user.last_name}', "birthday": birthday, "view": True}
    return render(request, 'profil/editprofile.html', context)

def updateuser(request):
    user = request.user
    if not user.isSeriøsAktør():
        user.updateUser(request.POST['navn'], request.POST['mail'], request.POST['date'])
    else:
        user.updateSeriousUser(request.POST['navn'], request.POST['mail'])
    return redirect("profil")