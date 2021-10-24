from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from tours import models
from django.core.serializers import serialize


# Create your views here.
def tour_details(request, pk):
    tour = models.Tour.objects.get(pk=pk)
    data = serialize("json", [tour], fields=('name', 'description', 'price', 'duration', 'city', 'rating'))
    return HttpResponse(data, content_type="application/json")

def tours(request):
    tours = models.Tour.objects.all().order_by('created_at').reverse()
    data = serialize("json", tours)
    return HttpResponse(data, content_type="application/json")

def tour_order(request,pk):
    if request.method=='POST':
        full_name = request.POST.get('full_name')
        comment = request.POST.get('comment')
        tour = models.Tour.objects.get(pk=pk)
        order = models.TourOrder()
        order.full_name = full_name
        order.tour =tour
        order.comment = comment
        order.save()
        return redirect(f'/tour/{tour.pk}/')