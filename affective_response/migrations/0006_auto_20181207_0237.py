# Generated by Django 2.1.4 on 2018-12-06 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('affective_response', '0005_auto_20181207_0155'),
    ]

    operations = [
        migrations.AddField(
            model_name='affectiveresponse',
            name='comfortability',
            field=models.IntegerField(choices=[(1, 'Very uncomfortable'), (2, 'Uncomfortable'), (3, 'Slightly Uncomfortable'), (4, 'Neutral'), (5, 'Slightly comfortable'), (6, 'Comfortable'), (7, 'Very comfortable')], default=0),
        ),
        migrations.AlterField(
            model_name='affectiveresponse',
            name='accompany',
            field=models.IntegerField(choices=[(1, 'Alone'), (2, 'With family member(s)'), (3, 'With friend(s)'), (4, 'With adult(s)'), (5, 'with child(ren)')], default=0),
        ),
        migrations.AlterField(
            model_name='affectiveresponse',
            name='category',
            field=models.IntegerField(choices=[(1, 'Activities'), (2, 'Social Behavior'), (3, 'Transportation')], default=0),
        ),
        migrations.AlterField(
            model_name='affectiveresponse',
            name='familiarity',
            field=models.IntegerField(choices=[(1, 'For the first time'), (2, 'More Often')], default=0),
        ),
    ]
