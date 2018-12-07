# Generated by Django 2.1.4 on 2018-12-06 17:03

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('affective_response', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='affectiveresponse',
            name='my_field2',
            field=multiselectfield.db.fields.MultiSelectField(choices=[(1, 'Item title 2.1'), (2, 'Item title 2.2'), (3, 'Item title 2.3'), (4, 'Item title 2.4'), (5, 'Item title 2.5')], default=1, max_length=5),
        ),
    ]