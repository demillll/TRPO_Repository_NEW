from django.contrib import admin
from .models import *

admin.site.register(Doctors)
admin.site.register(Specializations)
admin.site.register(Patients)
admin.site.register(Procedures)
admin.site.register(PatientProcedures)