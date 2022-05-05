# Generated by Django 3.0.5 on 2022-05-05 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0007_auto_20220503_0839'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('by', models.CharField(max_length=40)),
                ('message', models.CharField(max_length=500)),
                ('senderType', models.CharField(default='user type', max_length=40)),
                ('replay', models.CharField(default='Replay', max_length=500)),
            ],
        ),
    ]