# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import sys

sys.path.append('/srv/www/ctec-pet-christopher/matricula')

os.environ['PYTHON_EGG_CACHE'] = '/srv/www/ctec-pet-christopher/matricula/.python-egg'
os.environ['DJANGO_SETTINGS_MODULE'] = 'matricula.settings'

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

