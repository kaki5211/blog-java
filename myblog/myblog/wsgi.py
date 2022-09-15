"""
WSGI config for myblog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import sys
# import site


from django.core.wsgi import get_wsgi_application

# site.addsitedir("/path/to/pythonhome/lib/python3.6/site-packages")
# sys.path.append("/path/to/projecthome/")
# sys.path.append("/path/to/projecthome/[project]")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myblog.settings')

application = get_wsgi_application()
