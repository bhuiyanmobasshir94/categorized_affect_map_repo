from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
from area.models import Area

class Location(models.Model):
    class Meta:
        verbose_name_plural = "Locations"
    area = models.ForeignKey(Area,on_delete=models.CASCADE)
    location_name = models.CharField(max_length=300)
    location_lat = models.FloatField(default=0.0)
    location_lon = models.FloatField(default=0.0)
    location_pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.location_name