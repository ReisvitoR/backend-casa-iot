
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class Usuario(AbstractUser):
    """Usuário customizado baseado no User do Django"""
    email = models.EmailField(unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"

class Casa(models.Model):
    nome = models.CharField(max_length=255)
    endereco = models.TextField(blank=True, null=True)
    timezone = models.CharField(max_length=50, default='America/Sao_Paulo')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='casas')

    class Meta:
        verbose_name = "Casa"
        verbose_name_plural = "Casas"
        ordering = ['nome']

    def __str__(self):
        return f"{self.nome} - {self.usuario.first_name}"

class TipoDispositivo(models.Model):
    """Tipos de dispositivos disponíveis"""
    nome = models.CharField(max_length=50, unique=True)
    icone = models.CharField(max_length=50, blank=True, null=True)
    categoria = models.CharField(max_length=50, choices=[
        ('iluminacao', 'Iluminação'),
        ('climatizacao', 'Climatização'),
        ('seguranca', 'Segurança'),
        ('entretenimento', 'Entretenimento'),
        ('eletrodomestico', 'Eletrodoméstico'),
        ('outro', 'Outro'),
    ])
    
    class Meta:
        verbose_name = "Tipo de Dispositivo"
        verbose_name_plural = "Tipos de Dispositivos"
        ordering = ['categoria', 'nome']
    
    def __str__(self):
        return self.nome

class Comodo(models.Model):
    nome = models.CharField(max_length=255)
    background_url = models.CharField(max_length=255, blank=True, null=True)
    casa = models.ForeignKey(Casa, on_delete=models.CASCADE, related_name='comodos')

    class Meta:
        verbose_name = "Cômodo"
        verbose_name_plural = "Cômodos"
        ordering = ['casa', 'nome']
        unique_together = ['casa', 'nome']  # Evita cômodos duplicados na mesma casa

    def __str__(self):
        return f"{self.nome} - {self.casa.nome}"

class Dispositivo(models.Model):
    nome = models.CharField(max_length=255)
    estado = models.BooleanField(default=False)
    tipo = models.ForeignKey(TipoDispositivo, on_delete=models.CASCADE, related_name='dispositivos')
    comodo = models.ForeignKey(Comodo, on_delete=models.CASCADE, related_name='dispositivos')
    potencia = models.FloatField(blank=True, null=True, help_text="Potência em Watts")
    marca = models.CharField(max_length=100, blank=True, null=True)
    modelo = models.CharField(max_length=100, blank=True, null=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    mac_address = models.CharField(max_length=17, blank=True, null=True)
    ativo = models.BooleanField(default=True)
    ultimo_ping = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = "Dispositivo"
        verbose_name_plural = "Dispositivos"
        ordering = ['comodo', 'nome']
        unique_together = ['comodo', 'nome']  # Evita dispositivos duplicados no mesmo cômodo

    def __str__(self):
        return f"{self.nome} ({self.comodo.nome})"

    @property
    def status_conexao(self):
        """Verifica se o dispositivo está online"""
        if not self.ultimo_ping:
            return "Nunca conectado"
        
        agora = timezone.now()
        diferenca = agora - self.ultimo_ping
        
        if diferenca.seconds < 300:  # 5 minutos
            return "Online"
        elif diferenca.seconds < 3600:  # 1 hora
            return "Instável"
        else:
            return "Offline"

class Cena(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)
    ativa = models.BooleanField(default=False)
    casa = models.ForeignKey(Casa, on_delete=models.CASCADE, related_name='cenas')
    indisponivel_ate = models.DateTimeField(blank=True, null=True, help_text="Data/hora até quando a cena ficará indisponível")
    tempo_execucao = models.FloatField(blank=True, null=True, help_text="Tempo total de execução em segundos")
    favorita = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Cena"
        verbose_name_plural = "Cenas"
        ordering = ['-favorita', 'nome']
        unique_together = ['casa', 'nome']  # Evita cenas duplicadas na mesma casa

    def __str__(self):
        try:
            return f"{self.nome} - {self.casa.nome}"
        except:
            return f"{self.nome} - Casa #{self.casa_id}"

    @property
    def pode_executar(self):
        """Verifica se a cena pode ser executada agora"""
        from django.utils import timezone
        if not self.ativa:
            return False
        if self.indisponivel_ate and self.indisponivel_ate > timezone.now():
            return False
        return True

    @property
    def status_disponibilidade(self):
        """Retorna o status atual da cena"""
        from django.utils import timezone
        if not self.ativa:
            return "inativa"
        if self.indisponivel_ate and self.indisponivel_ate > timezone.now():
            return "temporariamente_indisponivel"
        return "disponivel"

class AcaoCena(models.Model):
    ordem = models.PositiveIntegerField()
    intervalo_tempo = models.FloatField(default=0.0, help_text="Intervalo em segundos antes desta ação")
    estado_desejado = models.BooleanField()
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE, related_name='acoes_cena')
    cena = models.ForeignKey(Cena, on_delete=models.CASCADE, related_name='acoes')
    condicional = models.BooleanField(default=False, help_text="Se True, só executa se o estado atual for diferente")

    class Meta:
        verbose_name = "Ação da Cena"
        verbose_name_plural = "Ações das Cenas"
        ordering = ['cena', 'ordem']
        unique_together = ['cena', 'ordem']  # Evita ordem duplicada na mesma cena

    def __str__(self):
        return f"Ação {self.ordem}: {self.dispositivo.nome} -> {'ON' if self.estado_desejado else 'OFF'}"

class LogDispositivo(models.Model):
    """Log de mudanças de estado dos dispositivos"""
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE, related_name='logs')
    estado_anterior = models.BooleanField()
    estado_novo = models.BooleanField()
    origem = models.CharField(max_length=50, choices=[
        ('manual', 'Manual'),
        ('cena', 'Cena'),
        ('agendamento', 'Agendamento'),
        ('api', 'API'),
        ('automacao', 'Automação'),
    ])
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True)
    cena = models.ForeignKey(Cena, on_delete=models.SET_NULL, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Log do Dispositivo"
        verbose_name_plural = "Logs dos Dispositivos"
        ordering = ['-timestamp']
    
    def __str__(self):
        return f"{self.dispositivo.nome}: {self.estado_anterior} -> {self.estado_novo}"
