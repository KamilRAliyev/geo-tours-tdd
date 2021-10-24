from django.db import models
from django.db.models.base import Model

# Create your models here.
class Tour(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=400, blank=False, null=False)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=False, null=False)
    duration = models.IntegerField(blank=False, null=False)
    city = models.CharField(max_length=200)
    rating = models.IntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Tour'
        verbose_name_plural = 'Tours'

class TourOrder(models.Model):
    full_name = models.CharField(max_length=100, blank=False, null=False)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='Tours')
    comment = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        verbose_name = 'Tour Order'
        verbose_name_plural = 'Tour Orders'