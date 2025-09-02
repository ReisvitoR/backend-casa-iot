import os
from .settings import *
import environ

env = environ.Env()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Hosts permitidos (adicione seu domínio aqui)
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '0.0.0.0',
    'backend-casa-iot.onrender.com',
    '*.onrender.com',
    # Adicione aqui outros domínios do seu deploy:
    # 'seudominio.com',
    # 'api.seudominio.com',
    # 'seu-app.herokuapp.com',
    # 'seu-app.railway.app',
]

# Desabilitar cache problemático em produção
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

# Session simples para produção
SESSION_ENGINE = 'django.contrib.sessions.backends.db'

# CORS configuração completa para produção
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

# CSRF trusted origins
CSRF_TRUSTED_ORIGINS = [
    'https://backend-casa-iot.onrender.com',
    'http://localhost:3000',
    'http://127.0.0.1:3000',
]

# Database 
DATABASES = {
    'default': env.db(),
}

# Static files para produção
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Security settings
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}
