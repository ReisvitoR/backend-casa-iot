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
    list_per_page = 25  # Paginação menor para carregar mais rápido

@admin.register(Casa)
class CasaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'usuario']
    list_filter = ['usuario']
    search_fields = ['nome', 'usuario__first_name', 'usuario__last_name']

@admin.register(TipoDispositivo)
class TipoDispositivoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'categoria']
    list_filter = ['categoria']
    search_fields = ['nome']

@admin.register(Comodo)
class ComodoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'casa', 'total_dispositivos', 'dispositivos_online']
    list_filter = ['casa']
    search_fields = ['nome', 'casa__nome']
    list_select_related = ['casa']
    list_per_page = 20
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('casa').prefetch_related('dispositivos')
    
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
    list_display = ['nome', 'tipo', 'comodo', 'estado_badge', 'status_conexao_badge']
    list_filter = ['tipo', 'estado', 'ativo', 'comodo__casa', 'comodo']
    search_fields = ['nome', 'marca', 'modelo']
    readonly_fields = ['status_conexao']
    list_select_related = ['tipo', 'comodo', 'comodo__casa']  # Otimização
    list_per_page = 25
    
    # Remover campos pesados dos list_display para melhor performance
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
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('tipo', 'comodo', 'comodo__casa')
    
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
    list_display = ['nome', 'casa', 'ativa', 'favorita']
    list_filter = ['casa', 'ativa', 'favorita']
    search_fields = ['nome', 'descricao']
    
    # Formulário simplificado
    fields = ['nome', 'casa', 'descricao', 'ativa', 'favorita']

@admin.register(AcaoCena)
class AcaoCenaAdmin(admin.ModelAdmin):
    list_display = ['cena', 'ordem', 'dispositivo', 'estado_desejado_badge']
    list_filter = ['cena__casa', 'cena', 'estado_desejado']
    search_fields = ['cena__nome', 'dispositivo__nome']
    ordering = ['cena', 'ordem']
    list_select_related = ['cena', 'dispositivo', 'cena__casa']
    list_per_page = 30
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('cena', 'dispositivo', 'cena__casa')
    
    def estado_desejado_badge(self, obj):
        color = "green" if obj.estado_desejado else "red"
        text = "LIGAR" if obj.estado_desejado else "DESLIGAR"
        return format_html(f'<span style="color: {color}; font-weight: bold;">{text}</span>')
    estado_desejado_badge.short_description = 'Ação'

@admin.register(LogDispositivo)
class LogDispositivoAdmin(admin.ModelAdmin):
    list_display = ['timestamp', 'dispositivo', 'mudanca_estado_badge', 'origem_badge']
    list_filter = ['origem', 'timestamp', 'dispositivo__comodo__casa']
    search_fields = ['dispositivo__nome']
    readonly_fields = ['timestamp']
    date_hierarchy = 'timestamp'
    list_select_related = ['dispositivo', 'dispositivo__comodo', 'dispositivo__comodo__casa']
    list_per_page = 50  # Logs podem ter mais itens por página
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related(
            'dispositivo', 'dispositivo__comodo', 'dispositivo__comodo__casa'
        ).order_by('-timestamp')
    
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
