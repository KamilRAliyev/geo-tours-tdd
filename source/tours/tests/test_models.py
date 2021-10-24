from django.test import TestCase
from mixer.backend.django import mixer
from tours import models

class TestTour(TestCase):
    def test_model_creation(self):
        obj = mixer.blend(models.Tour)
        self.assertEqual(obj.pk, 1, "Tour is not creating") 
    
class TestTourOrder(TestCase):
    def test_model_creation(self):
        tour = mixer.blend(models.Tour, name="TestTour1", price=21.00)
        tourOrder = mixer.blend(models.TourOrder, tour=tour, full_name="test_persona")
        self.assertEqual(tourOrder.tour, tour)