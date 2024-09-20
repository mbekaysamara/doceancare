
# WSGI config for dOceanCare project.

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dOceanCare.settings')

application = get_wsgi_application()
