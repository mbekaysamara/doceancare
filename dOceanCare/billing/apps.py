# billing/apps.py

from django.apps import AppConfig

from dOceanCare.views import billing


class BillingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'billing'
    verbose_name = 'Billing Management'
