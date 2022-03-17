

from pyexpat import model
from random import choices
from secrets import choice
from sqlite3 import DateFromTicks
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import *
from brukere.models import Turgåere


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
        #ForeignKey(Turgåere, on_delete=models.CASCADE, blank=False)
    dato = models.DateTimeField(null=True,blank=False, validators=[validate_date])
    beskrivelse = models.TextField(blank=False, default='')
    #Klasse som definerer valg for vankselighetsgrad 
    class Grad(models.TextChoices):
        ENKEL = 'E'
        MIDDELS = 'M'
        KREVENDE = 'K'
        EKSTRA_KREVENDE = 'EK'

    vanskelighetsgrad = models.CharField(
        max_length = 2,
        choices = Grad.choices,
        default= Grad.ENKEL
    )
    terreng = models.CharField(max_length=40, default='', null=True)
    lengde = models.IntegerField(null=True)
    bilde = models.ImageField(upload_to='static/uploads/', blank=True)
    synlig = models.BooleanField(default=True)

    def deleteEvent(self):
        event = Event.objects.filter(pk = self.pk)
        event.delete()
        return True

    def updateEvent(self, tittel, dato, beskrivelse):
        event = Event.objects.filter(pk = self.pk)
        event.update(tittel = tittel, dato = dato, beskrivelse = beskrivelse)
        return True

    def __str__(self):
        return '{}, Dato: {}'.format(self.tittel, self.dato)

    def labels_vankselighetsgrad(self):
        return [label for value, label in self.fields['vanskelighetsgrad'].choices if value in self['vanskelighetsgrad'].value()]
