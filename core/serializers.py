from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import *

class UsuarioSerializer(serializers.ModelSerializer):
    total_casas = serializers.SerializerMethodField()
    
    class Meta:
        model = Usuario
        fields = ['id', 'email', 'first_name', 'last_name', 'total_casas', 'date_joined']
        read_only_fields = ['date_joined']
    
    def get_total_casas(self, obj):
        return obj.casas.count()

class TipoDispositivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDispositivo
        fields = '__all__'

class CasaSerializer(serializers.ModelSerializer):
    total_comodos = serializers.SerializerMethodField()
    total_dispositivos = serializers.SerializerMethodField()
    usuario_nome = serializers.CharField(source='usuario.first_name', read_only=True)
    
    class Meta:
        model = Casa
        fields = ['id', 'nome', 'endereco', 'timezone', 'usuario', 'usuario_nome', 
                 'total_comodos', 'total_dispositivos']
    
    def get_total_comodos(self, obj):
        return obj.comodos.count()
    
    def get_total_dispositivos(self, obj):
        return sum(comodo.dispositivos.count() for comodo in obj.comodos.all())

class DispositivoSimpleSerializer(serializers.ModelSerializer):
    """Serializer simplificado para uso em listas"""
    tipo_nome = serializers.CharField(source='tipo.nome', read_only=True)
    status_conexao = serializers.ReadOnlyField()
    
    class Meta:
        model = Dispositivo
        fields = ['id', 'nome', 'estado', 'tipo_nome', 'status_conexao', 'ativo']

class ComodoSerializer(serializers.ModelSerializer):
    dispositivos = DispositivoSimpleSerializer(many=True, read_only=True)
    total_dispositivos = serializers.SerializerMethodField()
    casa_nome = serializers.CharField(source='casa.nome', read_only=True)
    
    class Meta:
        model = Comodo
        fields = ['id', 'nome', 'background_url', 'casa', 'casa_nome', 
                 'dispositivos', 'total_dispositivos']
    
    def get_total_dispositivos(self, obj):
        return obj.dispositivos.count()

class DispositivoSerializer(serializers.ModelSerializer):
    tipo_nome = serializers.CharField(source='tipo.nome', read_only=True)
    tipo_categoria = serializers.CharField(source='tipo.categoria', read_only=True)
    comodo_nome = serializers.CharField(source='comodo.nome', read_only=True)
    casa_nome = serializers.CharField(source='comodo.casa.nome', read_only=True)
    status_conexao = serializers.ReadOnlyField()
    
    class Meta:
        model = Dispositivo
        fields = ['id', 'nome', 'estado', 'tipo', 'tipo_nome', 'tipo_categoria', 
                 'comodo', 'comodo_nome', 'casa_nome', 'ativo', 'status_conexao']

class AcaoCenaSerializer(serializers.ModelSerializer):
    dispositivo_nome = serializers.CharField(source='dispositivo.nome', read_only=True)
    dispositivo_comodo = serializers.CharField(source='dispositivo.comodo.nome', read_only=True)
    
    class Meta:
        model = AcaoCena
        fields = ['id', 'ordem', 'intervalo_tempo', 'estado_desejado', 'dispositivo', 
                 'dispositivo_nome', 'dispositivo_comodo', 'cena', 'condicional']

class CenaSerializer(serializers.ModelSerializer):
    acoes = AcaoCenaSerializer(many=True, read_only=True)
    total_acoes = serializers.SerializerMethodField()
    casa_nome = serializers.CharField(source='casa.nome', read_only=True)
    pode_executar = serializers.ReadOnlyField()
    status_disponibilidade = serializers.ReadOnlyField()
    
    class Meta:
        model = Cena
        fields = ['id', 'nome', 'descricao', 'ativa', 'casa', 'casa_nome', 
                 'indisponivel_ate', 'favorita', 'acoes', 'total_acoes',
                 'pode_executar', 'status_disponibilidade']
    
    def get_total_acoes(self, obj):
        return obj.acoes.count()

class LogDispositivoSerializer(serializers.ModelSerializer):
    dispositivo_nome = serializers.CharField(source='dispositivo.nome', read_only=True)
    usuario_nome = serializers.CharField(source='usuario.first_name', read_only=True)
    cena_nome = serializers.CharField(source='cena.nome', read_only=True)
    
    class Meta:
        model = LogDispositivo
        fields = ['id', 'dispositivo', 'dispositivo_nome', 'estado_anterior', 
                 'estado_novo', 'origem', 'usuario', 'usuario_nome', 'cena', 
                 'cena_nome', 'timestamp']
        read_only_fields = ['timestamp']

# Serializers para autenticação
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    
    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        
        if email and password:
            user = authenticate(username=email, password=password)
            if not user:
                raise serializers.ValidationError("Credenciais inválidas")
            if not user.is_active:
                raise serializers.ValidationError("Conta desativada")
            data['user'] = user
        else:
            raise serializers.ValidationError("Email e senha são obrigatórios")
        
        return data
