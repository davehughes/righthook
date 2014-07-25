import importlib
import os

original_settings = os.environ.get('RIGHTHOOK_ORIGINAL_DJANGO_SETTINGS_MODULE')
original_settings_module = importlib.import_module(original_settings)
globals().update(original_settings_module.__dict__)

ROOT_URLCONF = 'righthook.urls'
WSGI_APPLICATION = 'righthook.wsgi.application'
