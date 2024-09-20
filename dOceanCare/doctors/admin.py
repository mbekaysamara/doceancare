# doctors/admin.py
from django.contrib import admin
from .models import Doctor


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'phone_number', 'email', 'gender', 'created_at', 'updated_at')
    search_fields = ('name', 'email', 'phone_number', 'specialization')
    list_filter = ('specialization', 'gender')
    ordering = ('name',)
