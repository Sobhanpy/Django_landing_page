from django.shortcuts import render , redirect
from accounts.models import CustomeUser
from django.contrib import messages
from .models import *
from .forms import *
# Create your views here.

def home (request):
    if request.method =='GET':
        services = Services.objects.filter(status=True)
        department=Department.objects.all()
        doctor=Doctors.objects.all()
        doctor_count = Doctors.objects.all().count()
        department_count = Department.objects.all().count()
        service_count=Services.objects.all().count()
        testimonials=Testimonials.objects.all()
        context = {
            'services':services,
            'department':department,
            'doctor':doctor,
            'department_count' : department_count,
            'doctor_count': doctor_count,
            'service_count': service_count,
            'testimonials':testimonials,
        }
        return render(request,"root/index.html" , context=context)   
    elif request.method == 'POST' and len(request.POST) == 2 :
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()  
            messages.add_message(request,messages.SUCCESS,'Your message succsefuly sent and we will call you soon')
            return redirect('root:home')   
        else :
            messages.add_message(request,messages.ERROR,'Your data is not valid try again')
            return redirect('root:home')
        
    elif request.method == 'POST' and len(request.POST) == 5:
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your message sent')
        else:
            messages.add_message(request, messages.ERROR, 'Your data is not valid try again')
        return redirect('root:home')
    elif request.method == 'POST' and len(request.POST) == 8:
        form = AppointmentsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Thank you for select us')
        else:
            messages.add_message(request, messages.ERROR, 'Your data is not valid try again')
        return redirect('root:home')