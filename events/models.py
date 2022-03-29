


from datetime import timezone
from email.policy import default
from pyexpat import model
from random import choices
from secrets import choice
from sqlite3 import DateFromTicks
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import *
from brukere.models import Turgåere
from datetime import datetime
from django.utils import timezone


# Create your models here.

def validate_date(dato):
    if dato < timezone.now():
        raise ValidationError("Dato kan ikke være tilbake i tid")

def validate_date_bool(dato):
    return dato < timezone.now()

class Event(models.Model):
    tittel = models.CharField(
        max_length=255,
        blank=False,
    )
    arrangør = models.CharField(max_length=40,default='')
    arrangør_username = models.CharField(max_length=50,default='')
        #ForeignKey(Turgåere, on_delete=models.CASCADE, blank=False)
    dato = models.DateTimeField(null=True,blank=False, validators=[validate_date])
    beskrivelse = models.TextField(blank=False, default='')
    bilde = models.ImageField(upload_to='static/uploads/eventimages/', blank=True)
    #Klasse som definerer valg for vankselighetsgrad
    class Grad(models.TextChoices):
        ENKEL = 'Enkel'
        MIDDELS = 'Middels'
        KREVENDE = 'Krevende'
        EKSTRA_KREVENDE = 'Ekstra Krevende'

    vanskelighetsgrad = models.CharField(
        max_length = 15,
        choices = Grad.choices,
        default= Grad.ENKEL
    )
    terreng = models.CharField(max_length=40, default='', null=True)
    lengde = models.IntegerField(null=True, default=None)
    utstyr = models.CharField(max_length=40, default='', null=True)
    bilde = models.ImageField(upload_to='static/uploads/', blank=True)
    synlig = models.BooleanField(default=True)
    seriøsaktør = models.BooleanField(default=False)
    pris = models.IntegerField(default=0)
    destinasjon = models.CharField(max_length=80,default='')

    def deleteEvent(self):
        event = Event.objects.filter(pk = self.pk)
        event.delete()
        return True

    def updateEvent(self, tittel, dato, beskrivelse):
        event = Event.objects.filter(pk = self.pk)
        event.update(tittel = tittel, dato = dato, beskrivelse = beskrivelse)
        return True

    def hasHappened(self):
        print('test')
        print(self.dato < timezone.now())
        return self.dato < timezone.now()

    def __str__(self):
        return '{}, Dato: {}'.format(self.tittel, self.dato)

    def labels_vankselighetsgrad(self):
        return [label for value, label in self.fields['vanskelighetsgrad'].choices if value in self['vanskelighetsgrad'].value()]
