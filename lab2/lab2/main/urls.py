from django.urls import path
from . import views
from .views import register

urlpatterns = [
    path('', views.index, name='index'),
    path('doctor_on_specialization/', views.doctor_on_specialization, name='doctor_on_specialization'),
    path('specializations/', views.specializations, name='specializations'),
    path('overtime_doctors/', views.overtime_doctors, name='overtime_doctors'),
        
    path('create_specialization/', views.create_specialization, name= 'create_specialization'),
    path('create_doctor/', views.create_doctor, name='create_doctor'),
    path('create_patient/', views.create_patient, name='create_patient'),
    path('create_procedure/', views.create_procedure, name='create_procedure'),
    path('create_patientprocedures/', views.create_patientprocedures, name='create_patientprocedures'),
    
    path('read_doctor/', views.read_doctor, name='read_doctor'),
    path('read_specialization/', views.read_specialization, name='read_specialization/'),
    path('read_patient/', views.read_patient, name='read_patient'),
    path('read_procedure/', views.read_procedure, name='read_procedure'),
    path('read_patientprocedures/', views.read_patientprocedures, name='read_patientprocedures'),
    
    path('<int:pk>/doctor_update',views.DoctorUpdate.as_view(), name = 'doctor_update'),
    path('<int:pk>/specialization_update',views.SpecializationUpdate.as_view(), name = 'specialization_update'),
    path('<int:pk>/patient_update',views.PatientUpdate.as_view(), name = 'patient_update'),
    path('<int:pk>/procedure_update',views.ProcedureUpdate.as_view(), name = 'procedure_update'),
    path('<int:pk>/patientprocedures_update',views.PatientProceduresUpdate.as_view(), name = 'patientprocedures_update'),
    
    path('<int:pk>/doctor_delete',views.DoctorDelete.as_view(), name = 'doctor_delete'),
    path('<int:pk>/specialization_delete',views.SpecializationDelete.as_view(), name = 'specialization_delete'),
    path('<int:pk>/patient_delete',views.PatientDelete.as_view(), name = 'patient_delete'),
    path('<int:pk>/procedure_delete',views.ProcedureDelete.as_view(), name = 'procedure_delete'),
    path('<int:pk>/patientprocedures_delete',views.PatientProceduresDelete.as_view(), name = 'patientprocedures_delete'),
    path('register', register.as_view(), name='register'),

]

