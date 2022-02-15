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
    profilbilde = models.ImageField(upload_to='static/uploads/profilbilder/',
                                    default='static/uploads/profilbilder/placeholder.jpg')
    by = models.CharField(choices=citychoices,
                          max_length=20, blank=False, default=" ")
    telefonnummer = models.CharField(max_length=12, blank=False, default='')
    ferdighetsnivå = models.CharField(choices=experience, blank=False, max_length=20, default=" ")

    def __str__(self):
        return '{}'.format(self.username)
