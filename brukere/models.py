import datetime
from datetime import date
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


# Create your models here.
from django.db.models.signals import *

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


class Turgåere(AbstractUser):
    ##PROFILBILDE funker kanskje ikke helt enda :)
    profilbilde = models.ImageField(upload_to='static/uploads/profilbilder/',
                                    default='placeholder.jpg')
    by = models.CharField(choices=citychoices,
                          max_length=20, blank=False, default=" ")
    telefonnummer = models.CharField(max_length=12, blank=False, default='')
    ferdighetsnivå = models.CharField(choices=experience, blank=False, max_length=20, default=" ")
    fødselsdato = models.DateField(verbose_name='Fødselsdato', blank=False)

    def fullName(self):
        return self.first_name + " " + self.last_name

    ##Metoden tar inn et event objekt som argument
    def register(self, event):
        if not self.isRegistered(event):
            registration = User_registration(user_pk=self, event_pk=event)
            registration.save()
        else:
            return False
        return True

    def unRegister(self, event):
        if self.isRegistered(event):
            registration = User_registration.objects.filter(user_pk=self, event_pk=event)
            registration.delete()
        else:
            return False
        return True
    
    def isRegistered(self, event):
        registration = User_registration.objects.filter(user_pk=self, event_pk=event)
        return registration.exists()

    def __str__(self):
        return '{}'.format(self.username)

class User_registration(models.Model):
    user_pk = models.ForeignKey(Turgåere, on_delete=models.CASCADE)
    event_pk = models.ForeignKey('events.Event', on_delete=models.CASCADE)

    def __str__(self):
        return '{}, {}'.format(self.user_pk, self.event_pk.pk)
