from django import forms 
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AddPostForm(forms.Form):
    name = forms.CharField(max_length=100)
    
class AddPostFormDoctor(forms.Form):
    name = forms.CharField(max_length=100, label="Name")
    stage = forms.CharField(max_length=100, label="Stage")
    specialization = forms.ModelChoiceField(queryset=Specializations.objects.all(), label="Specialization")
    hours_worked = forms.IntegerField(label='Hours worked')
    month = forms.CharField(max_length=10, label="Month")
    hours_worked_month = forms.IntegerField(label='Hours worked in Month')
    
class AddPostFormSpecialization(forms.Form):
    name = forms.CharField(label = 'Specialization',max_length=100)
    
class AddPostFormPatient(forms.Form):
    name = forms.CharField(label = 'Patient',max_length=100)
    
class AddPostFormProcedure(forms.Form):
    name = forms.CharField(label = 'Procedure',max_length=100)
    
class AddPostFormPatientProcedures(forms.Form):
    doctor = forms.ModelChoiceField(queryset=Doctors.objects.all(),label="Doctors")
    patient = forms.ModelChoiceField(queryset=Patients.objects.all(),label="Patient")
    procedure = forms.ModelChoiceField(queryset=Procedures.objects.all(),label="Procedure")
    date = forms.DateField(label="Date")

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "password1", "password2")
        
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

    
    
