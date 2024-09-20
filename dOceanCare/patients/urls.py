# patients/urls.py
from django.urls import path
from . import views

app_name = 'patients'

urlpatterns = [
    path('', views.patient_list, name='patient_list'),
    path('<int:id>/detail/', views.patient_detail, name='patient_detail'),
    path('create/', views.patient_create, name='patient_create'),
    path('<int:id>/edit/', views.patient_edit, name='patient_edit'),
]
