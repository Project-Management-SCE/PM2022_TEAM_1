from django.test import TestCase, tag
from django.urls import reverse
from django.test import Client
from track.models import *


class AdminTest(TestCase):
    @tag('unit-test')
    def admin_Add_Nurse_GET(self):
        c = Client()
        response = c.get(reverse('admin-add-nurse'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin_add_nurse.html')

    @tag('unit-test')
    def test_login(self):
        login = self.client.login(username='test', password='test')
        self.assertFalse(login)

