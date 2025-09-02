from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from core.models import *

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    list_display = ['email', 'first_name', 'last_name', 'is_active', 'date_joined']
    list_filter = ['is_active', 'is_staff', 'date_joined']
    search_fields = ['email', 'first_name', 'last_name']
    ordering = ['-date_joined']

@admin.register(Casa)
class CasaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'usuario', 'endereco']
    list_filter = ['usuario']
    search_fields = ['nome', 'usuario__first_name', 'usuario__last_name']
    fields = ['nome', 'usuario', 'endereco', 'timezone']

@admin.register(TipoDispositivo)
class TipoDispositivoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'categoria', 'icone']
    list_filter = ['categoria']
    search_fields = ['nome']
    fields = ['nome', 'categoria', 'icone']

@admin.register(Comodo)
class ComodoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'casa', 'background_url']
    list_filter = ['casa']
    search_fields = ['nome', 'casa__nome']
    fields = ['nome', 'casa', 'background_url']

@admin.register(Dispositivo)
class DispositivoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'tipo', 'comodo', 'estado', 'ativo']
    list_filter = ['tipo', 'estado', 'ativo', 'comodo__casa']
    search_fields = ['nome', 'marca', 'modelo']
    readonly_fields = ['status_conexao']
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('nome', 'tipo', 'comodo', 'estado', 'ativo')
        }),
        ('Especificações Técnicas', {
            'fields': ('potencia', 'marca', 'modelo')
        }),
        ('Conectividade', {
            'fields': ('ip_address', 'mac_address', 'ultimo_ping', 'status_conexao')
        }),
    )

@admin.register(Cena)
class CenaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'casa', 'ativa', 'favorita']
    list_filter = ['casa', 'ativa', 'favorita']
    search_fields = ['nome', 'descricao']
    fields = ['nome', 'casa', 'descricao', 'ativa', 'favorita', 'indisponivel_ate', 'tempo_execucao']

@admin.register(AcaoCena)
class AcaoCenaAdmin(admin.ModelAdmin):
    list_display = ['cena', 'ordem', 'dispositivo', 'estado_desejado']
    list_filter = ['cena__casa', 'cena', 'estado_desejado']
    search_fields = ['cena__nome', 'dispositivo__nome']
    ordering = ['cena', 'ordem']
    fields = ['cena', 'dispositivo', 'estado_desejado', 'ordem', 'intervalo_tempo', 'condicional']

@admin.register(LogDispositivo)
class LogDispositivoAdmin(admin.ModelAdmin):
    list_display = ['timestamp', 'dispositivo', 'estado_anterior', 'estado_novo', 'origem']
    list_filter = ['origem', 'timestamp', 'dispositivo__comodo__casa']
    search_fields = ['dispositivo__nome']
    readonly_fields = ['timestamp']
    date_hierarchy = 'timestamp'
    
    def has_add_permission(self, request):
        return False  # Logs são criados automaticamente
