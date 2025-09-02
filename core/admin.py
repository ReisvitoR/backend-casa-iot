from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from core.models import *

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    list_display = ['email', 'first_name', 'last_name', 'is_active']
    list_filter = ['is_active', 'is_staff']
    search_fields = ['email', 'first_name', 'last_name']

@admin.register(Casa)
class CasaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'usuario', 'endereco']
    list_filter = ['usuario']
    search_fields = ['nome']

@admin.register(TipoDispositivo)
class TipoDispositivoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'categoria']
    list_filter = ['categoria']
    search_fields = ['nome']

@admin.register(Comodo)
class ComodoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'casa']
    list_filter = ['casa']
    search_fields = ['nome']

@admin.register(Dispositivo)
class DispositivoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'tipo', 'comodo', 'estado', 'ativo']
    list_filter = ['tipo', 'estado', 'ativo']
    search_fields = ['nome']

@admin.register(Cena)
class CenaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'casa', 'ativa']
    list_filter = ['casa', 'ativa']
    search_fields = ['nome']

@admin.register(AcaoCena)
class AcaoCenaAdmin(admin.ModelAdmin):
    list_display = ['cena', 'dispositivo', 'estado_desejado']
    list_filter = ['cena']
    search_fields = ['cena__nome']

@admin.register(LogDispositivo)
class LogDispositivoAdmin(admin.ModelAdmin):
    list_display = ['timestamp', 'dispositivo', 'estado_anterior', 'estado_novo']
    list_filter = ['timestamp']
    readonly_fields = ['timestamp']
    
    def has_add_permission(self, request):
        return False
