# billing/admin.py
from django.contrib import admin
from .models import Billing


@admin.register(Billing)
class BillingAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'patient', 'appointment', 'amount', 'payment_status', 'payment_date', 'created_at', 'updated_at')
    search_fields = ('patient__name', 'appointment__id', 'payment_status')
    list_filter = ('payment_status', 'payment_date')
    ordering = ('-created_at',)
