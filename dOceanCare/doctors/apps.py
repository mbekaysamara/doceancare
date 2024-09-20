# doctors/apps.py

from django.apps import AppConfig

from dOceanCare.views import doctors


class DoctorsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'doctors'
    verbose_name = 'Doctors Management'
