import datetime
from django.test import TestCase
from .models import Event

# Create your tests here.
class test_event(TestCase):
    def test_make_event(self):
        time = datetime.datetime.now()
        event = Event(tittel="Tur", dato=time, beskrivelse="Hello")
        self.assertEqual(event.tittel, "Tur")
        self.assertEqual(event.dato, time)
        self.assertEqual(event.beskrivelse,"Hello")