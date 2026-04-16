# 📝 DIO Blog API

API de blog desenvolvida em Python como parte do bootcamp da DIO (Luizalabs), com autenticação JWT, testes automatizados e estrutura baseada em boas práticas de backend.

---

## ⚙️ Tecnologias utilizadas

- Python 3.12
- FastAPI
- SQLite
- SQLAlchemy (ou Databases, dependendo da implementação)
- JWT (PyJWT)
- Pytest
- Poetry

---

## 📌 Funcionalidades

- Cadastro e autenticação de usuários
- Login com JWT
- CRUD de posts
- Proteção de rotas autenticadas
- Validação de dados com schemas
- Testes automatizados

---

## 🔐 Autenticação

A API utiliza **JWT (JSON Web Token)** para proteger rotas privadas.

Fluxo de autenticação:

1. Usuário realiza login
2. Recebe um token JWT
3. Utiliza o token no header das requisições:

Authorization: Bearer <token>

---

## 📦 Instalação e execução

Clone o repositório:
git clone https://github.com/estevaoMG/dio-blog.git
cd dio-blog

Instale as dependências:
poetry install

Execute a aplicação:
poetry run uvicorn src.main:app --reload

---

## 🧪 Testes

poetry run pytest -v

---

## 🗂 Estrutura do projeto

src/
 ├── auth/
 ├── database/
 ├── models/
 ├── routes/
 ├── schemas/
 ├── tests/
 └── main.py

---

## 🚧 Melhorias futuras

- Paginação de posts
- Refresh token JWT
- Deploy com Docker
- CI/CD com GitHub Actions
- Melhorias na documentação Swagger

---

## 👨‍💻 Autor

Estevão Gouveia
Projeto desenvolvido durante o bootcamp da DIO (Luizalabs Backend Python)
