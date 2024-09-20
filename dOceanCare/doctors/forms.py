# doctors/forms.py
from django import forms
from .models import Doctor


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['name', 'specialization', 'phone_number', 'email', 'address', 'gender']
        widgets = {
            'gender': forms.Select(choices=[('M', 'Male'), ('F', 'Female')]),
        }
