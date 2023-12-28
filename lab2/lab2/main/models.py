import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class Doctors(models.Model):
    name = models.CharField('Name', max_length=100)
    stage = models.CharField('Stage', max_length=100)
    specialization = models.ForeignKey('Specializations', on_delete = models.PROTECT,null = True)
    hours_worked = models.IntegerField()
    month = models.CharField('Month', max_length=10, default=datetime.datetime.now().strftime("%B"))
    hours_worked_month = models.IntegerField('Hours Worked in Month', default=0)
    class Meta:
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return f'/read_doctor'
    
class Specializations(models.Model):
    name = models.CharField(("Specialization"), max_length=100) 
    class Meta:
        verbose_name = 'Specialization'
        verbose_name_plural = 'Specializations'    
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return f'/read_specialization'

class Patients(models.Model):
    name = models.CharField(max_length=100)
    procedures = models.ManyToManyField('Procedures', through='PatientProcedures')
    class Meta:
        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'     
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return f'/read_patient'
    
class Procedures(models.Model):
    name = models.CharField(max_length=100)  
    class Meta:
        verbose_name = 'Procedure'
        verbose_name_plural = 'Procedures'
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return f'/read_procedure'

class PatientProcedures(models.Model):
    doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patients, on_delete=models.CASCADE)
    procedure = models.ForeignKey(Procedures, on_delete=models.CASCADE)
    procedure_name = models.CharField(max_length=100)
    doctor_name = models.CharField(max_length=100)
    patient_name = models.CharField(max_length=100)
    date = models.DateField()
    class Meta:
        verbose_name = 'Patients Procedures'
        verbose_name_plural = 'Patients Procedures'
    def __str__(self):
        return f"{self.patient} - {self.procedure} - {self.date}"
    def get_absolute_url(self):
        return f'/read_patientprocedures'
