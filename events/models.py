from django.db import models
from django.contrib.auth.models import *


# Create your models here.

class Event(models.Model):
    tittel = models.CharField(
        max_length=255,
        blank=False,
    )
    arrangør = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, default=None)
    dato = models.DateField()
    beskrivelse = models.TextField(blank=False, default='')
    bilde = models.ImageField(upload_to='static/uploads/', blank=True)
    synlig = models.BooleanField(default=True)

    def __str__(self):
        return '{}, Dato: {}'.format(self.tittel, self.dato)

