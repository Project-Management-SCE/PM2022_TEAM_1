# Generated by Django 3.0.5 on 2022-05-08 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0011_merge_20220508_0332'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='Glucose',
        ),
        migrations.AlterField(
            model_name='feedback',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
