# doctors/views.py
from django.shortcuts import render, get_object_or_404
from .models import Doctor


def doctor_detail(request, id):
    doctor = get_object_or_404(Doctor, id=id)
    return render(request, 'doctors/doctor_detail.html', {'doctor': doctor})
