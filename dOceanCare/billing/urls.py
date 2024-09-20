# billing/urls.py
from django.urls import path
from . import views

app_name = 'billing'

urlpatterns = [
    path('', views.billing_list, name='billing_list'),
    path('<int:id>/detail/', views.billing_detail, name='billing_detail'),
    path('create/', views.billing_create, name='billing_create'),
    path('<int:id>/edit/', views.billing_edit, name='billing_edit'),
]
