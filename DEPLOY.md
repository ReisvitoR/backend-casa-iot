# 🚀 Deploy do Backend Casa IoT

## 📋 Pré-requisitos

- ✅ PostgreSQL configurado (Supabase)
- ✅ Código commitado no Git
- ✅ Variáveis de ambiente configuradas

## 🌐 Opções de Deploy

### 1. 🔥 Railway (Recomendado - Fácil)

```bash
# 1. Instale a CLI do Railway
npm install -g @railway/cli

# 2. Login
railway login

# 3. No diretório do projeto
railway deploy

# 4. Configure as variáveis de ambiente no painel Railway:
# DATABASE_URL=postgresql://...
# DJANGO_SECRET_KEY=your-secret-key
# DJANGO_DEBUG=False
# DJANGO_ALLOWED_HOSTS=*.railway.app
```

### 2. 🟢 Render (Gratuito)

1. Conecte seu repositório no [Render](https://render.com)
2. Escolha "Web Service"
3. Configure:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn config-admin.asgi:application --host 0.0.0.0 --port $PORT`
   - **Environment Variables**:
     ```
     DATABASE_URL=postgresql://...
     DJANGO_SECRET_KEY=your-secret-key
     DJANGO_DEBUG=False
     DJANGO_ALLOWED_HOSTS=*.onrender.com
     ```

### 3. 🟣 Heroku

```bash
# 1. Instale a CLI do Heroku
# 2. Login
heroku login

# 3. Crie o app
heroku create seu-app-casa-iot

# 4. Configure as variáveis
heroku config:set DATABASE_URL="postgresql://..."
heroku config:set DJANGO_SECRET_KEY="your-secret-key"
heroku config:set DJANGO_DEBUG=False
heroku config:set DJANGO_ALLOWED_HOSTS="*.herokuapp.com"

# 5. Deploy
git push heroku main
```

### 4. ☁️ Vercel

1. Conecte seu repositório no [Vercel](https://vercel.com)
2. Configure as variáveis de ambiente
3. Use o arquivo `vercel.json`:

```json
{
  "builds": [
    {
      "src": "config-admin/wsgi.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "config-admin/wsgi.py"
    }
  ]
}
```

## 🔐 Variáveis de Ambiente Necessárias

```env
DATABASE_URL=postgresql://postgres.vpkdjntlyxonsrzzwijn:hk8UQYGH2I8NDPZB@aws-1-sa-east-1.pooler.supabase.com:5432/postgres
DJANGO_SECRET_KEY=django-insecure-ws47k7v^pv5c_=2p@42-8=ok+qk^+68kw4e#lmofiocju434-z
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=*.railway.app,*.render.com,*.herokuapp.com,*.vercel.app
CORS_ALLOWED_ORIGINS=https://your-frontend.vercel.app,https://your-frontend.netlify.app
```

## 🧪 Testar Localmente com Configurações de Produção

```bash
# Ative o ambiente virtual
.\.venv\Scripts\activate

# Instale as dependências de produção
pip install -r requirements.txt

# Colete arquivos estáticos
python manage_production.py collectstatic --noinput

# Execute as migrações
python manage_production.py migrate

# Teste o servidor com Uvicorn (produção)
python manage_production.py runserver
# Ou diretamente:
uvicorn config-admin.asgi:application --host 0.0.0.0 --port 8000 --reload
```

## 📱 URLs da API em Produção

Após o deploy, sua API estará disponível em:

- **Admin**: `https://seu-app.railway.app/admin/`
- **API Root**: `https://seu-app.railway.app/api/`
- **Swagger**: `https://seu-app.railway.app/api/swagger/`
- **Schema**: `https://seu-app.railway.app/api/schema/`

## 🔗 Conectar Frontend

No seu frontend, use a URL base:

```javascript
// React/Next.js
const API_BASE_URL = 'https://seu-app.railway.app/api'

// Exemplo de login
const response = await fetch(`${API_BASE_URL}/auth/login/`, {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    username: 'email@exemplo.com',
    password: 'senha123'
  })
})
```

## 🛡️ Checklist de Segurança

- [ ] `DEBUG = False` em produção
- [ ] Secret key aleatória e segura
- [ ] ALLOWED_HOSTS configurado corretamente
- [ ] CORS configurado apenas para domínios necessários
- [ ] HTTPS habilitado (automático na maioria das plataformas)
- [ ] Variáveis sensíveis em variáveis de ambiente

## 🔧 Comandos Úteis

```bash
# Ver logs (Railway)
railway logs

# Ver logs (Heroku)
heroku logs --tail

# Executar migrações em produção
railway run python manage.py migrate  # Railway
heroku run python manage.py migrate   # Heroku

# Criar superuser em produção
railway run python manage.py createsuperuser  # Railway
heroku run python manage.py createsuperuser   # Heroku
```
