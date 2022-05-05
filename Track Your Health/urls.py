"""Track Your Health URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path

from track import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name=''),


    path('login', views.afterlogin_view, name='login'),
    path('afterlogin', views.afterlogin_view, name='afterlogin'),

    path('adminclick', views.adminclick_view),
    path('adminlogin', LoginView.as_view(template_name='loginPage.html')),
    path('admin-dashboard', views.admin_page, name='admin-dashboard'),
    path('admin-patient', views.admin_patient_view, name='admin-patient'),
    path('admin-view-patient', views.admin_view_patient_view, name='admin-view-patient'),
    path('admin-nurse', views.admin_nurse_view, name='admin-nurse'),
    path('admin-add-nurse', views.admin_add_nurse, name='admin-add-nurse'),
    path('admin-add-patient', views.admin_add_patient, name='admin-add-patient'),
    path('admin-feedbacks', views.admin_feedbacks, name='admin-feedbacks'),

    path('nurseclick', views.nurseclick_view),
    path('nurselogin', LoginView.as_view(template_name='loginPage.html')),
    path('nurse-dashboard', views.nurse_dashboard, name='nurse-dashboard'),
    path('nursesignup', views.nurse_signup_view, name='nursesignup'),
    path('nurse-patient', views.nurse_view_patient, name='nurse-patient'),

    path('patientclick', views.patientclick_view),
    path('patientlogin', LoginView.as_view(template_name='loginPage.html')),
    path('patientsignup', views.patient_signup_view),
    path('patient-dashboard', views.patient_dashboard, name='patient-dashboard'),
    path('patient-dashboard/<int:id>', views.patient_dashboard, name='patient-dashboard'),
    path('patient-view-food', views.patient_view_food, name='patient-view-food'),
    path('food-favorite/<int:food_id>', views.food_list, name='food-favorite'),
    path('patient-feedback', views.patient_feedback, name='patient-feedback'),
    path('show-food-list', views.show_food_list, name='show-food-list'),
    path('send-replay/<int:pk>', views.admin_replay, name='send-replay'),

    path('logout', views.logoutUser, name='logout'),






]
