# patients/apps.py

from django.apps import AppConfig

from dOceanCare.views import patients


class PatientsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'patients'
    verbose_name = 'Patients Management'
