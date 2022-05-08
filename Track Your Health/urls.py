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

    path('adminclick', views.adminclick_view),
    path('nurseclick', views.nurseclick_view),
    path('patientclick', views.patientclick_view),


    #signup urls
    path('adminlogin', LoginView.as_view(template_name='loginPage.html')),

    path('nursesignup', views.nurse_signup_view, name='nursesignup'),

    path('login', views.afterlogin_view, name='login'),
 
    path('nurse-dashboard', views.nurse_dashboard, name='nurse-dashboard'),
    path('admin-dashboard', views.admin_page, name='admin-dashboard'),

    path('adminlogin', LoginView.as_view(template_name='loginPage.html')),
    path('nurselogin', LoginView.as_view(template_name='loginPage.html')),
    path('patientlogin', LoginView.as_view(template_name='loginPage.html')),

    path('afterlogin', views.afterlogin_view, name='afterlogin'),
    path('patientsignup', views.patient_signup_view),
    path('patient-dashboard', views.patient_dashboard, name='patient-dashboard'),

    path('patient-dashboard/<int:id>', views.patient_dashboard, name='patient-dashboard'),
    path('logout', views.logoutUser, name='logout'),

    path('patient-feedback', views.patient_feedback, name='patient-feedback'),
    path('admin-feedbacks', views.admin_feedbacks, name='admin-feedbacks'),
    path('patient-replays', views.feedback_list, name='patient-replays'),

    path('admin-patient', views.admin_patient_view, name='admin-patient'),
    path('admin-view-patient', views.admin_view_patient_view, name='admin-view-patient'),
    path('admin-view-report', views.admin_view_report, name='admin-view-report'),
    path('admin-nurse', views.admin_nurse_view, name='admin-nurse'),
    path('admin-add-nurse', views.admin_add_nurse, name='admin-add-nurse'),
    path('admin-add-patient', views.admin_add_patient, name='admin-add-patient'),
    path('nurse-food', views.nurse_food, name='nurse-food'),
    path('nurse-add-food', views.nurse_add_food, name='nurse-add-food'),
    path('nurse-patient', views.nurse_view_patient, name='nurse-patient'),
    path('nurse-reprot', views.nurse_report_view, name='nurse-reprot'),
    path('admin-nurse-reprot/<int:id>', views.nurse_report, name='admin-nurse-reprot'),
    path('update-Urine-surgery/<int:id>', views.upadateUrineSurgery, name='update-Urine-surgery'),
    path('admin-add-medication/<int:id_patient>', views.admin_add_medication, name='admin-add-medication'),
    path('nurse-add-record/<int:id_nurse>', views.nurse_add_Record, name='nurse-add-record'),
]
