import asyncio
import unittest
# from multiprocessing.dummy.connection import Client
from django.test import Client
from django.test import TestCase, tag
from django.urls import reverse

from track.models import *



class LogoutTest(TestCase):
    def testLogout(self):
        User.objects.create(username='israa1', password='123')
        self.client.login(username='username', password='password')

        response = self.client.get(reverse('logout'), follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context["user"].is_authenticated)





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
        self.assert_(response.status_code, 200)

    @tag('unit-test')
    def test_login_access_name(self):
        response = self.client.get(reverse('login'))
        self.assert_(response.status_code, 200)

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
        self.assertTemplateUsed(response,'loginPage.html')

    @tag('unit-test')
    def testLogin_NOT_UsedTemplate(self):
        response = self.client.get(reverse('login'))
        self.assert_(response.status_code, 200)
        self.assertTemplateNotUsed(response,'home.html')

    @tag('unit-test')
    def testUserLogin(self):

        User.objects.create(username='aa', password='aa')

        data = {'username': 'a12', 'password': '1234'}
        response=self.client.post(reverse('login'),data=data,follow=True)
        self.assertEqual(response.status_code,200)
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