from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
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

class UsuarioViewSet(viewsets.ModelViewSet):
    """API para gerenciamento de usuários"""
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    # Autenticação removida - acesso livre
    
    @action(detail=False, methods=['get'])
    def me(self, request):
        """Retorna dados do primeiro usuário (sem autenticação)"""
        primeiro_usuario = Usuario.objects.first()
        if primeiro_usuario:
            serializer = UsuarioSerializer(primeiro_usuario)
            return Response(serializer.data)
        return Response({'error': 'Nenhum usuário encontrado'}, status=404)

class CasaViewSet(viewsets.ModelViewSet):
    """API para gerenciamento de casas"""
    queryset = Casa.objects.all()
    serializer_class = CasaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["usuario"]
    
    def get_queryset(self):
        # Filtra por usuário se especificado na query
        queryset = Casa.objects.all()
        usuario_id = self.request.query_params.get('usuario', None)
        if usuario_id:
            queryset = queryset.filter(usuario_id=usuario_id)
        return queryset
    
    def perform_create(self, serializer):
        # Sem autenticação: associa ao primeiro usuário ou cria um padrão
        from .models import Usuario
        primeiro_usuario = Usuario.objects.first()
        if not primeiro_usuario:
            # Cria um usuário padrão se não existir nenhum
            primeiro_usuario = Usuario.objects.create_user(
                username='usuario_padrao',
                email='padrao@casaiot.com',
                first_name='Usuário',
                last_name='Padrão'
            )
        serializer.save(usuario=primeiro_usuario)
    
    @action(detail=True, methods=['get'])
    def status(self, request, pk=None):
        """Status completo da casa com dispositivos e cenas"""
        try:
            casa = self.get_object()
            
            # Dispositivos por cômodo
            comodos_status = []
            for comodo in casa.comodos.all():
                dispositivos = comodo.dispositivos.all()
                comodos_status.append({
                    'id': comodo.id,
                    'nome': comodo.nome,
                    'total_dispositivos': dispositivos.count(),
                    'dispositivos_ligados': dispositivos.filter(estado=True).count(),
                    'dispositivos_ativos': dispositivos.filter(ativo=True).count(),
                    'dispositivos': [
                        {
                            'id': d.id,
                            'nome': d.nome,
                            'estado': 'ligado' if d.estado else 'desligado',
                            'ativo': d.ativo,
                            'tipo': d.tipo.nome if d.tipo else None
                        } for d in dispositivos
                    ]
                })
            
            # Cenas da casa
            cenas = casa.cenas.all()
            cenas_ativas = cenas.filter(ativa=True)
            
            return Response({
                'casa': {
                    'id': casa.id,
                    'nome': casa.nome,
                    'endereco': casa.endereco or ''
                },
                'resumo': {
                    'total_comodos': casa.comodos.count(),
                    'total_dispositivos': sum(c['total_dispositivos'] for c in comodos_status),
                    'dispositivos_ligados': sum(c['dispositivos_ligados'] for c in comodos_status),
                    'total_cenas': cenas.count(),
                    'cenas_ativas': cenas_ativas.count()
                },
                'comodos': comodos_status,
                'cenas': [
                    {
                        'id': c.id,
                        'nome': c.nome,
                        'ativa': c.ativa,
                        'favorita': c.favorita,
                        'pode_executar': c.pode_executar,
                        'status': c.status_disponibilidade
                    } for c in cenas
                ]
            })
        except Exception as e:
            return Response({'error': str(e)}, status=500)

class ComodoViewSet(viewsets.ModelViewSet):
    """API para gerenciamento de cômodos"""
    queryset = Comodo.objects.all()
    serializer_class = ComodoSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["casa"]
    
    def get_queryset(self):
        
        return Comodo.objects.all()
   
    
    @action(detail=True, methods=['post'])
    def toggle_all(self, request, pk=None):
        """Liga/desliga todos os dispositivos do cômodo"""
        comodo = self.get_object()
        estado = request.data.get('estado', True)
        
        dispositivos_alterados = []
        for dispositivo in comodo.dispositivos.filter(ativo=True):
            if dispositivo.estado != estado:
                # Registra log (sem usuário, já que não há autenticação)
                LogDispositivo.objects.create(
                    dispositivo=dispositivo,
                    estado_anterior=dispositivo.estado,
                    estado_novo=estado,
                    origem='api',
                    usuario=None  # Sem autenticação
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
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["categoria"]

class DispositivoViewSet(viewsets.ModelViewSet):
    """API para gerenciamento de dispositivos"""
    queryset = Dispositivo.objects.all()
    serializer_class = DispositivoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["comodo", "tipo", "estado", "ativo"]
    
    def get_queryset(self):
        # Filtra dispositivos por usuário se especificado
        queryset = Dispositivo.objects.all()
        usuario_id = self.request.query_params.get('usuario', None)
        if usuario_id:
            queryset = queryset.filter(comodo__casa__usuario_id=usuario_id)
        return queryset
    
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
        
        # Registra log (sem usuário, já que não há autenticação)
        LogDispositivo.objects.create(
            dispositivo=dispositivo,
            estado_anterior=estado_anterior,
            estado_novo=dispositivo.estado,
            origem='api',
            usuario=None  # Sem autenticação
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
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["casa", "ativa", "favorita"]
    
    def get_queryset(self):
        # Filtra cenas por usuário se especificado
        queryset = Cena.objects.all()
        usuario_id = self.request.query_params.get('usuario', None)
        if usuario_id:
            queryset = queryset.filter(casa__usuario_id=usuario_id)
        return queryset
    
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
            
            
            if acao.condicional and dispositivo.estado == acao.estado_desejado:
                continue
            
            
            # Registra log (sem usuário, já que não há autenticação)
            LogDispositivo.objects.create(
                dispositivo=dispositivo,
                estado_anterior=dispositivo.estado,
                estado_novo=acao.estado_desejado,
                origem='cena',
                usuario=None,  # Sem autenticação
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
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["cena", "dispositivo"]
    
    def get_queryset(self):
        # Filtra ações por usuário se especificado
        queryset = AcaoCena.objects.all()
        usuario_id = self.request.query_params.get('usuario', None)
        if usuario_id:
            queryset = queryset.filter(cena__casa__usuario_id=usuario_id)
        return queryset

class LogDispositivoViewSet(viewsets.ReadOnlyModelViewSet):
    """API para visualização de logs (somente leitura)"""
    queryset = LogDispositivo.objects.all()
    serializer_class = LogDispositivoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["dispositivo", "origem", "usuario", "cena"]
    
    def get_queryset(self):
        # Filtra logs por usuário se especificado
        queryset = LogDispositivo.objects.all()
        usuario_id = self.request.query_params.get('usuario', None)
        if usuario_id:
            queryset = queryset.filter(dispositivo__comodo__casa__usuario_id=usuario_id)
        return queryset
