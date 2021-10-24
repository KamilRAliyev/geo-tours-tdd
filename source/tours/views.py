from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404
from tours import models
from django.core.serializers import serialize


# Create your views here.
def tour_details(request, pk):
    tour = models.Tour.objects.get(pk=pk)
    data = serialize("json", [tour], fields=('name', 'description', 'price', 'duration', 'city', 'rating'))
    return HttpResponse(data, content_type="application/json")
