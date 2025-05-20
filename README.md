# 🧠 Syntaxia Synapse

## 🇧🇷 Português

Uma API REST construída com **FastAPI** e **MongoDB** para gerenciamento de estímulos motivacionais, com suporte a CRUD completo, paginação, testes automatizados e deploy via Docker.

### 🚀 Funcionalidades

- ✅ Inserção de estímulos (`POST /estimulo`)
- ✅ Busca aleatória com filtro por tipo (`GET /estimulo?tipo=texto`)
- ✅ Listagem paginada (`GET /estimulos?skip=0&limit=10`)
- ✅ Atualização parcial (`PUT /estimulo/{id}`)
- ✅ Deleção (`DELETE /estimulo/{id}`)
- ✅ Testes automatizados com `pytest` + `httpx`
- ✅ Containerização com Docker + Docker Compose
- ✅ Variáveis de ambiente com `.env`
- ✅ Pronto para CI com GitHub Actions

## 🇺🇸 English

A REST API built with **FastAPI** and **MongoDB** to manage motivational prompts, featuring full CRUD operations, pagination, automated testing, and Docker deployment.

### 🚀 Features

- ✅ Add new prompts (`POST /estimulo`)
- ✅ Fetch random prompt filtered by type (`GET /estimulo?tipo=texto`)
- ✅ Paginated list (`GET /estimulos?skip=0&limit=10`)
- ✅ Partial updates (`PUT /estimulo/{id}`)
- ✅ Deletion (`DELETE /estimulo/{id}`)
- ✅ Automated tests with `pytest` + `httpx`
- ✅ Docker + Docker Compose setup
- ✅ Environment variables with `.env`
- ✅ Ready for CI with GitHub Actions

---

## 🛠️ Tecnologias | Technologies

- Python 3.12+
- FastAPI
- MongoDB (Motor async)
- Docker / Docker Compose
- Pydantic
- pytest + httpx
- python-dotenv

---

## 📦 Instalação local | Local setup (no Docker)

```bash
git clone https://github.com/your-user/syntaxia-synapse.git
cd syntaxia-synapse

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate   # Windows

pip install -r requirements-dev.txt
cp .env.example .env

uvicorn api.main:app --reload
```

Acesse | Access: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🐳 Docker

```bash
docker-compose up --build
```

---

## ✅ Testes | Running tests

```bash
pytest
```

---

## 🧪 .env

```dotenv
MONGO_URL=mongodb://mongo:27017
```

---

## 📂 Estrutura | Structure

```
.
├── api/
│   ├── main.py
│   ├── db/
│   │   ├── mongo.py
│   │   └── seed.py
│   └── routes/
│       └── estimulo.py
├── tests/
│   └── test_estimulo.py
├── docker-compose.yml
├── Dockerfile
├── requirements-dev.txt
├── .env.example
└── README.md
```

---

## 👥 Contribuindo | Contributing

1. Fork
2. Create a branch
3. Commit and open a pull request

---

## 📬 Contato | Contact

**Nome | Name:** Victoria Lara  
**LinkedIn:** [linkedin.com/in/victorialara](https://www.linkedin.com/in/victorialara)