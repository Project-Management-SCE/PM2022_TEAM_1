from django.contrib import messages

from django.contrib import auth
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate

from . import forms, models
from django.shortcuts import get_object_or_404


def home_view(request):
    if request.user.is_authenticated:  # check if the user is authenticated
        return HttpResponseRedirect('afterlogin')
    return render(request, 'index.html')  # home page


def adminclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')  # after login for the admin
    return render(request, 'adminclick.html')


def nurseclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')  # after login for the nurse
    return render(request, 'nurseclick.html')


# for showing signup/login button for patient(by sumit)
def patientclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')  # after login for the patient
    return render(request, 'patientclick.html')

#check the type of the user
def is_admin(user):
    return user.is_staff

@user_passes_test(is_admin)
def admin_page(request):
    return render(request, 'adminPage.html')


# nurse signup
def nurse_signup_view(request):
    userForm = forms.NurseUserForm()
    nurseForm = forms.NurseForm()
    mydict = {'userForm': userForm, 'nurseForm': nurseForm}
    if request.method == 'POST':
        userForm = forms.NurseUserForm(request.POST)
        nurseForm = forms.NurseForm(request.POST, request.FILES)
        if userForm.is_valid() and nurseForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()
            nurse = nurseForm.save(commit=False)
            nurse.user = user
            nurse = nurse.save()
            my_nurse_group = Group.objects.get_or_create(name='NURSE')
            my_nurse_group[0].user_set.add(user)
        return HttpResponseRedirect('nurselogin')
    return render(request, 'nursesignup.html', context=mydict)


def is_nurse(user):
    return user.groups.filter(name='NURSE').exists()


# patient signup
def patient_signup_view(request):
    userForm = forms.PatientUserForm()
    patientForm = forms.PatientForm()
    mydict = {'userForm': userForm, 'patientForm': patientForm}
    if request.method == 'POST':
        userForm = forms.PatientUserForm(request.POST)
        patientForm = forms.PatientForm(request.POST, request.FILES)
        if userForm.is_valid() and patientForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()
            patient = patientForm.save(commit=False)
            patient.user = user
            patient.assignedDoctorId = request.POST.get('assignedDoctorId')
            patient = patient.save()
            my_patient_group = Group.objects.get_or_create(name='PATIENT')
            my_patient_group[0].user_set.add(user)
        return HttpResponseRedirect('patientlogin')
    return render(request, 'patientsignup.html', context=mydict)


def afterlogin_view(request):
    if request.user.is_authenticated == False:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user.is_staff:
                auth.login(request, user)
                return redirect('admin-dashboard')
            elif user is not None and user.groups.filter(name='NURSE').exists():
                auth.login(request, user)
                return redirect('nurse-dashboard')
            elif user is not None and user.groups.filter(name='PATIENT').exists():
                auth.login(request, user)
                return redirect('patient-dashboard')
        else:
            return render(request, 'loginPage.html')
    else:
        if request.user.is_staff:
            return redirect('admin-dashboard')
        if request.user.groups.filter(name='NURSE'):
            return redirect('nurse-dashboard')
        if request.user.groups.filter(name='PATIENT'):
            return redirect('patient-dashboard')


# @login_required(login_url='nurselogin')
@user_passes_test(is_nurse)
def nurse_dashboard(request):
    mydict = {
    }
    return render(request, 'nurse_dashboard.html', context=mydict)


def is_patient(user):
    return user.groups.filter(name='PATIENT').exists()


@user_passes_test(is_patient)
def patient_dashboard(request):
    mydict = {}
    user = models.User.objects.get(pk=request.user.pk)
    for i in models.Patient.objects.all():
        if i.user.id == user.id:
            mydict['user'] = i
    return render(request, 'patient_dashboard.html', context=mydict)

def logoutUser(request):
    logout(request)
    return redirect('login')


@user_passes_test(is_admin)
def admin_patient_view(request):
    return render(request, 'admin_patient.html')

@user_passes_test(is_admin)
def admin_view_patient_view(request):
    patients = models.Patient.objects.all()
    return render(request, 'admin_view_patient.html', {'patients': patients})

@user_passes_test(is_admin)
def admin_nurse_view(request):
    return render(request, 'admin_nurse.html')


@user_passes_test(is_admin)
def admin_add_nurse(request):
    userForm = forms.NurseUserForm()
    nurseForm = forms.NurseForm()
    mydict = {'userForm': userForm, 'nurseForm': nurseForm}
    if request.method == 'POST':
        print("add nurse")
        userForm = forms.NurseUserForm(request.POST)
        nurseForm = forms.NurseForm(request.POST, request.FILES)
        print(userForm.is_valid())
        print(nurseForm.is_valid())
        if userForm.is_valid() and nurseForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()
            nurse = nurseForm.save(commit=False)
            nurse.user = user
            nurse.save()
            my_nurse_group = Group.objects.get_or_create(name='NURSE')
            my_nurse_group[0].user_set.add(user)
        return HttpResponseRedirect('/admin-nurse')
    return render(request, 'admin_add_nurse.html', context=mydict)


