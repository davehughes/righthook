Purpose:
--------
Simple service for handling webhooks and pushing the details to a Celery task
queue to be asynchronously processed.  Separates the availability of webhook
handlers from the availability of your main Django application.

Installing and configuring
--------------------------
TODO: upload to pypi
```sh
pip install git+git://github.com/davehughes/righthook#egg=righthook
```

The following variables need to be set up for righthook to run correctly:
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

