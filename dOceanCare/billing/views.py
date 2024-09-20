# billing/views.py
from django.shortcuts import render, get_object_or_404
from .models import Billing


def billing_detail(request, id):
    billing = get_object_or_404(Billing, id=id)
    return render(request, 'billing/billing_detail.html', {'billing': billing})
