The following variables need to be set up for righthook to run correctly:
```sh
export DJANGO_SETTINGS_MODULE='righthook.settings'
export RIGHTHOOK_ORIGINAL_DJANGO_SETTINGS_MODULE='myapp.settings'
```

Setting up celeryd
------------------
+ Add 'righthook.tasks' to CELERY_IMPORTS in the 'myapp.settings' module
