# patients/views.py
from django.shortcuts import render, get_object_or_404
from .models import Patient


def patient_detail(request, id):
    patient = get_object_or_404(Patient, id=id)
    return render(request, 'patients/patient_detail.html', {'patient': patient})
