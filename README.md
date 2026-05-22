## Personal Journal API

API de diário pessoal com autenticação JWT, desenvolvida com Django REST Framework e SimpleJWT.

## Funcionalidades

- Registro e login de usuários com JWT
- CRUD de entradas do diário (cada usuário só acessa os próprios dados)
- Entradas públicas visíveis sem autenticação
- Logout com blacklist de token
- Endpoint `/api/me/` para dados do usuário logado
- Grupo `Editor` com permissão de leitura geral

## Endpoints

| Método | URL | Descrição | Auth |
|--------|-----|-----------|------|
| POST | `/api/auth/register/` | Registrar usuário | Não |
| POST | `/api/auth/login/` | Login (retorna access + refresh) | Não |
| POST | `/api/auth/refresh/` | Renovar access token | Não |
| POST | `/api/auth/logout/` | Logout (blacklist do refresh) | Sim |
| GET | `/api/me/` | Dados do usuário logado | Sim |
| GET/POST | `/api/entries/` | Listar/Criar entradas | Sim |
| GET/PUT/PATCH/DELETE | `/api/entries/{id}/` | Detalhar/Editar/Deletar entrada | Sim |
| GET | `/api/journal/public/` | Listar entradas públicas | Não |

## Como rodar localmente

### Requisitos
- Python 3.10+
- pip

### Passo a passo

```bash
# 1. Clone o repositório
git clone https://github.com/rafaelandrier/api-project.git
cd api-project

# 2. Crie e ative o ambiente virtual
python -m venv venv

# Windows (PowerShell):
venv\Scripts\Activate.ps1
# Linux / macOS:
source venv/bin/activate

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Rode as migrations (cria o banco e o grupo Editor automaticamente)
python manage.py migrate

# 5. Crie um superusuário (opcional, para acessar /admin/)
python manage.py createsuperuser

# 6. Suba o servidor
python manage.py runserver
```

O servidor estará disponível em `http://127.0.0.1:8000/`.

## Como testar (PowerShell)

```powershell
# Registrar usuário
$body = @{ username = "maria"; email = "maria@email.com"; password = "senha1234" } | ConvertTo-Json
Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/auth/register/" -Method Post -Body $body -ContentType "application/json"

# Login e captura de tokens
$loginBody = @{ username = "maria"; password = "senha1234" } | ConvertTo-Json
$tokens = Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/auth/login/" -Method Post -Body $loginBody -ContentType "application/json"

# Acessar rota protegida /api/me/
$headers = @{ Authorization = "Bearer $($tokens.access)" }
Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/me/" -Method Get -Headers $headers

# Criar uma entrada no diário
$entry = @{ title = "Meu primeiro dia"; content = "Hoje foi incrível!"; mood = "happy" } | ConvertTo-Json
Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/entries/" -Method Post -Body $entry -Headers $headers -ContentType "application/json"
```

## Tecnologias

- Python 3
- Django 6
- Django REST Framework
- djangorestframework-simplejwt
- SQLite (banco padrão para desenvolvimento)
