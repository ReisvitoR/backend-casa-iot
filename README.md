# 🏠 Casa IoT - Backend API

> Sistema de automação residencial inteligente com Django REST Framework

Uma API completa para gerenciar dispositivos IoT em ambientes residenciais, permitindo controle inteligente de iluminação, climatização e automação de cenas personalizadas.

## 🚀 Demonstração

**API Live:** https://backend-casa-iot.onrender.com/api/  
**Documentação Swagger:** https://backend-casa-iot.onrender.com/swagger/  
**Painel Admin:** https://backend-casa-iot.onrender.com/admin/

## ✨ Funcionalidades

### 🏘️ **Gerenciamento de Residências**
- Cadastro e gestão de casas
- Organização por cômodos
- Controle de acesso por usuário

### 🔌 **Dispositivos IoT**
- Suporte a múltiplos tipos de dispositivos (lâmpadas, sensores, climatização)
- Status em tempo real (ligado/desligado)
- Histórico de atividades e logs

### 🎭 **Automação Inteligente**
- Criação de cenas personalizadas
- Agendamento automático
- Controle temporal (horários específicos)

### 👥 **Sistema de Usuários**
- Autenticação por token
- Perfis personalizados
- Controle de permissões

## 🛠️ Tecnologias

- **Python 3.13** - Linguagem principal
- **Django 5.2.5** - Framework web
- **Django REST Framework** - API REST
- **PostgreSQL** - Banco de dados (Supabase)
- **Uvicorn** - Servidor ASGI
- **Render.com** - Deploy e hospedagem

### 📦 Principais Dependências

```
Django==5.2.5
djangorestframework==3.16.1
django-cors-headers==4.4.0
django-jazzmin==3.0.0
drf-spectacular==0.27.2
psycopg==3.1.19
uvicorn[standard]==0.30.6
whitenoise==6.7.0
```

## 🏗️ Arquitetura

```
Casa IoT Backend/
├── core/                   # App principal
│   ├── models.py          # Modelos de dados
│   ├── serializers.py     # Serialização da API
│   ├── views.py           # Lógica de negócio
│   └── urls.py            # Rotas da API
├── config-admin/          # Configurações
│   ├── settings.py        # Configurações gerais
│   ├── settings_production.py # Produção
│   └── urls.py            # URLs principais
└── manage.py              # CLI do Django
```

## 📊 Modelo de Dados

### Entidades Principais

- **Usuario** - Usuários do sistema
- **Casa** - Residências
- **Comodo** - Ambientes da casa
- **TipoDispositivo** - Categorias de dispositivos
- **Dispositivo** - Dispositivos IoT
- **Cena** - Cenários de automação
- **AcaoCena** - Ações dentro de uma cena
- **LogDispositivo** - Histórico de atividades

## 🚦 Endpoints da API

### 🏠 **Casas**
```
GET    /api/casas/           # Listar casas
POST   /api/casas/           # Criar casa
GET    /api/casas/{id}/      # Detalhes da casa
PUT    /api/casas/{id}/      # Atualizar casa
DELETE /api/casas/{id}/      # Excluir casa
```

### 🚪 **Cômodos**
```
GET    /api/comodos/         # Listar cômodos
POST   /api/comodos/         # Criar cômodo
GET    /api/comodos/{id}/    # Detalhes do cômodo
PUT    /api/comodos/{id}/    # Atualizar cômodo
DELETE /api/comodos/{id}/    # Excluir cômodo
```

### 🔌 **Dispositivos**
```
GET    /api/dispositivos/           # Listar dispositivos
POST   /api/dispositivos/           # Criar dispositivo
GET    /api/dispositivos/{id}/      # Detalhes do dispositivo
PUT    /api/dispositivos/{id}/      # Atualizar dispositivo
DELETE /api/dispositivos/{id}/      # Excluir dispositivo
GET    /api/dispositivos/status/    # Status de todos os dispositivos
```

### 🎭 **Cenas**
```
GET    /api/cenas/           # Listar cenas
POST   /api/cenas/           # Criar cena
GET    /api/cenas/{id}/      # Detalhes da cena
PUT    /api/cenas/{id}/      # Atualizar cena
DELETE /api/cenas/{id}/      # Excluir cena
POST   /api/cenas/{id}/executar/  # Executar cena
```

## 🔧 Instalação e Configuração

### Pré-requisitos
- Python 3.13+
- PostgreSQL ou SQLite
- Git

### 1. Clone o repositório
```bash
git clone https://github.com/ReisvitoR/backend-casa-iot.git
cd backend-casa-iot
```

### 2. Crie um ambiente virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente
Crie um arquivo `.env` baseado no `.env.example`:
```bash
cp .env.example .env
```

Edite o `.env` com suas configurações:
```env
# Configurações do Django
DJANGO_SECRET_KEY=sua-chave-secreta-aqui
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1,seu-dominio.com

# Banco de dados
DATABASE_URL=postgresql://usuario:senha@host:porta/database

# CORS (frontend) pode ser qualquer um.
CORS_ALLOWED_ORIGINS=http://localhost:3000,https://seu-frontend.vercel.app 
```

### 5. Execute as migrações
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Crie um superusuário
```bash
python manage.py createsuperuser
```

### 7. Execute o servidor
```bash
# Desenvolvimento
python manage.py runserver

# Produção
uvicorn config-admin.asgi:application --host 0.0.0.0 --port 8000
```

## 🌐 Deploy

O projeto está configurado para deploy automático no **Render.com**.

### Configuração no Render:

1. **Build Command:**
   ```bash
   chmod +x build.sh && ./build.sh
   ```

2. **Start Command:**
   ```bash
   uvicorn config-admin.asgi:application --host 0.0.0.0 --port $PORT
   ```

3. **Variáveis de Ambiente:**
   ```
   DATABASE_URL=sua-url-do-postgres
   DJANGO_ALLOWED_HOSTS=seu-dominio.onrender.com
   CORS_ALLOWED_ORIGINS=https://seu-frontend.vercel.app
   ```

## 📝 Uso da API

### Autenticação

A API usa autenticação por token. Para obter um token:

```bash
curl -X POST https://backend-casa-iot.onrender.com/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"username": "seu_usuario", "password": "sua_senha"}'
```

Use o token nas requisições:
```bash
curl -H "Authorization: Token seu_token_aqui" \
  https://backend-casa-iot.onrender.com/api/dispositivos/
```

### Exemplos de Uso

**Criar um dispositivo:**
```json
POST /api/dispositivos/
{
  "nome": "Lâmpada da Sala",
  "tipo_dispositivo": 1,
  "comodo": 1,
  "status": true,
  "intensidade": 80
}
```

**Criar uma cena:**
```json
POST /api/cenas/
{
  "nome": "Modo Cinema",
  "descricao": "Diminui as luzes para assistir filme",
  "ativa": true,
  "acoes": [
    {
      "dispositivo": 1,
      "acao": "intensidade",
      "valor": "20"
    }
  ]
}
```

## 🧪 Testes

```bash
# Executar todos os testes
python manage.py test

# Executar testes específicos
python manage.py test core.tests
```

## 📚 Documentação

- **Swagger UI:** `/swagger/` - Interface interativa da API
- **ReDoc:** `/redoc/` - Documentação alternativa
- **Admin Panel:** `/admin/` - Interface administrativa

## 🤝 Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👨‍💻 Autor

**ReisvitoR** - [GitHub](https://github.com/ReisvitoR)

