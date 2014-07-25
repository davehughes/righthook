import os

os.environ['RIGHTHOOK_ORIGINAL_DJANGO_SETTINGS_MODULE'] = os.environ['DJANGO_SETTINGS_MODULE']
os.environ['DJANGO_SETTINGS_MODULE'] = "righthook.settings"

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
