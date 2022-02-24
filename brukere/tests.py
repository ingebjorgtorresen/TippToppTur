from django.test import TestCase

from brukere.models import Turgåere


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up model used by tests
        Turgåere.objects.create(by="Trondheim", telefonnummer="112", ferdighetsnivå="nybegynner")

    def test_city_is_correct(self):
        user = Turgåere.objects.get(id=1)
        city = "Trondheim"
        self.assertEqual(user.by, city)

    def test_city_max_length(self):
        user = Turgåere.objects.get(id=1)
        max = user._meta.get_field('by').max_length
        self.assertEqual(max, 20)

    def test_phonenumber_is_correct(self):
        user = Turgåere.objects.get(id=1)
        phonenumber = "112"
        self.assertEqual(user.telefonnummer, phonenumber)

    def test_phonenumber_max_length(self):
        user = Turgåere.objects.get(id=1)
        max = user._meta.get_field('telefonnummer').max_length
        self.assertEqual(max, 12)

    def test_skills_is_correct(self):
        user = Turgåere.objects.get(id=1)
        skills = "nybegynner"
        self.assertEqual(user.ferdighetsnivå, skills)

    def test_skills_max_length(self):
        user = Turgåere.objects.get(id=1)
        max = user._meta.get_field('ferdighetsnivå').max_length
        self.assertEqual(max, 20)
