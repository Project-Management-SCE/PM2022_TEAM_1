from django.contrib.auth.models import User
from django.db import models


# Create your models here.

GENDER_CHOICES = (
    (0, 'male'),
    (1, 'female'),
    (2, 'not specified'),
)

class Food(models.Model):
    Name = models.CharField(max_length=50)
    number=models.IntegerField(default=1)
    max_Cholesterol=models.IntegerField(default=150)
    max_Liver_function=models.IntegerField(default=55)
    max_Kidney_function=models.IntegerField(default=60)
    max_Blood_Pressure=models.IntegerField(default=80)
    pic = models.ImageField(upload_to='profile_pic/Food/', null=True, blank=True)

class Medication(models.Model):
    name = models.CharField(max_length=255)
    dosage = models.PositiveIntegerField(default=0)
    mg=models.PositiveIntegerField(default=0)


class Patient(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    address = models.CharField(max_length=40)
    gender = models.IntegerField(choices=GENDER_CHOICES)
    age = models.IntegerField(default=15)
    symptoms = models.CharField(max_length=100,null=False)
    assignedDoctorId = models.PositiveIntegerField(null=True)
    profile_pic = models.ImageField(upload_to='profile_pic/PatientProfilePic/', null=True, blank=True)
    admitDate=models.DateField(auto_now=True)
    status=models.BooleanField(default=False)
    Urine_surgery=models.CharField(max_length=1000,default='u')
    Blood_Pressure=models.IntegerField(default=80)
    Fats=models.IntegerField(default=20)
    Cholesterol=models.IntegerField(default=150)
    Liver_function=models.IntegerField(default=55)
    Kidney_function=models.IntegerField(default=60)
    food_list = models.ManyToManyField(Food)
    medication_dosages = models.ManyToManyField(Medication)

    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name+" ("+self.symptoms+")"



class Nurse(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=True)
    department= models.CharField(max_length=50,default='Cardiologist')
    profile_pic = models.ImageField(upload_to='profile_pic/NurseProfilePic/', null=True, blank=True)
    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return "{} ({})".format(self.user.first_name,self.department)