from django.db import models

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