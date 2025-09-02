from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.db import transaction
from core.models import *

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    list_display = ['email', 'first_name', 'last_name', 'is_active']
    list_filter = ['is_active', 'is_staff']
    search_fields = ['email', 'first_name', 'last_name']
    
    def get_queryset(self, request):
        try:
            return super().get_queryset(request)
        except Exception:
            return Usuario.objects.none()

@admin.register(Casa)
class CasaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'get_usuario', 'endereco']
    list_filter = ['usuario']
    search_fields = ['nome']
    
    def get_usuario(self, obj):
        try:
            return obj.usuario.first_name if obj.usuario else 'N/A'
        except:
            return 'N/A'
    get_usuario.short_description = 'Usuário'
    
    def get_queryset(self, request):
        try:
            return super().get_queryset(request).select_related('usuario')
        except Exception:
            return Casa.objects.none()

@admin.register(TipoDispositivo)
class TipoDispositivoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'categoria']
    list_filter = ['categoria']
    search_fields = ['nome']

@admin.register(Comodo)
class ComodoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'get_casa']
    list_filter = ['casa']
    search_fields = ['nome']
    
    def get_casa(self, obj):
        try:
            return obj.casa.nome if obj.casa else 'N/A'
        except:
            return 'N/A'
    get_casa.short_description = 'Casa'
    
    def get_queryset(self, request):
        try:
            return super().get_queryset(request).select_related('casa')
        except Exception:
            return Comodo.objects.none()

@admin.register(Dispositivo)
class DispositivoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'get_tipo', 'get_comodo', 'estado', 'ativo']
    list_filter = ['tipo', 'estado', 'ativo']
    search_fields = ['nome']
    
    def get_tipo(self, obj):
        try:
            return obj.tipo.nome if obj.tipo else 'N/A'
        except:
            return 'N/A'
    get_tipo.short_description = 'Tipo'
    
    def get_comodo(self, obj):
        try:
            return obj.comodo.nome if obj.comodo else 'N/A'
        except:
            return 'N/A'
    get_comodo.short_description = 'Cômodo'
    
    def get_queryset(self, request):
        try:
            return super().get_queryset(request).select_related('tipo', 'comodo')
        except Exception:
            return Dispositivo.objects.none()

@admin.register(Cena)
class CenaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'get_casa', 'ativa']
    list_filter = ['casa', 'ativa']
    search_fields = ['nome']
    
    def get_casa(self, obj):
        try:
            return obj.casa.nome if obj.casa else 'N/A'
        except:
            return 'N/A'
    get_casa.short_description = 'Casa'
    
    def get_queryset(self, request):
        try:
            return super().get_queryset(request).select_related('casa')
        except Exception:
            return Cena.objects.none()

@admin.register(AcaoCena)
class AcaoCenaAdmin(admin.ModelAdmin):
    list_display = ['get_cena', 'get_dispositivo', 'estado_desejado']
    list_filter = ['cena']
    search_fields = ['cena__nome']
    
    def get_cena(self, obj):
        try:
            return obj.cena.nome if obj.cena else 'N/A'
        except:
            return 'N/A'
    get_cena.short_description = 'Cena'
    
    def get_dispositivo(self, obj):
        try:
            return obj.dispositivo.nome if obj.dispositivo else 'N/A'
        except:
            return 'N/A'
    get_dispositivo.short_description = 'Dispositivo'
    
    def get_queryset(self, request):
        try:
            return super().get_queryset(request).select_related('cena', 'dispositivo')
        except Exception:
            return AcaoCena.objects.none()

@admin.register(LogDispositivo)
class LogDispositivoAdmin(admin.ModelAdmin):
    list_display = ['timestamp', 'get_dispositivo', 'estado_anterior', 'estado_novo']
    list_filter = ['timestamp']
    readonly_fields = ['timestamp']
    
    def get_dispositivo(self, obj):
        try:
            return obj.dispositivo.nome if obj.dispositivo else 'N/A'
        except:
            return 'N/A'
    get_dispositivo.short_description = 'Dispositivo'
    
    def get_queryset(self, request):
        try:
            return super().get_queryset(request).select_related('dispositivo')
        except Exception:
            return LogDispositivo.objects.none()
    
    def has_add_permission(self, request):
        return False
