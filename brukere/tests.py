from django.test import TestCase
from brukere.models import *
from events.models import Event

# Create your tests here.

class registerTestCase(TestCase):
    def testRegister(self):
        turgåer = Turgåere.objects.create(username="Test", password="password12321")
        event = Event.objects.create(tittel="test", arrangør=turgåer, beskrivelse="test", dato="2022-02-17")
        User_registration.objects.create(user_pk=turgåer, event_pk=event)
        self.assertAlmostEqual(User_registration.objects.filter(user_pk=turgåer, event_pk=event).exists(), True)
