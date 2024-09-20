# billing/forms.py
from django import forms
from .models import Billing


class BillingForm(forms.ModelForm):
    class Meta:
        model = Billing
        fields = ['patient', 'appointment', 'amount', 'payment_status', 'payment_date']
        widgets = {
            'payment_date': forms.DateInput(attrs={'type': 'date'}),
            'payment_status': forms.Select(choices=[('Paid', 'Paid'), ('Pending', 'Pending')]),
        }
