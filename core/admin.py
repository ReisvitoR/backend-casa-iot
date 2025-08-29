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
    list_display = ['nome', 'usuario', 'total_comodos', 'total_dispositivos']
    list_filter = ['usuario']
    search_fields = ['nome', 'usuario__first_name', 'usuario__last_name']
    
    def total_comodos(self, obj):
        return obj.comodos.count()
    total_comodos.short_description = 'Cômodos'
    
    def total_dispositivos(self, obj):
        return sum(comodo.dispositivos.count() for comodo in obj.comodos.all())
    total_dispositivos.short_description = 'Dispositivos'

@admin.register(TipoDispositivo)
class TipoDispositivoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'categoria', 'total_dispositivos']
    list_filter = ['categoria']
    search_fields = ['nome']
    
    def total_dispositivos(self, obj):
        return obj.dispositivos.count()
    total_dispositivos.short_description = 'Qtd. Dispositivos'

@admin.register(Comodo)
class ComodoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'casa', 'total_dispositivos', 'dispositivos_online']
    list_filter = ['casa']
    search_fields = ['nome', 'casa__nome']
    
    def total_dispositivos(self, obj):
        return obj.dispositivos.count()
    total_dispositivos.short_description = 'Total Disp.'
    
    def dispositivos_online(self, obj):
        online = obj.dispositivos.filter(ativo=True).count()
        total = obj.dispositivos.count()
        if total == 0:
            return "0/0"
        color = "green" if online == total else "orange" if online > 0 else "red"
        return format_html(f'<span style="color: {color};">{online}/{total}</span>')
    dispositivos_online.short_description = 'Online/Total'

@admin.register(Dispositivo)
class DispositivoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'tipo', 'comodo', 'estado_badge', 'status_conexao_badge', 'potencia', 'ultimo_ping']
    list_filter = ['tipo', 'estado', 'ativo', 'comodo__casa', 'comodo']
    search_fields = ['nome', 'marca', 'modelo', 'ip_address']
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
    
    def estado_badge(self, obj):
        color = "green" if obj.estado else "red"
        text = "ON" if obj.estado else "OFF"
        return format_html(f'<span style="background-color: {color}; color: white; padding: 2px 8px; border-radius: 4px;">{text}</span>')
    estado_badge.short_description = 'Estado'
    
    def status_conexao_badge(self, obj):
        status = obj.status_conexao
        colors = {
            "Online": "green",
            "Instável": "orange", 
            "Offline": "red",
            "Nunca conectado": "gray"
        }
        color = colors.get(status, "gray")
        return format_html(f'<span style="color: {color}; font-weight: bold;">{status}</span>')
    status_conexao_badge.short_description = 'Conexão'

@admin.register(Cena)
class CenaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'casa', 'total_acoes', 'ativa_badge', 'favorita_badge']
    list_filter = ['casa', 'ativa', 'favorita']
    search_fields = ['nome', 'descricao', 'casa__nome']
    
    def total_acoes(self, obj):
        return obj.acoes.count()
    total_acoes.short_description = 'Ações'
    
    def ativa_badge(self, obj):
        color = "green" if obj.ativa else "gray"
        text = "SIM" if obj.ativa else "NÃO"
        return format_html(f'<span style="color: {color}; font-weight: bold;">{text}</span>')
    ativa_badge.short_description = 'Ativa'
    
    def favorita_badge(self, obj):
        if obj.favorita:
            return format_html('<i class="fas fa-star" style="color: gold;"></i>')
        return ""
    favorita_badge.short_description = 'Fav'

@admin.register(AcaoCena)
class AcaoCenaAdmin(admin.ModelAdmin):
    list_display = ['cena', 'ordem', 'dispositivo', 'estado_desejado_badge', 'intervalo_tempo', 'condicional_badge']
    list_filter = ['cena__casa', 'cena', 'estado_desejado', 'condicional']
    search_fields = ['cena__nome', 'dispositivo__nome']
    ordering = ['cena', 'ordem']
    
    def estado_desejado_badge(self, obj):
        color = "green" if obj.estado_desejado else "red"
        text = "LIGAR" if obj.estado_desejado else "DESLIGAR"
        return format_html(f'<span style="color: {color}; font-weight: bold;">{text}</span>')
    estado_desejado_badge.short_description = 'Ação'
    
    def condicional_badge(self, obj):
        color = "orange" if obj.condicional else "blue"
        text = "CONDICIONAL" if obj.condicional else "SEMPRE"
        return format_html(f'<span style="color: {color}; font-weight: bold;">{text}</span>')
    condicional_badge.short_description = 'Tipo'

@admin.register(LogDispositivo)
class LogDispositivoAdmin(admin.ModelAdmin):
    list_display = ['timestamp', 'dispositivo', 'mudanca_estado_badge', 'origem_badge', 'usuario', 'cena']
    list_filter = ['origem', 'timestamp', 'dispositivo__comodo__casa']
    search_fields = ['dispositivo__nome', 'usuario__first_name', 'cena__nome']
    readonly_fields = ['timestamp']
    date_hierarchy = 'timestamp'
    
    def mudanca_estado_badge(self, obj):
        anterior = '<i class="fas fa-circle" style="color: green;"></i>' if obj.estado_anterior else '<i class="fas fa-circle" style="color: red;"></i>'
        novo = '<i class="fas fa-circle" style="color: green;"></i>' if obj.estado_novo else '<i class="fas fa-circle" style="color: red;"></i>'
        return format_html(f'{anterior} <i class="fas fa-arrow-right"></i> {novo}')
    mudanca_estado_badge.short_description = 'Mudança'
    
    def origem_badge(self, obj):
        colors = {
            'manual': 'blue',
            'cena': 'green',
            'api': 'orange',
            'automacao': 'purple',
        }
        color = colors.get(obj.origem, 'gray')
        return format_html(f'<span style="color: {color}; font-weight: bold;">{obj.origem.upper()}</span>')
    origem_badge.short_description = 'Origem'
    
    def has_add_permission(self, request):
        return False  # Logs são criados automaticamente
