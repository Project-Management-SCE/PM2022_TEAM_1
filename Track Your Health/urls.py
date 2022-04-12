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
    path('nursesignup', views.nurse_signup_view, name='nursesignup'),

    path('login', views.afterlogin_view, name='login'),
 
    path('nurse-dashboard', views.nurse_dashboard, name='nurse-dashboard'),

    path('nurselogin', LoginView.as_view(template_name='loginPage.html')),
    path('patientlogin', LoginView.as_view(template_name='loginPage.html')),

    path('afterlogin', views.afterlogin_view, name='afterlogin'),
    path('patientsignup', views.patient_signup_view),
    path('patient-dashboard', views.patient_dashboard, name='patient-dashboard'),

        path('patient-dashboard/<int:id>', views.patient_dashboard, name='patient-dashboard'),
    path('logout', views.logoutUser, name='logout'),

]
