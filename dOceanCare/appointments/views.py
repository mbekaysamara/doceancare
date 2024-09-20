# appointments/views.py
from django.shortcuts import render, get_object_or_404
from .models import Appointment


def appointment_detail(request, id):
    appointment = get_object_or_404(Appointment, id=id)
    return render(request, 'appointments/appointment_detail.html', {'appointment': appointment})


def appointment_list(request):
    return None


def create_appointment(request):
    return None


def update_appointment(request):
    return None


def delete_appointment(request):
    return None
