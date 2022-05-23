# Generated by Django 3.0.5 on 2022-05-23 19:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0012_auto_20220523_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='id',
            field=models.IntegerField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True),
        ),
    ]
