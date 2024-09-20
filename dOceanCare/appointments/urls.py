# appointments/urls.py

from django.urls import path
from . import views  # Import views from the appointments app

urlpatterns = [
    path('', views.appointment_list, name='appointment_list'),  # List all appointments
    path('<int:pk>/', views.appointment_detail, name='appointment_detail'),  # Appointment detail view
    path('create/', views.create_appointment, name='create_appointment'),  # Create new appointment
    path('update/<int:pk>/', views.update_appointment, name='update_appointment'),  # Update appointment
    path('delete/<int:pk>/', views.delete_appointment, name='delete_appointment'),  # Delete appointment
]
