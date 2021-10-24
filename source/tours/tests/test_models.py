from django.test import TestCase
from mixer.backend.django import mixer
from tours import models

class TestTour(TestCase):
    def test_model_creation(self):
        obj = mixer.blend(models.Tour)
        self.assertEqual(obj.pk, 1, "Tour is not creating") 