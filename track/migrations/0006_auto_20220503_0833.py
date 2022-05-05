# Generated by Django 3.0.5 on 2022-05-03 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0005_auto_20220503_0831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='static/profile_pic/Food/'),
        ),
        migrations.AlterField(
            model_name='nurse',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='static/profile_pic/NurseProfilePic/'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='static/profile_pic/PatientProfilePic/'),
        ),
    ]
