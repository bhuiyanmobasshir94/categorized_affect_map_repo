from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
CHOICE = [(1,'Active'),(0,'Inactive')]

class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"
    category_name = models.CharField(max_length=200)
    category_status = models.BooleanField(choices=CHOICE,default=0,blank=False)
    category_votes = models.IntegerField(default=0)
    category_pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.category_name