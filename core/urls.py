from rest_framework import routers
from core.views import (
    UsuarioViewSet, ComodoViewSet, DispositivoViewSet, CenaViewSet, 
    AcaoCenaViewSet, CasaViewSet, TipoDispositivoViewSet, LogDispositivoViewSet, CustomAuthToken
)
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'casas', CasaViewSet)
router.register(r'comodos', ComodoViewSet)
router.register(r'tipos-dispositivo', TipoDispositivoViewSet)
router.register(r'dispositivos', DispositivoViewSet)
router.register(r'cenas', CenaViewSet)
router.register(r'acoes-cena', AcaoCenaViewSet)
router.register(r'logs', LogDispositivoViewSet)

urlpatterns = [
    path('auth/login/', CustomAuthToken.as_view(), name='api_token_auth'),
    path('', include(router.urls)),
]
