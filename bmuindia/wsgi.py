"""
WSGI config for bmuindia project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os, sys

sys.path.append('/home/nandit/Desktop/bmuindia')
sys.path.append('/home/nandit/Desktop/bmuindia/venv/lib/python2.7/site-packages')
	
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bmuindia.settings")

application = get_wsgi_application()
