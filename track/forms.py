from django import forms
from django.contrib.auth.models import User
from . import models


#for nurse signup
class NurseUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        fields="__all__"
        widgets = {
        'password': forms.PasswordInput()
        }

class NurseForm(forms.ModelForm):
    class Meta:
        model=models.Nurse
        fields=['address','mobile','department','status','profile_pic']
        fields = "__all__"


class PatientUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        fields = "__all__"
        widgets = {
        'password': forms.PasswordInput()
        }
class PatientForm(forms.ModelForm):
    class Meta:
        model=models.Patient
        fields=['address','status','symptoms','profile_pic','gender','age']
        fields = "__all__"


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = models.Feedback
        fields = ['by', 'message','senderType']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 6, 'cols': 30}),
        }
        fields = "__all__"


class MedicationForm(forms.ModelForm):
    class Meta:
        model=models.Medication 
        fields=['name','numOftimes','mg','expiratDate','Description']
        fields = "__all__"

