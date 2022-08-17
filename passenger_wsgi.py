# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/var/www/u1750434/data/www/zetroom.com/zetroom')
sys.path.insert(1, '/var/www/u1750434/data/djangoenv/lib/python3.7/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'zetroom.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
