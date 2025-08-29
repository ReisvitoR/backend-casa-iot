from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.utils import timezone
from django.db.models import Count, Q
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import *
from .serializers import *

def index(request):
    """Página inicial do sistema"""
    return render(request, 'core/index.html')

class CustomAuthToken(ObtainAuthToken):
    """Autenticação customizada que retorna informações do usuário"""
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                          context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user': UsuarioSerializer(user).data
        })

class UsuarioViewSet(viewsets.ModelViewSet):
    """API para gerenciamento de usuários"""
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    @action(detail=False, methods=['get'])
    def me(self, request):
        """Retorna dados do usuário logado"""
        serializer = UsuarioSerializer(request.user)
        return Response(serializer.data)

class CasaViewSet(viewsets.ModelViewSet):
    """API para gerenciamento de casas"""
    queryset = Casa.objects.all()
    serializer_class = CasaSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["usuario"]
    
    def get_queryset(self):
        # Usuários só veem suas próprias casas
        return Casa.objects.filter(usuario=self.request.user)
    
    def perform_create(self, serializer):
        # Associa automaticamente ao usuário logado
        serializer.save(usuario=self.request.user)

class ComodoViewSet(viewsets.ModelViewSet):
    """API para gerenciamento de cômodos"""
    queryset = Comodo.objects.all()
    serializer_class = ComodoSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["casa"]
    
    def get_queryset(self):
        # Usuários só veem cômodos de suas casas
        return Comodo.objects.filter(casa__usuario=self.request.user)
    
    @action(detail=True, methods=['post'])
    def toggle_all(self, request, pk=None):
        """Liga/desliga todos os dispositivos do cômodo"""
        comodo = self.get_object()
        estado = request.data.get('estado', True)
        
        dispositivos_alterados = []
        for dispositivo in comodo.dispositivos.filter(ativo=True):
            if dispositivo.estado != estado:
                # Registra log
                LogDispositivo.objects.create(
                    dispositivo=dispositivo,
                    estado_anterior=dispositivo.estado,
                    estado_novo=estado,
                    origem='api',
                    usuario=request.user
                )
                dispositivo.estado = estado
                dispositivo.save()
                dispositivos_alterados.append(dispositivo.nome)
        
        return Response({
            'message': f'Estado alterado para {"ligado" if estado else "desligado"}',
            'dispositivos_alterados': dispositivos_alterados,
            'total_alterados': len(dispositivos_alterados)
        })

class TipoDispositivoViewSet(viewsets.ModelViewSet):
    """API para tipos de dispositivos"""
    queryset = TipoDispositivo.objects.all()
    serializer_class = TipoDispositivoSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["categoria"]

class DispositivoViewSet(viewsets.ModelViewSet):
    """API para gerenciamento de dispositivos"""
    queryset = Dispositivo.objects.all()
    serializer_class = DispositivoSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["comodo", "tipo", "estado", "ativo"]
    
    def get_queryset(self):
        # Usuários só veem dispositivos de suas casas
        return Dispositivo.objects.filter(comodo__casa__usuario=self.request.user)
    
    @action(detail=True, methods=['post'])
    def toggle(self, request, pk=None):
        """Liga/desliga um dispositivo"""
        dispositivo = self.get_object()
        
        if not dispositivo.ativo:
            return Response({
                'error': 'Dispositivo está inativo'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        estado_anterior = dispositivo.estado
        dispositivo.estado = not dispositivo.estado
        dispositivo.ultimo_ping = timezone.now()
        dispositivo.save()
        
        # Registra log
        LogDispositivo.objects.create(
            dispositivo=dispositivo,
            estado_anterior=estado_anterior,
            estado_novo=dispositivo.estado,
            origem='api',
            usuario=request.user
        )
        
        return Response({
            'message': f'Dispositivo {"ligado" if dispositivo.estado else "desligado"}',
            'estado': dispositivo.estado,
            'dispositivo': DispositivoSerializer(dispositivo).data
        })

    @action(detail=True, methods=['post'])
    def toggle_ativo(self, request, pk=None):
        """Ativa/desativa um dispositivo"""
        dispositivo = self.get_object()
        dispositivo.ativo = not dispositivo.ativo
        dispositivo.save()
        
        return Response({
            'message': f'Dispositivo {"ativado" if dispositivo.ativo else "desativado"}',
            'ativo': dispositivo.ativo,
            'dispositivo': DispositivoSerializer(dispositivo).data
        })

    @action(detail=False, methods=['get'])
    def status_geral(self, request):
        """Status geral de todos os dispositivos do usuário"""
        dispositivos = self.get_queryset()
        
        return Response({
            'total_dispositivos': dispositivos.count(),
            'ativos': dispositivos.filter(ativo=True).count(),
            'inativos': dispositivos.filter(ativo=False).count(),
            'ligados': dispositivos.filter(estado=True, ativo=True).count(),
            'desligados': dispositivos.filter(estado=False, ativo=True).count(),
            'por_tipo': dispositivos.values('tipo__nome').annotate(
                total=Count('id'),
                ativos=Count('id', filter=Q(ativo=True)),
                ligados=Count('id', filter=Q(estado=True, ativo=True))
            )
        })

class CenaViewSet(viewsets.ModelViewSet):
    """API para gerenciamento de cenas"""
    queryset = Cena.objects.all()
    serializer_class = CenaSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["casa", "ativa", "favorita"]
    
    def get_queryset(self):
        # Usuários só veem cenas de suas casas
        return Cena.objects.filter(casa__usuario=self.request.user)
    
    @action(detail=True, methods=['post'])
    def executar(self, request, pk=None):
        """Executa uma cena"""
        cena = self.get_object()
        
        # Verifica se a cena pode ser executada
        if not cena.pode_executar:
            if not cena.ativa:
                return Response({
                    'error': 'Cena está inativa',
                    'status': 'inativa'
                }, status=status.HTTP_400_BAD_REQUEST)
            elif cena.indisponivel_ate and cena.indisponivel_ate > timezone.now():
                return Response({
                    'error': f'Cena temporariamente indisponível até {cena.indisponivel_ate}',
                    'disponivel_em': cena.indisponivel_ate,
                    'status': 'temporariamente_indisponivel'
                }, status=status.HTTP_400_BAD_REQUEST)
        
        # Executa as ações
        acoes_executadas = []
        inicio_execucao = timezone.now()
        
        for acao in cena.acoes.order_by('ordem'):
            dispositivo = acao.dispositivo
            
            # Pula dispositivos inativos
            if not dispositivo.ativo:
                continue
            
            # Verifica se é condicional
            if acao.condicional and dispositivo.estado == acao.estado_desejado:
                continue
            
            # Registra log
            LogDispositivo.objects.create(
                dispositivo=dispositivo,
                estado_anterior=dispositivo.estado,
                estado_novo=acao.estado_desejado,
                origem='cena',
                usuario=request.user,
                cena=cena
            )
            
            dispositivo.estado = acao.estado_desejado
            dispositivo.ultimo_ping = timezone.now()
            dispositivo.save()
            
            acoes_executadas.append({
                'dispositivo': dispositivo.nome,
                'estado': acao.estado_desejado,
                'ordem': acao.ordem
            })
        
        # Atualiza tempo de execução da cena
        tempo_execucao = (timezone.now() - inicio_execucao).total_seconds()
        cena.tempo_execucao = tempo_execucao
        cena.save()
        
        return Response({
            'message': f'Cena "{cena.nome}" executada com sucesso',
            'acoes_executadas': acoes_executadas,
            'tempo_execucao': tempo_execucao,
            'total_acoes': len(acoes_executadas),
            'status': cena.status_disponibilidade
        })
    
    @action(detail=True, methods=['post'])
    def toggle_favorita(self, request, pk=None):
        """Marca/desmarca cena como favorita"""
        cena = self.get_object()
        cena.favorita = not cena.favorita
        cena.save()
        
        return Response({
            'message': f'Cena {"marcada" if cena.favorita else "desmarcada"} como favorita',
            'favorita': cena.favorita
        })

    @action(detail=True, methods=['post'])
    def toggle_ativa(self, request, pk=None):
        """Ativa/desativa uma cena"""
        cena = self.get_object()
        cena.ativa = not cena.ativa
        cena.save()
        
        return Response({
            'message': f'Cena {"ativada" if cena.ativa else "desativada"}',
            'ativa': cena.ativa,
            'status': cena.status_disponibilidade
        })

    @action(detail=True, methods=['post'])
    def desativar_temporariamente(self, request, pk=None):
        """Desativa uma cena temporariamente"""
        cena = self.get_object()
        minutos = request.data.get('minutos', 60)  # padrão 1 hora
        
        cena.indisponivel_ate = timezone.now() + timezone.timedelta(minutes=minutos)
        cena.save()
        
        return Response({
            'message': f'Cena desativada temporariamente por {minutos} minutos',
            'indisponivel_ate': cena.indisponivel_ate,
            'status': cena.status_disponibilidade
        })

    @action(detail=True, methods=['post'])
    def reativar(self, request, pk=None):
        """Reativa uma cena removendo a restrição temporal"""
        cena = self.get_object()
        cena.indisponivel_ate = None
        cena.save()
        
        return Response({
            'message': 'Cena reativada',
            'status': cena.status_disponibilidade
        })

    @action(detail=False, methods=['get'])
    def status_geral(self, request):
        """Retorna status geral de todas as cenas do usuário"""
        cenas = self.get_queryset()
        
        return Response({
            'total_cenas': cenas.count(),
            'ativas': cenas.filter(ativa=True).count(),
            'inativas': cenas.filter(ativa=False).count(),
            'temporariamente_indisponiveis': cenas.filter(
                indisponivel_ate__gt=timezone.now()
            ).count(),
            'favoritas': cenas.filter(favorita=True).count(),
            'por_status': {
                'disponivel': len([c for c in cenas if c.status_disponibilidade == 'disponivel']),
                'inativa': len([c for c in cenas if c.status_disponibilidade == 'inativa']),
                'temporariamente_indisponivel': len([c for c in cenas if c.status_disponibilidade == 'temporariamente_indisponivel'])
            }
        })

class AcaoCenaViewSet(viewsets.ModelViewSet):
    """API para gerenciamento de ações de cenas"""
    queryset = AcaoCena.objects.all()
    serializer_class = AcaoCenaSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["cena", "dispositivo"]
    
    def get_queryset(self):
        # Usuários só veem ações de cenas de suas casas
        return AcaoCena.objects.filter(cena__casa__usuario=self.request.user)

class LogDispositivoViewSet(viewsets.ReadOnlyModelViewSet):
    """API para visualização de logs (somente leitura)"""
    queryset = LogDispositivo.objects.all()
    serializer_class = LogDispositivoSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["dispositivo", "origem", "usuario", "cena"]
    
    def get_queryset(self):
        # Usuários só veem logs de suas casas
        return LogDispositivo.objects.filter(
            dispositivo__comodo__casa__usuario=self.request.user
        )
