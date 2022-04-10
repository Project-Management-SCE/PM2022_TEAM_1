from django import forms
from django.contrib.auth.models import User
from . import models


#for nurse signup
class NurseUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }

class NurseForm(forms.ModelForm):
    class Meta:
        model=models.Nurse
        fields=['address','mobile','department','status','profile_pic']


class PatientUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
class PatientForm(forms.ModelForm):
    class Meta:
        model=models.Patient
        fields=['address','status','symptoms','profile_pic','gender','age']
