from django.test import TestCase
from brukere.models import *
from events.models import Event

# Create your tests here.

class registerTestCase(TestCase):
    def testRegister(self):
        turgåer = Turgåere.objects.create(username="Test", password="password12321")
        event = Event.objects.create(tittel="test", arrangør=turgåer, beskrivelse="test", dato="2022-02-17")
        turgåer.register(event)
        self.assertEqual(User_registration.objects.filter(user_pk=turgåer, event_pk=event).exists(), True)

    def testErrorHandling(self):
        turgåer = Turgåere.objects.create(username="Test", password="password12321")
        event = Event.objects.create(tittel="test", arrangør=turgåer, beskrivelse="test", dato="2022-02-17")
        self.assertEqual(turgåer.register(event), True)
        self.assertEqual(turgåer.register(event), False)
        self.assertEqual(turgåer.unRegister(event), True)
        self.assertEqual(turgåer.unRegister(event), False)
        self.assertEqual(User_registration.objects.filter(user_pk=turgåer, event_pk=event).exists(), False)
