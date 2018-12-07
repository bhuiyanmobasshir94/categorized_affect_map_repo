from django.db import models
from django.utils import timezone
import datetime

# Create your models here.


class Area(models.Model):
    class Meta:
        verbose_name_plural = "areas"
    area_name = models.CharField(max_length=300)
    area_lat = models.FloatField(default=0.0)
    area_lon = models.FloatField(default=0.0)
    area_pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.area_name