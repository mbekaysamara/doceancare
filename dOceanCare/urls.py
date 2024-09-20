# docean_care/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin route
    path('', views.home, name='home'),  # Home route
    path('patients/', views.patients, name='patients'),  # Patients app routes
    path('doctors/', views.doctors, name='doctors'),    # Doctors app routes
    path('appointments/', views.appointments, name='appointments'),  # Appointments app routes
    path('billing/', views.billing, name='billing'),  # Billing app routes
    path('contact/', views.contact, name='contact'),    # Contact app routes
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
