import datetime
from django.test import TestCase
from .models import Event
from events import models
from events.models import Event
from brukere.models import Turgåere

class EventModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        #Set up model used by tests
        Turgåere.objects.create(by = "Trondheim", telefonnummer = "112", ferdighetsnivå = "nybegynner")
        bruker = Turgåere.objects.get(id=1)
        Event.objects.create(tittel = "Test event", dato = "2023-10-23", arrangør = bruker, beskrivelse = "en fin tur med gutta", bilde = None, synlig = True )
        Event.objects.create(tittel = "Test seriøs event", dato = "2023-10-23", arrangør="Test", beskrivelse="Hei",bilde=None, synlig=True, seriøsaktør=True, pris=105)
    
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

    def test_date_is_correct(self):
        event = Event.objects.get(id=1)
        date = datetime.datetime(2023, 10, 22, 22, 0, tzinfo=datetime.timezone.utc)
        self.assertEqual(event.dato, date)

    def test_date_not_too_old(self):
        event = Event.objects.get(id=1)
        date = datetime.datetime.today()
        self.assertTrue(event.dato > datetime.datetime(date.year, date.month, date.day, date.hour, date.minute, tzinfo=datetime.timezone.utc))

    def test_descrition_is_correct(self):
        event = Event.objects.get(id=1)
        description = "en fin tur med gutta"
        self.assertEqual(event.beskrivelse, description)
    
    def test_seriøst_event(self):
        event = Event.objects.get(id=2)
        self.assertEqual(event.pris, 105)
        self.assertTrue(event.seriøsaktør)

# Create your tests here.
class test_event(TestCase):
    def test_make_event(self):
        time = datetime.datetime.now()
        event = Event(tittel="Tur", dato=time, beskrivelse="Hello")
        self.assertEqual(event.tittel, "Tur")
        self.assertEqual(event.dato, time)
        self.assertEqual(event.beskrivelse,"Hello")

    def test_delete_event(self):
        time = datetime.datetime.now()
        event = Event(tittel="Test", dato=time, beskrivelse="Hello")
        event.save()
        self.assertEqual(Event.objects.filter(tittel="Test").exists(), True)
        event.deleteEvent()
        self.assertEqual(Event.objects.filter(tittel="Test").exists(), False)

    def test_update_event(self):
        time = datetime.datetime.now()
        event = Event(tittel="Test", dato=time, beskrivelse="Hello")
        event.save()
        event.updateEvent("Test2", time, "Is it me you're looking for")
        self.assertEqual(Event.objects.get(pk = event.pk).tittel, "Test2")
        self.assertEqual(Event.objects.get(pk = event.pk).beskrivelse, "Is it me you're looking for")
