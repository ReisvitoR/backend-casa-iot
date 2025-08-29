from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import *

class UsuarioSerializer(serializers.ModelSerializer):
    total_casas = serializers.SerializerMethodField()
    total_dispositivos = serializers.SerializerMethodField()
    
    class Meta:
        model = Usuario
        fields = ['id', 'email', 'first_name', 'last_name', 'total_casas', 'total_dispositivos', 'date_joined']
        read_only_fields = ['date_joined']
    
    def get_total_casas(self, obj):
        return obj.casas.count()
    
    def get_total_dispositivos(self, obj):
        return sum(casa.comodos.all().aggregate(
            total=models.Count('dispositivos')
        )['total'] or 0 for casa in obj.casas.all())

class TipoDispositivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDispositivo
        fields = '__all__'

class CasaSerializer(serializers.ModelSerializer):
    total_comodos = serializers.SerializerMethodField()
    total_dispositivos = serializers.SerializerMethodField()
    dispositivos_online = serializers.SerializerMethodField()
    usuario_nome = serializers.CharField(source='usuario.first_name', read_only=True)
    
    class Meta:
        model = Casa
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']
    
    def get_total_comodos(self, obj):
        return obj.comodos.count()
    
    def get_total_dispositivos(self, obj):
        return sum(comodo.dispositivos.count() for comodo in obj.comodos.all())
    
    def get_dispositivos_online(self, obj):
        total = 0
        online = 0
        for comodo in obj.comodos.all():
            for dispositivo in comodo.dispositivos.all():
                total += 1
                if dispositivo.status_conexao == "Online":
                    online += 1
        return {"online": online, "total": total}

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
    dispositivos_ligados = serializers.SerializerMethodField()
    casa_nome = serializers.CharField(source='casa.nome', read_only=True)
    
    class Meta:
        model = Comodo
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']
    
    def get_total_dispositivos(self, obj):
        return obj.dispositivos.count()
    
    def get_dispositivos_ligados(self, obj):
        return obj.dispositivos.filter(estado=True).count()

class DispositivoSerializer(serializers.ModelSerializer):
    tipo_nome = serializers.CharField(source='tipo.nome', read_only=True)
    tipo_categoria = serializers.CharField(source='tipo.categoria', read_only=True)
    comodo_nome = serializers.CharField(source='comodo.nome', read_only=True)
    casa_nome = serializers.CharField(source='comodo.casa.nome', read_only=True)
    status_conexao = serializers.ReadOnlyField()
    
    class Meta:
        model = Dispositivo
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at', 'ultimo_ping']

class AcaoCenaSerializer(serializers.ModelSerializer):
    dispositivo_nome = serializers.CharField(source='dispositivo.nome', read_only=True)
    dispositivo_comodo = serializers.CharField(source='dispositivo.comodo.nome', read_only=True)
    
    class Meta:
        model = AcaoCena
        fields = '__all__'
        read_only_fields = ['created_at']

class CenaSerializer(serializers.ModelSerializer):
    acoes = AcaoCenaSerializer(many=True, read_only=True)
    total_acoes = serializers.SerializerMethodField()
    casa_nome = serializers.CharField(source='casa.nome', read_only=True)
    pode_executar = serializers.SerializerMethodField()
    
    class Meta:
        model = Cena
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']
    
    def get_total_acoes(self, obj):
        return obj.acoes.count()
    
    def get_pode_executar(self, obj):
        from django.utils import timezone
        if obj.indisponivel_ate and obj.indisponivel_ate > timezone.now():
            return False
        return True

class LogDispositivoSerializer(serializers.ModelSerializer):
    dispositivo_nome = serializers.CharField(source='dispositivo.nome', read_only=True)
    usuario_nome = serializers.CharField(source='usuario.first_name', read_only=True)
    cena_nome = serializers.CharField(source='cena.nome', read_only=True)
    
    class Meta:
        model = LogDispositivo
        fields = '__all__'
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
