"""
ASGI config for config-admin project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# Use settings de produção se RENDER estiver definido
if os.environ.get('RENDER'):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config-admin.settings_production')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config-admin.settings')

application = get_asgi_application()
