# Mobshow Backend

## 📖 Sobre o projeto
Mobshow é uma plataforma web desenvolvida para as pessoas jogarem quiz diretamente do YouTube na nossa plataforma com seus amigos!

### 🕸️ Fluxo de uma requisição
```
Request → Router → Service → Repository → Banco
                ↑               ↑
           schemas/          entities/
         (validação)        (domínio)
```
Cada camada só conhece a camada imediatamente abaixo. O `dependencies/` é o único ponto que conecta as camadas entre si.

## ⚙️ Setup e instalação

### Pré-requisitos
- Python
- PostgreSQL
- Redis

### 1. Crie e ative o ambiente virtual

```bash
python -m venv .venv

# Linux/Mac
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Configure as variáveis de ambiente

```bash
cp .env.example .env
```

Edite o `.env` com seus valores.

### 4. Inicie a aplicação

```bash
uvicorn main:app --host 0.0.0.0 --reload --app-dir src
```
Documentação em `/docs`.

## 🤐 Variáveis de ambiente

| Variável | Descrição | Exemplo |
|---|---|---|
| `REDIS_URL` | URL de conexão com o Redis | `redis://localhost:6379` |
| `LOG_LEVEL` | Nível de log da aplicação | `INFO` |

Exemplo de `.env`:

```env
REDIS_URL=redis://localhost:6379
LOG_LEVEL=INFO
```

## 📍 Endpoints

### Health

| Método | Rota | Descrição |
|---|---|---|
| `GET` | `/health` | Verifica se a API está online |

## 📁 Estrutura do Projeto
```
src/
├── database/        # Inicialização da camada de dados (Redis, Postgres)
├── dependencies/    # Cola para abstração das camadas (desacoplamento)
├── entities/        # Representação completa dos objetos do negócio
├── exceptions/      # Erros de domínio
├── middlewares/     # Lógica transversal a todas as requisições
├── repositories/    # Abstração da camada de dados
├── routers/         # Recebimento de requests e validação de dados
├── schemas/         # DTOs
├── services/        # Lógica de negócio
├── config.py        # Centralização de envs e configs
└── main.py          # Orquestração do App
```