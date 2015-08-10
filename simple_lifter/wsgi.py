__author__ = 'jason.a.parent@gmail.com (Jason Parent)'

# Standard library imports...
import os

# Django imports...
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "simple_lifter.settings")

application = get_wsgi_application()
