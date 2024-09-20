# appointments/apps.py

from django.apps import AppConfig

from dOceanCare.views import appointments


class AppointmentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'appointments'
    verbose_name = 'Appointments Management'
