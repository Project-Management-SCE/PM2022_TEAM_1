# Generated by Django 2.2.28 on 2022-05-16 09:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0022_auto_20220516_0851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
