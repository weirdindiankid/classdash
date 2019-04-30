import os
import sys

sys.path.append('/home/classdash/projectclassdash/django/api/api')

os.environ['PYTHON_EGG_CACHE'] = '/home/classdash/projectclassdash/django/api/.python-egg'

os.environ['DJANGO_SETTINGS_MODULE'] = '/home/classdash/projectclassdash/django/api/api/settings.py'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

