from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
    
    def ready(self):
        # Registra os filtros de template customizados
        try:
            from .templatetags import legacy_filters
        except ImportError:
            pass
