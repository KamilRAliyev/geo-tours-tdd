from django.http.response import HttpResponse
from django.test import TestCase
from tours import models
from mixer.backend.django import mixer
from django.core.serializers import serialize
from http import HTTPStatus
from django.utils.encoding import force_text
from time import sleep

class TestTourDetails(TestCase):
    def test_tour_get(self):
        obj = mixer.blend(models.Tour, name='test1')
        data = serialize("json", [obj], fields=('name', 'description', 'price', 'duration', 'city', 'rating'))
        response = self.client.get(f'/tours/{obj.pk}')

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(force_text(response.content), data )

class TestTourList(TestCase):
    def test_tours_get(self):
        obj = mixer.blend(models.Tour, name='test2')
        sleep(2)
        obj1 = mixer.blend(models.Tour, name='test3')
        etalon = models.Tour.objects.all().order_by('created_at').reverse()
        data = serialize("json", etalon)
        response = self.client.get(f'/tours/')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(force_text(response.content), data )

class TestTourOrder(TestCase):
    def test_ordering_tour(self):
        tour = mixer.blend(models.Tour, name='test2')
        response = self.client.post(f"/tours/{tour.pk}/order", data={
           'full_name':"Persona1",
           'comment': "My mail: kamil@gmail.com" 
        })
        
        
        self.assertEqual(models.TourOrder.objects.get(tour=tour).tour, tour)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

