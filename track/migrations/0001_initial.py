# Generated by Django 2.2.28 on 2022-05-16 09:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('name', models.CharField(default='unknown', max_length=30)),
                ('time', models.TimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('by', models.CharField(max_length=40)),
                ('message', models.CharField(max_length=500)),
                ('senderType', models.CharField(default='user type', max_length=40)),
                ('replay', models.CharField(default='There is no response to this message', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('number', models.IntegerField(default=1)),
                ('max_Cholesterol', models.IntegerField(default=150)),
                ('max_Liver_function', models.IntegerField(default=55)),
                ('max_Kidney_function', models.IntegerField(default=60)),
                ('max_Blood_Pressure', models.IntegerField(default=80)),
                ('pic', models.ImageField(blank=True, null=True, upload_to='profile_pic/Food/')),
            ],
        ),
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('numOftimes', models.PositiveIntegerField(default=0)),
                ('mg', models.PositiveIntegerField(default=0)),
                ('expiratDate', models.CharField(max_length=50)),
                ('Description', models.CharField(max_length=3000)),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patientName', models.CharField(max_length=40)),
                ('body', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=40)),
                ('gender', models.IntegerField(choices=[(0, 'male'), (1, 'female'), (2, 'not specified')])),
                ('age', models.IntegerField(default=15)),
                ('symptoms', models.CharField(max_length=100, null=True)),
                ('assignedDoctorId', models.PositiveIntegerField(null=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='profile_pic/PatientProfilePic/')),
                ('admitDate', models.DateField(auto_now=True)),
                ('status', models.BooleanField(default=False)),
                ('Urine_surgery', models.CharField(default='u', max_length=1000)),
                ('Blood_Pressure', models.IntegerField(default=80)),
                ('Glucose', models.IntegerField(default=80)),
                ('Fats', models.IntegerField(default=20)),
                ('Cholesterol', models.IntegerField(default=150)),
                ('Liver_function', models.IntegerField(default=55)),
                ('Kidney_function', models.IntegerField(default=60)),
                ('ECG', models.IntegerField(default=70)),
                ('feedbacks', models.ManyToManyField(to='track.Feedback')),
                ('food_list', models.ManyToManyField(to='track.Food')),
                ('medication_dosages', models.ManyToManyField(to='track.Medication')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Nurse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=40)),
                ('mobile', models.CharField(max_length=20, null=True)),
                ('department', models.CharField(default='Cardiologist', max_length=50)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='profile_pic/NurseProfilePic/')),
                ('status', models.BooleanField(default=False)),
                ('reports', models.ManyToManyField(to='track.Record')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
