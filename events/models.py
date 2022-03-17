

from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import *
from brukere.models import Turgåere


# Create your models here.

def validate_date(dato):
    if dato < timezone.now().date():
        raise ValidationError("Dato kan ikke være tilbake i tid")

def validate_date_bool(dato):
    return dato < timezone.now().date()

class Event(models.Model):
    tittel = models.CharField(
        max_length=255,
        blank=False,
    )
    arrangør = models.CharField(max_length=40,default='')
        #ForeignKey(Turgåere, on_delete=models.CASCADE, blank=False)
    dato = models.DateField(null=True,blank=False, validators=[validate_date])
    beskrivelse = models.TextField(blank=False, default='')
    bilde = models.ImageField(upload_to='static/uploads/', blank=True)
    synlig = models.BooleanField(default=True)

    def __str__(self):
        return '{}, Dato: {}'.format(self.tittel, self.dato)


