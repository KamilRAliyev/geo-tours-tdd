from django.test import TestCase
from tours import models
from mixer.backend.django import mixer
from django.core.serializers import serialize
from http import HTTPStatus
from django.utils.encoding import force_text

class TestTourDetails(TestCase):
    def test_tour_get(self):
        obj = mixer.blend(models.Tour, name='test1')
        data = serialize("json", [obj], fields=('name', 'description', 'price', 'duration', 'city', 'rating'))
        response = self.client.get(f'/tours/{obj.pk}')

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(force_text(response.content), data )
