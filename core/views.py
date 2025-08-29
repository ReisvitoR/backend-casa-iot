from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.utils import timezone
from django.db.models import Count, Q
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from .models import *
from .serializers import *

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
    
    @action(detail=True, methods=['get'])
    def dashboard(self, request, pk=None):
        """Dashboard com estatísticas da casa"""
        casa = self.get_object()
        
        total_comodos = casa.comodos.count()
        total_dispositivos = sum(c.dispositivos.count() for c in casa.comodos.all())
        dispositivos_ligados = sum(c.dispositivos.filter(estado=True).count() for c in casa.comodos.all())
        dispositivos_online = sum(c.dispositivos.filter(
            ultimo_ping__gte=timezone.now() - timezone.timedelta(minutes=5)
        ).count() for c in casa.comodos.all())
        
        total_cenas = casa.cenas.count()
        cenas_ativas = casa.cenas.filter(ativa=True).count()
        
        return Response({
            'casa': CasaSerializer(casa).data,
            'estatisticas': {
                'total_comodos': total_comodos,
                'total_dispositivos': total_dispositivos,
                'dispositivos_ligados': dispositivos_ligados,
                'dispositivos_online': dispositivos_online,
                'total_cenas': total_cenas,
                'cenas_ativas': cenas_ativas,
                'consumo_estimado': self.calcular_consumo_estimado(casa),
            }
        })
    
    def calcular_consumo_estimado(self, casa):
        """Calcula consumo estimado em kWh"""
        consumo = 0
        for comodo in casa.comodos.all():
            for dispositivo in comodo.dispositivos.filter(estado=True):
                if dispositivo.potencia:
                    consumo += dispositivo.potencia / 1000  # Convert W to kW
        return round(consumo, 2)

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
    def ping(self, request, pk=None):
        """Atualiza último ping do dispositivo"""
        dispositivo = self.get_object()
        dispositivo.ultimo_ping = timezone.now()
        dispositivo.save()
        
        return Response({
            'message': 'Ping atualizado',
            'ultimo_ping': dispositivo.ultimo_ping,
            'status_conexao': dispositivo.status_conexao
        })
    
    @action(detail=False, methods=['get'])
    def status_geral(self, request):
        """Status geral de todos os dispositivos do usuário"""
        dispositivos = self.get_queryset()
        
        total = dispositivos.count()
        ligados = dispositivos.filter(estado=True).count()
        online = dispositivos.filter(
            ultimo_ping__gte=timezone.now() - timezone.timedelta(minutes=5)
        ).count()
        inativos = dispositivos.filter(ativo=False).count()
        
        return Response({
            'total_dispositivos': total,
            'dispositivos_ligados': ligados,
            'dispositivos_online': online,
            'dispositivos_inativos': inativos,
            'por_tipo': dispositivos.values('tipo__nome').annotate(
                total=Count('id'),
                ligados=Count('id', filter=Q(estado=True))
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
        if cena.indisponivel_ate and cena.indisponivel_ate > timezone.now():
            return Response({
                'error': f'Cena indisponível até {cena.indisponivel_ate}',
                'disponivel_em': cena.indisponivel_ate
            }, status=status.HTTP_400_BAD_REQUEST)
        
        # Executa as ações
        acoes_executadas = []
        inicio_execucao = timezone.now()
        
        for acao in cena.acoes.order_by('ordem'):
            dispositivo = acao.dispositivo
            
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
            'total_acoes': len(acoes_executadas)
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
