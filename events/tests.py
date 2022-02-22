from django.test import TestCase

from events.models import Event
from brukere.models import Turgåere

class EventModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        #Set up model used by tests
        Turgåere.objects.create(by = "Trondheim", telefonnummer = "112", ferdighetsnivå = "nybegynner")
        bruker = Turgåere.objects.get(id=1)
        Event.objects.create(tittel = "Test event", dato = "2022-02-23", arrangør = bruker, beskrivelse = "en fin tur med gutta", bilde = None, synlig = True )
    
    def test_title_label(self):
        event = Event.objects.get(id=1)
        field_label = event._meta.get_field('tittel').verbose_name
        self.assertEqual(field_label, 'tittel')
    
    def test_host_label(self):
        event = Event.objects.get(id=1)
        field_label = event._meta.get_field('arrangør').verbose_name
        self.assertEqual(field_label, 'arrangør')

    def test_tittel_max_length(self):
        event = Event.objects.get(id=1)
        max = event._meta.get_field('tittel').max_length
        self.assertEqual(max, 255)

    def test_title_is_correct(self):
        #event = Event.objects.values("tittel")
        event = Event.objects.get(id=1)
        tittel = "Test event"
        self.assertEqual(event.tittel, tittel) 