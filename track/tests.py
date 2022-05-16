import asyncio
import unittest
# from multiprocessing.dummy.connection import Client

from django.test import TestCase, tag
from django.urls import reverse
from django.test import Client
from track.models import *


@tag("unit_test")
class LogoutTest(TestCase):
    def testLogout(self):
        User.objects.create(username='israa1', password='123')
        self.client.login(username='username', password='password')

        response = self.client.get(reverse('logout'), follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context["user"].is_authenticated)


@tag("unit_test")
class AdminUsersTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='username', email='email',
                                             last_name='last_name',
                                             first_name='first_name')
        self.user.set_password('password')
        self.user.save()


#
@tag("unit_test")
class AdminPatientFormTests(TestCase):
    @tag('unit-test')
    def test_Add_patient_GET(self):
        c = Client()
        response = self.client.get(reverse('admin-add-patient'))
        self.assert_(response.status_code, 200)


@tag("unit_test")
class AdminNurseFormTests(TestCase):

    @tag("unit-test")
    def test_Add_Nurse_GET(self):
        c = Client()
        response = c.get(reverse('admin-add-nurse'))
        self.assert_(response.status_code, 200)

    @tag('unit-test')
    def test_login(self):
        login = self.client.login(username='test', password='test')
        self.assertFalse(login)


@tag('unit-test')
class RegisterTest_Nurse(TestCase):
    @tag('unit-test')
    def test_register_access_url(self):
        response = self.client.get('/nursesignup')
        self.assertEqual(response.status_code, 200)


class RegisterTest_Patient(TestCase):
    @tag('unit-test')
    def test_register_access_url(self):
        response = self.client.get('/patientsignup')
        self.assert_(response.status_code, 200)

    @tag('unit-test')
    def test_register_access_name(self):
        response = self.client.get('patientsignup')
        self.assert_(response.status_code, 200)

    @tag('unit-test')
    def test_register_access_url_negative(self):
        response = self.client.get('patientsignup')
        self.assertNotEqual(response.status_code, 300)


class loginTest(TestCase):

    @tag('unit-test')
    def test_login_access_url(self):
        response = self.client.get('/login/')
        self.assertNotEqual(response.status_code, 300)

    @tag('unit-test')
    def test_login_access_name(self):
        response = self.client.get(reverse('login'))
        self.assertNotEqual(response.status_code, 300)

    @tag('unit-test')
    def test_login_access_url_negative(self):
        response = self.client.get('/login/')
        self.assertNotEqual(response.status_code, 300)

    @tag('unit-test')
    def test_login_access_name_negative(self):
        response = self.client.get(reverse('login'))
        self.assertNotEqual(response.status_code, 300)

    @tag('unit-test')
    def testLoginUsedTemplate(self):
        response = self.client.get(reverse('login'))
        self.assert_(response.status_code, 200)
        self.assertTemplateUsed(response, 'loginPage.html')

    @tag('unit-test')
    def testLogin_NOT_UsedTemplate(self):
        response = self.client.get(reverse('login'))
        self.assert_(response.status_code, 200)
        self.assertTemplateNotUsed(response, 'home.html')

    @tag('unit-test')
    def testUserLogin(self):
        User.objects.create(username='aa', password='aa')

        data = {'username': 'a12', 'password': '1234'}
        response = self.client.post(reverse('login'), data=data, follow=True)
        self.assertEqual(response.status_code, 200)
        '''the reason why it redircets to login that's this user doesnt belong to any group'''
        self.assertRedirects(response, reverse('login'))

    @tag('integration-test')
    def testLoginAndLogout(self):
        User.objects.create(username='aa', password='aa')

        data = {'username': 'a12', 'password': '1234'}
        response = self.client.post(reverse('login'), data=data, follow=True)
        self.assertEqual(response.status_code, 200)
        '''the reason why it redircets to login that's this user doesnt belong to any group'''
        self.assertRedirects(response, reverse('login'))
        self.assertTemplateUsed(response, 'loginPage.html')

        response = self.client.get(reverse('logout'), follow=True)

        # Assert
        self.assert_(response.status_code, 200)
        self.assertFalse(response.context["user"].is_authenticated)


class FeedbackTest(TestCase):

    @tag('unit-test')
    def test_feedback_access_url(self):
        response = self.client.get('patient-feedback', )
        self.assert_(response.status_code, 200)

    @tag('unit-test')
    def test_feedback_access_subject(self):
        response = self.client.get(reverse('patient-feedback'))
        self.assert_(response.status_code, 200)

    @tag('unit-test')
    def test_feedback_access_url_negative(self):
        response = self.client.get('/patient-feedback')
        self.assertNotEqual(response.status_code, 300)

    @tag('unit-test')
    def test_view(self):
        data = {'feedbackContent': 'content', }
        response = self.client.post(reverse('patient-feedback'), data=data, follow=True)
        self.assert_(response.status_code, 200)


class addMedicationTest(TestCase):
    @tag('unit-test')
    def test_medication_access_url(self):
        response = self.client.get('/admin-add-medication')
        self.assert_(response.status_code, 200)


class addRecordTest(TestCase):
    @tag('unit-test')
    def test_record_access_url(self):
        response = self.client.get('/nurse-add-record')
        self.assert_(response.status_code, 200)


class addFoodTest(TestCase):
    @tag('unit-test')
    def test_food_access_url(self):
        response = self.client.get('/nurse-add-food')
        self.assert_(response.status_code, 200)


class viewFoodTest(TestCase):
    @tag('unit-test')
    def testFoodViewTemplate(self):
        response = self.client.get('/patient-view-food')
        self.assert_(response.status_code, 200)


################################ HAchathon UnitTest ###############################################

class NurseMessageTest(TestCase):

    @tag('unit-test')
    def test_message_access_url(self):
        response = self.client.get('nurse-message')
        self.assertNotEqual(response.status_code, 300)

    @tag('unit-test')
    def test_message_access_template(self):
        response = self.client.get(('nurse-message'))
        self.assertNotEqual(response.status_code, 300)
        self.assertTemplateNotUsed(response, 'nurseMessage.html')


class NurseInsertTest(TestCase):

    @tag('unit-test')
    def test_LiverFunction_access_url(self):
        response = self.client.get('update-LiverFunction/<int:id>')
        self.assertNotEqual(response.status_code, 300)

    @tag('unit-test')
    def test_LiverFunction_access_template(self):
        response = self.client.get('update-LiverFunction/<int:id>')
        self.assertNotEqual(response.status_code, 300)
        self.assertTemplateNotUsed(response, 'updateLiverFunction.html')


class NurseInsertInfoTest(TestCase):

    @tag('unit-test')
    def test_LiverFunction_access_url(self):
        response = self.client.get('update-Fats/<int:id>')
        self.assertNotEqual(response.status_code, 300)

    @tag('unit-test')
    def test_LiverFunction_access_template(self):
        response = self.client.get('update-Fats/<int:id>')
        self.assertNotEqual(response.status_code, 300)
        self.assertTemplateNotUsed(response, 'updateFats.html')

    @tag('unit-test')
    def test_LiverCholesterol_access_url(self):
        response = self.client.get('update-Cholesterol/<int:id>')
        self.assertNotEqual(response.status_code, 300)

    @tag('unit-test')
    def test_Cholesterol_access_template(self):
        response = self.client.get('update-Cholesterol/<int:id>')
        self.assertNotEqual(response.status_code, 300)
        self.assertTemplateNotUsed(response, 'updateCholesterol.html')

    @tag('unit-test')
    def test_BloodPressure_access_url(self):
        response = self.client.get('update-BloodPressure/<int:id>')
        self.assertNotEqual(response.status_code, 300)

    @tag('unit-test')
    def test_BloodPressure_access_template(self):
        response = self.client.get('update-BloodPressure/<int:id>')
        self.assertNotEqual(response.status_code, 300)
        self.assertTemplateNotUsed(response, 'updateBloodPressure.html')

    @tag('unit-test')
    def test_KidneyFunction_access_url(self):
        response = self.client.get('update-KidneyFunction/<int:id>')
        self.assertNotEqual(response.status_code, 300)

    @tag('unit-test')
    def test_KidneyFunction_access_template(self):
        response = self.client.get('update-KidneyFunction/<int:id>')
        self.assertNotEqual(response.status_code, 300)
        self.assertTemplateNotUsed(response, 'updateKidneyFunction.html')

    @tag('integration-test')
    def testLoginAndLogout(self):
        # Login
        user = User.objects.create()
        self.client.force_login(user=user)
        # accss view
        response = self.client.get(('login'))
        self.assertTrue(user.is_authenticated)

        self.assert_(response.status_code, 200)

        # logout
        response = self.client.get(reverse('logout'), follow=True)

        self.assertEqual(response.status_code, 200)

    @tag('integration-test')
    def testUpdateKidneyFunction(self):
        # Login
        user = User.objects.create()
        self.client.force_login(user=user)
        # accss view
        self.assertTrue(user.is_authenticated)
        response = self.client.get(('update-KidneyFunction/<int:id>'))

        self.assert_(response.status_code, 200)

        # logout
        response = self.client.get(reverse('logout'), follow=True)

        self.assertEqual(response.status_code, 200)


class PatientBookAppointmentTest(TestCase):

    @tag('unit-test')
    def test_Appointment_access_url(self):
        response = self.client.get('appointment')
        self.assertNotEqual(response.status_code, 300)

    @tag('unit-test')
    def test_BookAppointment_access_url(self):
        response = self.client.get('bookappointment')
        self.assertNotEqual(response.status_code, 300)

    @tag('unit-test')
    def test_BookAppointment_access_template(self):
        response = self.client.get('bookappointment')
        self.assertNotEqual(response.status_code, 300)
        self.assertTemplateNotUsed(response, 'BookAppointment.html')

    @tag('unit-test')
    def test_Appointment_access_template(self):
        response = self.client.get('appointment')
        self.assertNotEqual(response.status_code, 300)
        self.assertTemplateNotUsed(response, 'patient_appointment.html')

    @tag('integration-test')
    def testLoginAndPatientBookAppointmentAndLogout(self):
        # Login
        user = User.objects.create()
        self.client.force_login(user=user)
        # accss view
        response = self.client.get(('login'))
        self.assertTrue(user.is_authenticated)

        response = self.client.get(('bookappointment'))
        self.assert_(response.status_code, 200)

        response = self.client.get(reverse('logout'), follow=True)

        self.assertEqual(response.status_code, 200)

class AdminBookAppointmentTest(TestCase):

    @tag('unit-test')
    def test_AdminBookAppointment_access_url(self):
        response = self.client.get('adminAppointment')
        self.assertNotEqual(response.status_code, 300)

    @tag('unit-test')
    def test_AdminAppointment_access_url(self):
        response = self.client.get('adminbookappointment')
        self.assertNotEqual(response.status_code, 300)

    @tag('unit-test')
    def test_AdminBookAppointment_access_template(self):
        response = self.client.get('adminbookappointment')
        self.assertNotEqual(response.status_code, 300)
        self.assertTemplateNotUsed(response, 'AdminBookAppointment.html')

    @tag('unit-test')
    def test_AdminAppointment_access_template(self):
        response = self.client.get('appointment')
        self.assertNotEqual(response.status_code, 300)
        self.assertTemplateNotUsed(response, 'admin_appointment.html')


    @tag('integration-test')
    def testLoginAndAdminBookAppointmentAndLogout(self):
        # Login
        user = User.objects.create()
        self.client.force_login(user=user)
        # accss view
        response = self.client.get(('login'))
        self.assertTrue(user.is_authenticated)

        response = self.client.get(('adminbookappointment'))
        self.assert_(response.status_code, 200)

        response = self.client.get(reverse('logout'), follow=True)

        self.assertEqual(response.status_code, 200)

    ####
