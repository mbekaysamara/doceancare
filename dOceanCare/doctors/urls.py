# doctors/urls.py
from django.urls import path
from . import views

app_name = 'doctors'

urlpatterns = [
    path('', views.doctor_list, name='doctor_list'),
    path('<int:id>/detail/', views.doctor_detail, name='doctor_detail'),
    path('create/', views.doctor_create, name='doctor_create'),
    path('<int:id>/edit/', views.doctor_edit, name='doctor_edit'),
]
