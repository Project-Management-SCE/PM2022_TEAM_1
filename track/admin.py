from django.contrib import admin
from .models import Nurse,Patient,Food,Medication,Record

# Register your models here.

admin.site.register(Nurse)
admin.site.register(Patient)
admin.site.register(Food)
admin.site.register(Medication)
admin.site.register(Record)