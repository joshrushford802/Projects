"""
WSGI config for eden_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "xxxx.settings")
# from whitenoise.django import DjangoWhiteNoise
# application = get_wsgi_application()
# application = DjangoWhiteNoise(application)

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eden_project.settings')

application = get_wsgi_application()
