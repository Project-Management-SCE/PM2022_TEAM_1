# Generated by Django 3.0.5 on 2022-05-08 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0012_auto_20220508_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='feedbacks',
            field=models.ManyToManyField(to='track.Feedback'),
        ),
    ]
