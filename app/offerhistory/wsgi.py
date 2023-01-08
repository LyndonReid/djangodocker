"""
WSGI config for offerhistory project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

sys.path.append('/home/ubuntu/offerhistory/offerhistory/')
os.environ.setdefault("PYTHON_EGG_CACHE", "/home/ubuntu/offerhistory/egg_cache")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'offerhistory.settings')

application = get_wsgi_application()


