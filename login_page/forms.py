from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from brukere.models import Turgåere

from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.

citychoices = (
    ('trondheim', 'Trondheim'),
    ('bergen', 'Bergen'),
    ('oslo', 'Oslo'),
    ('tromsø', 'Tromsø')
)
experience = (
    ('nybegynner', 'Nybegynner'),
    ('erfaren', 'Erfaren'),
    ('ekspert', 'Ekspert')
)


class CustomUserCreationForm(UserCreationForm):

    email = forms.EmailField(required=True)
    telefonnummer = forms.CharField(required=True)
    by = forms.CharField(required=True)
    ferdighetsnivå = forms.CharField(required=True)
    profilbilde = forms.ImageField(required=False)

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email", "by", "telefonnummer", "ferdighetsnivå","profilbilde")

    def save(self, commit=True):
        User = super(CustomUserCreationForm, self).save(commit=False)
        User.email = self.cleaned_data['email']
        User.telefonnummer = self.cleaned_data['telefonnummer']
        User.by = self.cleaned_data['by']
        User.ferdighetsnivå = self.cleaned_data['ferdighetsnivå']
        User.profilbilde = self.cleaned_data['profilbilde']

        if commit:
            Turgåere.save()
        return Turgåere
