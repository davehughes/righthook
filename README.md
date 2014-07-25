Purpose:
--------
Simple service for handling webhooks and pushing the details to a Celery task
queue to be asynchronously processed.  Separates the availability of webhook
handlers from the availability of your main Django application.

Installing and configuring
--------------------------
```sh
pip install righthook
```

The following variables need to be set up for the service to run correctly:
```sh
export DJANGO_SETTINGS_MODULE='righthook.settings'
export RIGHTHOOK_ORIGINAL_DJANGO_SETTINGS_MODULE='myapp.settings'
```
'myapp.settings' stands in here for either a custom settings file or the existing
settings file for your Django application that already holds the configuration
for your connection to a Celery backend.

Setting up celeryd
------------------
+ Add 'righthook.tasks' to CELERY_IMPORTS in the 'myapp.settings' module (or
  in the configuration file for your celeryd workers, if it is different)


Routing in nginx
----------------
+ Create an upstream pointing to the port or file socket where the righthook
  service is running
+ Add a route for '/webhooks' that serves from that upstream


Consuming Webhooks
------------------
```python
import re
from django.dispatch import receiver
from righthook.signals import webhook_received

@receiver(webhook_received)
def handle_webhook(path, request_data=None, **kwargs):
    if path == '/webhooks/serviceA':
        handle_service_a_webhook(path, request_data)
    elif path == '/webhooks/serviceB':
        handle_service_b_webhook(path, request_data)
    # ...

def handle_service_a_webhook(path, request_data):
    # ...
    pass

def handle_service_b_webhook(path, request_data):
    # ...
    pass
```
