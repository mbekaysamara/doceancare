# views.py
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def patients(request):
    return render(request, 'patients/patient_list.html')


def doctors(request):
    return render(request, 'doctors/doctor_list.html')


def appointments(request):
    return render(request, 'appointments/appointment_list.html')


def billing(request):
    return render(request, 'billing/billing_list.html')


def contact(request):
    if request.method == 'POST':
        # Handle form submission here (e.g., send email, save data)
        pass
    return render(request, 'contact.html')
