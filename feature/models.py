from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

from category.models import Category

CHOICE = [(1,'Active'),(0,'Inactive')]

class Feature(models.Model):
    class Meta:
        verbose_name_plural = "features"
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    feature_name = models.CharField(max_length=300)
    feature_value = models.IntegerField(default=0)
    feature_status = models.BooleanField(choices=CHOICE,default=0,blank=False)
    feature_votes = models.IntegerField(default=0)
    feature_pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.feature_name