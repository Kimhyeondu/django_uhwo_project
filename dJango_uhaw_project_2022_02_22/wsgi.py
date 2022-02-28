"""
WSGI config for dJango_uhaw_project_2022_02_22 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dJango_uhaw_project_2022_02_22.settings')

application = get_wsgi_application()
