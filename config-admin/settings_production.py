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

# CORS para permitir frontend consumir a API
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # React/Next.js local
    "http://localhost:5173",  # Vite local
    "http://localhost:8080",  # Vue local
    "http://127.0.0.1:3000",
    "http://127.0.0.1:5173",
    "http://127.0.0.1:8080",
    # "https://meuapp.netlify.app",
    # "https://meuapp.vercel.app",
]

CORS_ALLOW_CREDENTIALS = True

# Headers permitidos
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
