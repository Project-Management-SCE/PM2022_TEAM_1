# Generated by Django 4.0.4 on 2022-05-24 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='id',
            field=models.IntegerField(default=7245, primary_key=True, serialize=False),
        ),
    ]
