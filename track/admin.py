from django.contrib import admin
from .models import Nurse,Patient,Food,Medication

# Register your models here.

admin.site.register(Nurse)
admin.site.register(Patient)
admin.site.register(Food)
admin.site.register(Medication)