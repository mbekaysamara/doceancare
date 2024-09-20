# appointments/admin.py
from django.contrib import admin
from .models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'patient', 'doctor', 'appointment_date', 'appointment_time', 'status', 'created_at', 'updated_at')
    search_fields = ('patient__name', 'doctor__name', 'status')
    list_filter = ('status', 'appointment_date')
    ordering = ('-appointment_date', '-appointment_time')
