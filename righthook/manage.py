#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ["RIGHTHOOK_ORIGINAL_DJANGO_SETTINGS_MODULE"] =  os.environ['DJANGO_SETTINGS_MODULE']
    os.environ["DJANGO_SETTINGS_MODULE"] = "righthook.settings"

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
