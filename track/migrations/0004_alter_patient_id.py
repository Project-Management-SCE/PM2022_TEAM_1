# Generated by Django 4.0.3 on 2022-05-24 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0003_alter_patient_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='id',
            field=models.IntegerField(default=3538, primary_key=True, serialize=False),
        ),
    ]