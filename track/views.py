import uuid
from pyexpat import model
from webbrowser import get
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


# check the type of the user
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



def aboutus(request):
    return render(request,"aboutus.html")

def afterlogin_view(request):
    if request.user.is_authenticated == False:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                if user.is_staff:
                    auth.login(request, user)
                    return redirect('admin-dashboard')
                elif user is not None and user.groups.filter(name='NURSE').exists():
                    auth.login(request, user)
                    return redirect('nurse-dashboard')
                elif user is not None and user.groups.filter(name='PATIENT').exists():
                    print("asdasdas")
                    auth.login(request, user)
                    return redirect('patient-dashboard')
            else:
                messages.info(request, 'invalid username or password')
                return redirect('login')
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


def is_patient(user):
    return user.groups.filter(name='PATIENT').exists()


@user_passes_test(is_patient)
def patient_dashboard(request):
    mydict = {}
    user = models.Patient.objects.get(user_id=request.user.id)
    # for i in models.Patient.objects.all():
    #     if i.user.id == user.id:
    mydict['user'] = user
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
def admin_view_report(request):
    nurses = models.Nurse.objects.all()
    patients = models.Patient.objects.all()
    return render(request, 'admin_view_nurse_report.html', {'nurses': nurses})


@user_passes_test(is_nurse)
def nurse_view_patient(request):
    patients = models.Patient.objects.all()
    print(len(patients))
    return render(request, 'nurse_view_patients.html', {'patients': patients})


@user_passes_test(is_nurse)
def nurse_report_view(request):
    patients = models.Patient.objects.all()
    return render(request, 'nurse_report.html', {'patients': patients})


def nurse_report(request, id):
    dect = {}
    dect['records'] = models.Record.objects.filter(nurse_id=id)
    return render(request, 'admin_nurse_report.html', dect)


@user_passes_test(is_admin)
def admin_nurse_view(request):
    patients = models.Patient.objects.all()
    return render(request, 'admin_nurse.html', {'patients': patients})


def upadateUrineSurgery(request, id):
    if request.method == 'POST':
        user = models.Patient.objects.get(user_id=id)
        user.Urine_surgery = request.POST['UrineSurgery']
        user.save()
    return render(request, 'updateUrineSurgery.html')


@user_passes_test(is_admin)
def admin_add_nurse(request):
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
            nurse.save()
            my_nurse_group = Group.objects.get_or_create(name='NURSE')
            my_nurse_group[0].user_set.add(user)
        return HttpResponseRedirect('/admin-nurse')
    return render(request, 'admin_add_nurse.html', context=mydict)


# @login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_add_patient(request):
    userForm = forms.PatientUserForm()
    patientForm = forms.PatientForm()
    mydict = {'userForm': userForm, 'patientForm': patientForm}
    if request.method == 'POST':
        userForm = forms.PatientUserForm(request.POST)
        patientForm = forms.PatientForm(request.POST, request.FILES)
        print(userForm.is_valid())
        print(patientForm.is_valid())
        if userForm.is_valid() and patientForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()
            patient = patientForm.save(commit=False)
            patient.user = user
            print("|Asdasdaddas")
            patient.save()
            my_patient_group = Group.objects.get_or_create(name='PATIENT')
            my_patient_group[0].user_set.add(user)
        return HttpResponseRedirect('/admin-view-patient')
    return render(request, 'admin_add_patient.html', context=mydict)


@user_passes_test(is_nurse)
def nurse_food(request):
    return render(request, 'nurse_food.html')


@user_passes_test(is_patient)
def patient_feedback(request):
    if request.method == 'POST':
        feedback = models.Feedback()
        feedback.name = request.POST['by']
        feedback.message = request.POST['message']
        feedback.senderType = request.POST['senderType']
        feedback.sen_id = request.user.id
        feedback.save()
        # patient = models.Patient()
        # for i in models.Patient.objects.all():
        #     if request.user == i.user:
        #         patient = i
        return render(request, 'feedback_for_patient.html')
    return render(request, 'patient_feedback.html')


@user_passes_test(is_nurse)
def upadateECG(request, id):
    if request.method == 'POST':
        user = models.Patient.objects.get(user_id=id)
        user.ECG = request.POST['ECG']
        user.save()
    return render(request, 'updateECG.html')


@user_passes_test(is_admin)
def admin_feedbacks(request):
    feedback = models.Feedback.objects.all().order_by('-id')
    return render(request, 'admin_feedbacks.html', {'feedback': feedback})


@user_passes_test(is_admin)
def admin_replay(request, pk):
    feedback = models.Feedback.objects.all().get(id=pk)
    if request.method == 'POST':
        feedback.replay = request.POST['replay']
        feedback.save()
        return render(request, 'replay_for_admin.html')
    return render(request, 'admin_replay.html')


@user_passes_test(is_nurse)
def nurseMessage(request, pk):
    patient = None
    for i in models.Patient.objects.all():
        if i.user_id == pk:
            patient = i
    print(patient)
    if request.method == 'POST':
        message = models.Feedback()
        message.by = request.user.username
        message.message = request.POST['message']
        message.senderType = request.POST['senderType']
        message.sen_id = request.user.id
        message.rec_id = patient.user_id
        message.save()
        # patient.feedbacks.add(message)
        return render(request, 'message_for_nurse.html')
    return render(request, 'nurseMessage.html', {'user': request.user})


@user_passes_test(is_patient)
def feedback_list(request):
    context = {}
    patient = models.Patient()
    if request.user.is_authenticated and not request.user.is_anonymous:
        for i in models.Patient.objects.all():
            if request.user.id == i.user_id:
                context['feedbacks'] = models.Feedback.objects.filter(sen_id=i.user_id)
        return render(request, 'patient_feedbacks.html', context)


@user_passes_test(is_patient)
def message_list(request):
    context = {}
    patient = models.Patient()
    if request.user.is_authenticated and not request.user.is_anonymous:
        for i in models.Patient.objects.all():
            if request.user.id == i.user_id:
                context['feedbacks'] = models.Feedback.objects.filter(rec_id=i.user_id)
        return render(request, 'patient_received.html', context)


@user_passes_test(is_patient)
def profile(request):
    mydict = {}
    user = models.User.objects.get(id=request.user.id)
    for i in models.Patient.objects.all():
        if i.user_id == user.id:
            mydict['user'] = i
    return render(request, 'profile.html', mydict)


@user_passes_test(is_nurse)
def updateBloodPressure(request, pk):
    if request.method == 'POST':
        user = models.Patient.objects.get(id=pk)
        user.Blood_Pressure = request.POST['BloodPressure']
        user.save()
    return render(request, 'updateBloodPressure.html')


@user_passes_test(is_patient)
def updateBloodPressurePatient(request, id):
    if request.method == 'POST':
        user = models.Patient.objects.get(user_id=id)
        user.Blood_Pressure = request.POST['BloodPressure']
        user.save()
    return render(request, 'updateBloodPressurePatient.html')

@user_passes_test(is_nurse)
def updateCholesterol(request, id):
    if request.method == 'POST':
        user = models.Patient.objects.get(user_id=id)
        user.Cholesterol = request.POST['Cholesterol']
        user.save()
    return render(request, 'updateCholesterol.html')


@user_passes_test(is_nurse)
def updateFats(request, id):
    print(id)
    if request.method == 'POST':
        user = models.Patient.objects.get(user_id=id)
        user.Fats = request.POST['Fats']
        user.save()
    return render(request, 'updateFats.html')



def updateLiverFunction(request, id):
    if request.method == 'POST':
        user = models.Patient.objects.get(user_id=id)
        user.Liver_function = request.POST['LiverFunction']
        user.save()
    return render(request, 'updateLiverFunction.html')




def updateKidneyFunction(request, id):
    if request.method == 'POST':
        user = models.Patient.objects.get(user_id=id)
        user.Kidney_function = request.POST['KidneyFunction']
        user.save()
    return render(request, 'updateKidneyFunction.html')

@user_passes_test(is_patient)
def patient_view_food(request):
    food = models.Food.objects.all()
    # for i in food:
    #     print(i.Name)
    return render(request, 'patient_view_food.html', {'food': food})


@user_passes_test(is_patient)
def show_food_list(request):
    context = None
    lst=[]
    if request.user.is_authenticated and not request.user.is_anonymous:
        userInfo = models.Patient.objects.get(user=request.user)
        food = models.FoodPatient.objects.filter(patient_id=userInfo.user_id)
        for i in food:
            for j in models.Food.objects.all():
                if i.foodName==j.Name:
                    lst.append(j)
        context = {'food': lst}
        print(userInfo.user)
    return render(request, 'show_food_list.html', context)


@user_passes_test(is_patient)
def food_list(request, pk):
    patient = models.Patient.objects.get(user=request.user)
    f = models.FoodPatient()
    for i in models.Food.objects.all():
        if i.Name == pk:
            print("TTTTrue")
            food = i
            f.foodName = food.Name
    check = patient.Cholesterol > food.max_Cholesterol or patient.Liver_function > food.max_Liver_function or patient.Kidney_function > food.max_Kidney_function or patient.Blood_Pressure > food.max_Blood_Pressure
    if request.user.is_authenticated and not request.user.is_anonymous:
        if check != True:
            messages.error(request, '\t')
        if check == True:
            print("True")
            user = models.Patient.objects.get(user=request.user)
            food.patient_id = user.user_id
            f.patient_id = user.user_id
            f.save()
            # food.save()
            messages.success(request, '\t')
    else:
        redirect('')
    return redirect('patient-view-food')


@user_passes_test(is_nurse)
def nurse_view_food(request):
    food = models.Food.objects.all()
    return render(request, 'nurse_view_food.html', {'food': food})


@user_passes_test(is_nurse)
def delete_food(request, pk):
    food = models.Food()
    print("asdasdasdasd")
    for i in models.Food.objects.all():
        if i.Name == pk:
            print("asdasdasd")

    food = models.Food.objects.filter(Name=pk)
    # for i in food:
    #     if i.Name==pk:
    #         i.delete()
    # print(i.max_Blood_Pressure)
    # print(models.Food.objects.filter(Name=pk))
    # print(food.max_Cholesterol)
    # for i in models.Food.objects.all():
    #     if i.Name == pk:
    #         i.delete()
    return HttpResponseRedirect('/nurse-view-food')


@user_passes_test(is_nurse)
def nurse_add_food(request):
    flag = False
    if request.method == 'POST':
        food = models.Food()
        for i in models.Food.objects.all():
            if i.Name == request.POST['Name']:
                flag = True

        food.Name = request.POST['Name']
        food.number = request.POST['num']
        food.max_Cholesterol = request.POST['max_Cholesterol']
        food.max_Liver_function = request.POST['max_Liver_function']
        food.max_Kidney_function = request.POST['max_Kidney_function']
        food.max_Blood_Pressure = request.POST['max_Blood_Pressure']
        food.pic = request.FILES['pic']
        if flag == False:
            food.save()
        else:
            messages.error(request, "The role is already booked")

        return HttpResponseRedirect('nurse-dashboard')
    return render(request, 'nurse_add_food.html')


# BSPM2022T1
@user_passes_test(is_admin)
def admin_add_medication(request, id_patient):
    if request.method == 'POST':
        medication = models.Medication()
        medication.name = request.POST['name']
        medication.numOftimes = request.POST['numOftimes']
        medication.mg = request.POST['mg']
        medication.expiratDate = request.POST['expiratDate']
        medication.Description = request.POST['Description']
        medication.patient_id = id_patient
        medication.save()
        return render(request, 'admin_view_patient.html', context={'patients': models.Patient.objects.all()})
    return render(request, 'admin_add_medication.html')


@user_passes_test(is_nurse)
def nurse_add_Record(request, id_nurse):
    if request.method == 'POST':
        record = models.Record()
        record.patientName = request.POST['patientName']
        record.body = request.POST['body']
        record.nurse_id = id_nurse
        record.save()
        # patient = models.Patient.objects.get(id_patient)
        # nurse = models.Nurse()
        # for i in models.Nurse.objects.all():
        #     if i.user.id == id_nurse:
        #         print("Asdasdasd")
        #         nurse = i
        #         print(nurse)
        return render(request, 'nurse_Record.html')
    return render(request, 'nurse_Record.html', context={'patients': models.Patient.objects.all()})


def updateGlucose(request, id):
    if request.method == 'POST':
        user = models.Patient.objects.get(user_id=id)
        user.Glucose = request.POST['Glucose']
        user.save()
    return render(request, 'updateGlucose.html')


@user_passes_test(is_patient)
def show_medication_list(request):
    context = None
    if request.user.is_authenticated and not request.user.is_anonymous:
        userInfo = models.Patient.objects.get(user=request.user)
        medication = models.Medication.objects.filter(patient_id=userInfo.user_id)
        context = {'medication': medication}
    return render(request, 'show_medication_list.html', context)


def Appointment(request):
    return render(request, 'patient_appointment.html')


def AdminBookAppointment(request):
    patient = models.Patient()
    if request.method == 'POST':
        c = False
        for i in models.Patient.objects.all():
            if i.user.username == request.POST['patientName']:
                c = True
                patient = i
        if c:
            ap = models.Appointment()
            ap.date = request.POST['appointment']
            ap.time = request.POST['time']
            ap.name = patient.user
            ap.patient_id = patient.user_id
            flag = True
            for i in models.Appointment.objects.all():
                if (str(i.date) == str(ap.date) and str(i.time)[0:5] == str(ap.time)):
                    flag = False
                    messages.error(request, "The role is already booked")
            if flag:
                ap.save()

                messages.success(request, "Book Success")
    return render(request, 'AdminBookAppointment.html', {'patients': models.Patient.objects.all()})


def PatientAppointments(request):
    context = {}
    context['appointment'] = models.Appointment.objects.filter(patient_id=request.user.id)
    return render(request, 'MyAppointment.html', context)

def adminAppointments(request):
    appointments = models.Appointment.objects.all()
    return render(request, 'adminAppointments.html', {'appointments': appointments})


def BookAppointment(request):
    if request.method == 'POST':
        user = models.Patient.objects.get(user=request.user)
        ap = models.Appointment()
        ap.date = request.POST['appointment']
        ap.time = request.POST['time']
        ap.name = request.user.username
        ap.patient_id = request.user.id
        flag = True
        for i in models.Appointment.objects.all():
            if (str(i.date) == str(ap.date) and str(i.time)[0:5] == str(ap.time)[0:5]):
                flag = False
                messages.error(request, "The role is already booked")
        if flag:
            ap.save()
            messages.success(request, "Book Success")
    return render(request, 'BookAppointment.html')


def Admin_Appointment(request):
    return render(request, 'admin_appointment.html')


@user_passes_test(is_patient)
def map(request):
    return render(request, 'map.html')
