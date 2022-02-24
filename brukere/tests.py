from django.test import TestCase
from brukere.models import *
from events.models import Event

# Create your tests here.

class registerTestCase(TestCase):
    def setUp(self):
        turgåer = Turgåere.objects.create(username="Test", password="password12321")
        Event.objects.create(tittel="test", arrangør=turgåer, beskrivelse="test", dato="2022-02-17")
