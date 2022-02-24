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

    ##Metoden tar inn et event objekt som argument
    @classmethod
    def register(cls, event):
        registration = User_registration(user_pk=cls.pk, event_pk=event.pk)
        registration.save()
        return None

    @classmethod
    def unRegister(cls, event):
        registration = User_registration.objects.filter(user_pk=cls.pk, event_pk=event.pk)
        registration.delete()
        return None
    
    @classmethod
    def isRegistered(cls, event):
        registration = User_registration.objects.filter(user_pk=cls.pk, event_pk=event.pk)
        return registration.exists()

    def __str__(self):
        return '{}'.format(self.username)

class User_registration(models.Model):
    user_pk = models.ForeignKey(Turgåere, on_delete=models.CASCADE)
    event_pk = models.ForeignKey('events.Event', on_delete=models.CASCADE)