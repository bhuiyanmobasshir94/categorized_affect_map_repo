from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
from location.models import Location

class Weather(models.Model):
    class Meta:
        verbose_name_plural = "weathers"
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    weather_main = models.CharField(max_length=100)
    weather_desc = models.CharField(max_length=200)
    weather_temp = models.FloatField(default=0.0)
    weather_pressure = models.IntegerField(default=0)
    weather_humidity = models.IntegerField(default=0)
    weather_temp_min = models.FloatField(default=0.0)
    weather_temp_max = models.FloatField(default=0.0)
    wind_speed = models.IntegerField(default=0)
    wind_degree = models.IntegerField(default=0)
    weather_datetime = models.IntegerField(default=0)
    clouds_all = models.IntegerField(default=0)
    sys_sunrise = models.IntegerField(default=0)
    sys_sunset = models.IntegerField(default=0)
    weather_pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.location + "_" + self.weather_datetime