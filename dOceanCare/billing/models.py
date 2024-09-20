# billing/models.py
from django.db import models
from django.urls import reverse


class Billing(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Paid', 'Paid'),
        ('Overdue', 'Overdue'),
    ]

    patient = models.ForeignKey('patients.Patient', on_delete=models.CASCADE, related_name='billings')
    appointment = models.ForeignKey('appointments.Appointment', on_delete=models.CASCADE, related_name='billings')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES, default='Pending')
    payment_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Billing {self.id} - {self.patient.name} - ${self.amount}"

    def get_absolute_url(self):
        return reverse('billing:billing_detail', args=[str(self.id)])
