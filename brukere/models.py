from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.db.models.signals import *


class Turgåere(AbstractUser):

    city = models.CharField(max_length=100)
    test = models.TextField(blank=True)

    def __str__(self):
        return '{}'.format(self.city)
