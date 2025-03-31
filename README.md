# Fast Zero

Uma API RESTful para uma aplicação de tarefas (Todo) construída com FastAPI, SQLAlchemy e PostgreSQL.

## Requisitos

- Python 3.13+
- Poetry
- PostgreSQL
- Docker (opcional)

## Instalação

### Clone o repositório

```bash
git clone <url-do-repositório>
cd fastapi_zero_duno
```

### Instale as dependências

```bash
poetry install
```

## Variáveis de Ambiente

Crie um arquivo `.env` na pasta raiz com as seguintes variáveis:

```env
DATABASE_URL=sua_url_conexão_com_o_banco
SECRET_KEY=sua_chave_secreta
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## Executando Localmente

### 1. Configure o banco de dados

Certifique-se de que o PostgreSQL esteja rodando e que sua DATABASE_URL no arquivo `.env` esteja correta.

### 2. Execute as migrações do banco de dados

```bash
poetry run alembic upgrade head
```

### 3. Inicie a aplicação

```bash
poetry run task run
```

A API estará disponível em <http://localhost:8000>

## Executando com Docker

Você também pode executar a aplicação usando Docker Compose:

```bash
docker compose up -d
```

Isso iniciará tanto o banco de dados PostgreSQL quanto a aplicação FastAPI.

## Documentação da API

Quando a aplicação estiver rodando, você pode acessar a documentação Swagger em:

- <http://localhost:8000/docs>
- <http://localhost:8000/redoc>

## Executando Testes

```bash
poetry run task test
```

## Ferramentas de Desenvolvimento

Este projeto utiliza várias ferramentas de desenvolvimento:

- `ruff` para linting e formatação
- `pytest` para testes
- `coverage` para cobertura de testes
- `taskipy` para automação de tarefas

Você pode executar essas ferramentas usando os seguintes comandos:

```bash
# Verificar o código
poetry run task lint

# Formatar o código
poetry run task format

# Executar testes com cobertura
poetry run task test
