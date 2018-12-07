# Generated by Django 2.1.4 on 2018-12-06 17:34

import django.core.validators
from django.db import migrations, models
import multiselectfield.db.fields
import re


class Migration(migrations.Migration):

    dependencies = [
        ('affective_response', '0002_affectiveresponse_my_field2'),
    ]

    operations = [
        migrations.AddField(
            model_name='affectiveresponse',
            name='feature_set',
            field=models.CharField(blank=True, max_length=7, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')]),
        ),
        migrations.AlterField(
            model_name='affectiveresponse',
            name='my_field2',
            field=multiselectfield.db.fields.MultiSelectField(choices=[(1, 'Item title 2.1'), (2, 'Item title 2.2'), (3, 'Item title 2.3'), (4, 'Item title 2.4'), (5, 'Item title 2.5')], default=0, max_length=5),
        ),
    ]