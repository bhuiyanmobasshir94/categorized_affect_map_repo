from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
FAMILIARITY_CHOICE = [(1,'For the first time'),(2,'More Often')]
ACCOMPANY_CHOICE = [(1,'Alone'),(2,'With family member(s)'),(3,'With friend(s)'),(4,'With adult(s)'),(5,'with child(ren)')]
COMFORTABILITY_CHOICE = [(1,'Very uncomfortable'),(2,'Uncomfortable'),(3,'Slightly Uncomfortable'),(4,'Neutral'),(5,'Slightly comfortable'),(6,'Comfortable'),(7,'Very comfortable')]

from category.models import Category
from location.models import Location
from category.models import Category
from feature.models import Feature

from multiselectfield import MultiSelectField


categories = Category.objects.filter(category_status=1)
features = Feature.objects.filter(feature_status=1)

CATEGORIES_CHOICE = tuple((x.id, x.category_name) for x in categories)
FEATURES_CHOICE = tuple((x.id, x.feature_name) for x in features)


class AffectiveResponse(models.Model):
    class Meta:
        verbose_name_plural = "affective response"
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    familiarity = models.IntegerField(choices=FAMILIARITY_CHOICE,blank=False)
    accompany = models.IntegerField(choices=ACCOMPANY_CHOICE,blank=False)
    category = models.IntegerField(choices=CATEGORIES_CHOICE,blank=False)
    feature_set =  MultiSelectField(choices=FEATURES_CHOICE,max_choices=5,max_length=20,default=0)
    comfortability = models.IntegerField(choices=COMFORTABILITY_CHOICE,blank=False)
    response_pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.location + "_" + self.category


# from django.core.validators import validate_comma_separated_integer_list 
#models.CharField(max_length=7,validators=[validate_comma_separated_integer_list],blank=True)