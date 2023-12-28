from django.shortcuts import render, redirect, HttpResponse
from .models import *
from .forms import *
from django.views.generic import UpdateView, DeleteView
from django.views.generic.edit import CreateView, FormView


# Create your views here.
def index(request):
    user = request.user
    main = Doctors.objects.all()
    return render(request, 'main/index.html', {'main' : main, 'user' : user})

def read_doctor(request):
    main = Doctors.objects.all()
    return render(request,'main/read_doctor.html', {'main' : main})   

def read_specialization(request):
    main = Specializations.objects.all()
    return render(request,'main/read_specialization.html', {'main' : main})   
 
def read_patient(request):
    main = Patients.objects.all()
    return render(request,'main/read_patient.html', {'main' : main})

def read_procedure(request):
    main = Procedures.objects.all()
    return render(request,'main/read_procedure.html', {'main' : main}) 
     
def read_patientprocedures(request):
    main = PatientProcedures.objects.all()
    return render(request,'main/read_patientprocedures.html', {'main' : main}) 

def specializations(request):
    if request.method =='POST':
        form = AddPostForm(request.POST)
        
        if form.is_valid():
            try:
                value = form.cleaned_data['name']
                request.session['name_value'] = value
                return redirect('http://127.0.0.1:8000/doctor_on_specialization/',{"name": list(form.base_fields.keys())[0]})
            except:
                form.add_error(None,'ERROR')
    else:
        form = AddPostForm()
        return render(request,'main/specializations.html',{'form': form})
    
def create_doctor(request):

    if request.method =='POST':
        form = AddPostFormDoctor(request.POST)
        
        if form.is_valid():
            try:
                Doctors.objects.create(**form.cleaned_data)
                return redirect('http://127.0.0.1:8000/create_doctor/')
            except:
                
                form.add_error(None,'ERROR')
    else:
        form = AddPostFormDoctor()
        return render(request,'main/create_doctor.html',{'form': form})

def create_specialization(request):

    if request.method =='POST':
        form = AddPostFormSpecialization(request.POST)
        
        if form.is_valid():
            try:
                Specializations.objects.create(**form.cleaned_data)
                return redirect('http://127.0.0.1:8000/')
            except:
                form.add_error(None,'ERROR')
    else:
        form = AddPostFormSpecialization()
        return render(request,'main/create_specialization.html',{'form': form})

def doctor_on_specialization(request):

    specializations = Specializations.objects.all()
    doctors = []
    name = request.session.get('name_value')
    try:
        for i in specializations:
            if i.name == name:
                id = i.id
        doctor = Doctors.objects.all()
        for i in doctor:
            if i.specialization_id == id:
                doctors.append(i)
    except: name = "\n\n There is no such specialization" 
    return render(request,'main/doctor_on_specialization.html',{'main':doctors})

def create_patient(request):

    if request.method =='POST':
        form = AddPostFormPatient(request.POST)
        
        if form.is_valid():
            try:
                Patients.objects.create(**form.cleaned_data)
                return redirect('http://127.0.0.1:8000/create_patient/')
            except:
                
                form.add_error(None,'ERROR')
    else:
        form = AddPostFormPatient()
        return render(request,'main/create_patient.html',{'form': form})

def create_procedure(request):

    if request.method =='POST':
        form = AddPostFormProcedure(request.POST)
        
        if form.is_valid():
            try:
                Procedures.objects.create(**form.cleaned_data)
                return redirect('http://127.0.0.1:8000/create_procedure/')
            except:
                
                form.add_error(None,'ERROR')
    else:
        form = AddPostFormProcedure()
        return render(request,'main/create_procedure.html',{'form': form})

def create_patientprocedures(request):
    if request.method == 'POST':
        form = AddPostFormPatientProcedures(request.POST)
        if form.is_valid():
            doctor = form.cleaned_data['doctor']
            patient = form.cleaned_data['patient']
            procedure = form.cleaned_data['procedure']
            date = form.cleaned_data['date']

            patient_procedure = PatientProcedures(doctor=doctor, patient=patient, procedure=procedure, date=date)
            patient_procedure.save()

            return redirect('http://127.0.0.1:8000/create_patientprocedures/')
    else:
        form = AddPostFormPatientProcedures()

    return render(request, 'main/create_patientprocedures.html', {'form': form})

class DoctorUpdate(UpdateView):
    model = Doctors
    template_name = 'main/create_doctor.html'
    
    fields = ['name', 'stage', 'specialization']

class SpecializationUpdate(UpdateView):
    model = Specializations
    template_name = 'main/create_specialization.html'
    
    fields = ['name']
    
class PatientUpdate(UpdateView):
     model = Patients
     template_name = 'main/create_patient.html'
    
     fields = ['name']
    
class ProcedureUpdate(UpdateView):
    model = Procedures
    template_name = 'main/create_procedure.html'
    
    fields = ['name']
    
class PatientProceduresUpdate(UpdateView):
    model = PatientProcedures
    template_name = 'main/create_patientprocedures.html'
    
    fields = ['doctor', 'pacient', 'procedure', 'date']
          
class DoctorDelete(DeleteView):
    model = Doctors
    success_url = '/read_doctor/'
    template_name = 'main/delete_doctor.html'

class SpecializationDelete(DeleteView):
    model = Specializations
    success_url = '/read_specialization/'
    template_name = 'main/delete_specialization.html'
    
class PatientDelete(DeleteView):
    model = Patients
    success_url = '/read_patient/'
    template_name = 'main/delete_patient.html'

class ProcedureDelete(DeleteView):
    model = Procedures
    success_url = '/read_procedure/'
    template_name = 'main/delete_procedure.html'

class PatientProceduresDelete(DeleteView):
    model = PatientProcedures
    success_url = '/read_patientprocedures/'
    template_name = 'main/delete_pacientprocedures.html'
    
from django.db.models import Count

def search_doctors(request):
    doctors = Doctors.objects.aggregate(total_doctors=Count('id', filter=models.Q(hours_worked__gt=40)))
    
    context = {'main': doctors}
    return render(request, 'main/search_doctors.html', context)

class register(FormView):
    form_class = RegistrationForm
    template_name = 'registration/register.html'
    success_url = '/accounts/login/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
from django.db.models import Sum

def overtime_doctors(request):
    month = request.GET.get('month')  # Получаем заданный месяц из параметров запроса

    if not month:
        # Если месяц не указан, выводим ошибку или делаем другую обработку
        return HttpResponse('Пожалуйста, укажите месяц')

    doctors = Doctors.objects.filter(month=month)  # Фильтруем докторов по заданному месяцу
    overtime_aggregate = doctors.filter(hours_worked_month__gt=40).aggregate(total_overtime=Sum('hours_worked_month') - 40 * doctors.count())

    total_overtime = overtime_aggregate['total_overtime'] or 0

    context = {
        'doctors': doctors,
        'total_overtime': total_overtime,
        'month': month
    }

    return render(request, 'main/overtime_doctors.html', context)